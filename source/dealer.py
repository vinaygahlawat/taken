from source.deck import Deck
from source.card import Card
from source.player import Player

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

    def __init__(self, number_of_players: int, deck_size: int, card_point_map: dict) -> None:
        # Set up Players
        self.players = {}
        for i in range(0, number_of_players):
            id = str(i)
            self.players[id] = Player(self, id)

        # Deal Cards
        self.game_deck: Deck = Deck(deck_size, card_point_map)

    def play_card(Player, Card):
        pass

    def start_game() -> None:
        pass

    def end_game() -> None:
        pass

    def play_round() -> None:
        pass
