from source.card import Card
from random import randint

class Deck:

    def __init__(self, size, point_values) -> None:
        self.card_deck = []

        for i in range (1, size+1):
            card = Card(i, point_values.get(i,1))
            self.card_deck.append(card)

    def shuffle(self) -> None:
        deck_size = len(self.card_deck)
        for card in self.card_deck:
            # Pick a random card in the deck and swap it around
            swap_index = randint(0, deck_size-1)
            temp: Card = self.card_deck[swap_index]
            self.card_deck[swap_index] = card
            card = temp
