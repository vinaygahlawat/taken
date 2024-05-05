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

        # Set up Players
        self.players = {}
        for i in range(0, number_of_players):
            id = str(i)
            self.players[id] = Player(self, id)

        # Deal Cards
        self.game_deck: Deck = Deck(deck_size + board_size, card_point_map)
        player_hand = []
        for i in range(number_of_players):
            hand = []
            player_hand.append(hand)

        number_of_cards_to_deal = rounds_per_game * number_of_players

        for i in range(number_of_cards_to_deal):
            player = i % number_of_players
            card = self.game_deck.card_deck[i]
            player_hand[player].append(card)

        # Save off cards to initialize board
        board_cards: list[Card] = []
        for i in range(board_size):
            card = self.game_deck.card_deck[number_of_cards_to_deal + i]
            board_cards.append(card)

        # Give dealt cards to players
        j = 0
        for id in self.players.keys():
            self.players[id].hand = player_hand[j]
            if j < number_of_players:
                j += 1

        # Initialize Board for match play
        self.board = Board(board_size, 5) # TODO parameterize max board row length, hard-coded to 5 for now
        self.board.initialize_rows(board_cards)

        # Prepare game play
        self.rounds = rounds_per_game

    def start_match(self) -> None:
        print_to_file(f'Match begins.')

#        while not self.end_game:
        # Start a game
        self.start_game()

        # End match because end state has been reached
        self.end_match()

        print_to_file(f'Match ended.')

    def start_game(self) -> None:
        print_to_file(f'\tGame begins.')

        # Loop for the number of rounds there are (as determined by the number of cards dealt)
        for i in range(self.rounds):
            # Play a round
            self.play_round()

            # Show game board at the end of every round
            print_to_file(f'\tEnd of round --> Current board:')
            self.board.show_board()


        print_to_file(f'\tGame ends.')

    def end_game(self) -> bool:
        print_to_file(f'\t Check for end game state...')

    def end_match(self) -> None:
        print_to_file(f'Begin end match wrap-up.')

        print_to_file(f'Complete end match wrap-up.')

    def play_round(self) -> None:
        print_to_file(f'\t\t*** Round Started ***')

        # Get a card from each player
        cards_played: list[Card] = []
        for id in self.players.keys():
            player = self.players[id]
            player_card = player.play_card()
            print_to_file(f'\t\t\t\tPlayer {player.id} played Card: {player_card.number}')
            cards_played.append(player_card)

        # Sort played cards so turns can commence, beginning with
        # the player with the lowest-numbered played card.
        cards_played.sort(key=Card.sortFunc)

        # Start turns with player with the lowest card
        # Add them to the board
        # while len(cards_played) > 0:
        for card in cards_played:
            self.play_turn(card)

        del(cards_played)
        print_to_file(f'\t\t*** Round Complete. ***')

    def play_turn(self, card) -> None:
        result = self.board.add_card(card)
        if result == None:
            # Card cannot be placed in any row, so Player must choose row to replace
            # TODO: add functionality for asking player for row choice
            print_to_file(f'Player must choose row to replace')
        else:
            # del(cards_played[0])
            row_taken = ''
            for card in result:
                row_taken += f'{card.number}|{card.points}\t'
            if row_taken != '':
                print_to_file("\t\t\tRow TakeN: " + row_taken)
            # TODO: add functionality to sum up card points and add to scoreboard
