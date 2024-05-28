from source.board import Board
from source.deck import Deck
from source.card import Card
from source.player import Player
from source.utility import print_to_file

'''
The Dealer object will be responsible for managing match play.
This means that all object interactions will funnel throught the Dealer.
The Dealer:
    * Initiates the start of match play
        * Creates the game paramenters (e.g. board size, number of players)
        * Initializes the number of Players
        * Prepares the Deck of Card objects

'''
class Dealer:

    def __init__(self, number_of_players: int, rounds_per_game: int, deck_size: int, board_size: int, card_point_map: dict) -> None:

        self.number_of_players = number_of_players
        self.deck_size = deck_size
        self.board_size = board_size
        self.rounds_per_game = rounds_per_game
        self.card_point_map = card_point_map

        # Set up Players
        self.players = {}
        for i in range(0, number_of_players):
            id = str(i)
            self.players[id] = Player(self, id)

        # Create a scoreboard
        self.scoreboard = {}
        for player in self.players:
            self.scoreboard[player] = 0

    def start_match(self) -> None:
        print_to_file(f'Match begins.')

        continue_match: bool = True
        while continue_match:
        # Start a game
            self.start_game()

            # End match because end state has been reached
            if self.end_game():
                print_to_file(f'Detected a match winner...')
                continue_match = False
                self.end_match()

        print_to_file(f'Match ended.')

    def start_game(self) -> None:
        print_to_file(f'\tGame begins.')

        # Deal Cards
        self.game_deck: Deck = Deck(self.deck_size + self.board_size, self.card_point_map)
        self.game_deck.shuffle()
        player_hand = []
        for i in range(self.number_of_players):
            hand = []
            player_hand.append(hand)

        number_of_cards_to_deal = self.rounds_per_game * self.number_of_players

        for i in range(number_of_cards_to_deal):
            player = i % self.number_of_players
            card = self.game_deck.card_deck[i]
            player_hand[player].append(card)

        # Save off cards to initialize board
        board_cards: list[Card] = []
        for i in range(self.board_size):
            card = self.game_deck.card_deck[number_of_cards_to_deal + i]
            board_cards.append(card)

        # Give dealt cards to players
        j = 0
        for id in self.players.keys():
            self.players[id].hand = player_hand[j]
            if j < self.number_of_players:
                j += 1

        # Initialize Board for match play
        self.board = Board(self.board_size, 5) # TODO parameterize max board row length, hard-coded to 5 for now
        self.match_threshold: int = 25 # TODO parameterize the point threshold for match end
        self.board.initialize_rows(board_cards)
        print_to_file(f'\t\tBoard at beginning of game:')
        self.board.show_board()

        # Prepare game play
        self.rounds = self.rounds_per_game

        # Loop for the number of rounds there are (as determined by the number of cards dealt)
        for i in range(self.rounds):
            # Play a round
            self.play_round()

            # Show game board at the end of every round
            print_to_file(f'\t\tEnd of round --> Current board:')
            self.board.show_board()

        print_to_file(f'\tGame ends.')

    def end_game(self) -> bool:
        print_to_file(f'\t Check for end game state...')
        is_match_finished: bool = False

        for player in self.scoreboard.keys():
            print_to_file(f'\t\tPlayer {player} has score: {self.scoreboard[player]}')
            if self.scoreboard[player] > self.match_threshold:
                print_to_file(f'\t\t\tPlayer {player} has crossed the threshold of {self.match_threshold}.')
                is_match_finished = True

        return is_match_finished

    def end_match(self) -> None:
        print_to_file(f'Begin end match wrap-up.')
        match_winner = self.match_winner()
        print_to_file(f'Match is over, and the winner is {match_winner}! Congrats!')
        print_to_file(f'Complete end match wrap-up.')

    def play_round(self) -> None:
        print_to_file(f'\t\t*** Round Started ***\n')

        # Get a card from each player
        cards_played: list[Card] = []
        map_card_to_player = {}
        for id in self.players.keys():
            player = self.players[id]
            card = player.play_card()
            print_to_file(f'\t\t\tPlayer {player.id} played Card: {card}')
            cards_played.append(card)
            map_card_to_player[card.number] = player.id

        # Sort played cards so turns can commence, beginning with
        # the player with the lowest-numbered played card.
        cards_played.sort(key=Card.sortFunc)

        # Start turns with player with the lowest card
        # Add them to the board
        for card in cards_played:
            self.play_turn(card, map_card_to_player[card.number])

        del(cards_played)
        self.show_scoreboard()
        print_to_file(f'\t\t*** Round Complete. ***\n')

    def play_turn(self, card, player_id) -> None:
        result = self.board.add_card(card)
        if result == []:
            # card was successfully added to board, nothing else to do.
            print_to_file(f'\t\t\t\tCard {card} was successfully added to the board.')
        else:
            point_tally = 0
            row_taken = ''
            for card in result:
                row_taken += f'{card} '
                point_tally += card.points
            if row_taken != '':
                print_to_file("\t\t\t\tRow TakeN: " + row_taken)
                # Add point tally from row taken to the player score
                self.scoreboard[player_id] += point_tally

    def show_scoreboard(self):
        print_to_file(f'\n\t\t******************************')
        print_to_file(f'\t\tSCOREBOARD: {self.scoreboard}')
        print_to_file(f'\t\t******************************\n')

    def match_winner(self) -> Player:
        winner: Player = None

        for player in self.scoreboard.keys():
            if winner is None:
                winner = player
            elif self.scoreboard[player] < self.scoreboard[winner]:
                winner = player

        return winner
