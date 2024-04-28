from source.deck import Deck
from source.card import Card
from source.player import Player
from source.board_row import BoardRow

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

        # Give dealt cards to players
        j = 0
        for id in self.players.keys():
            self.players[id].hand = player_hand[j]
            if j < number_of_players:
                j += 1

        # Set up board
        self.board: BoardRow = []
        for row in range(board_size):
            self.board.append(BoardRow(self.game_deck.card_deck[deck_size+row],5))

    def play_card(Player, Card):
        pass

    def start_game() -> None:
        pass

    def end_game() -> None:
        pass

    def play_round() -> None:
        pass
