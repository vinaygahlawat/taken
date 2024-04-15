import unittest
from source.deck import Deck
from source.card import Card

class TestDeck(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.deck = Deck(10, {4:3,7:11})

    def test_deck_size(self):
        self.assertEqual(len(self.deck.card_deck), 10, "The size of the card deck is incorrect.")

    def test_deck_card_points(self):
        self.assertEqual(self.deck.card_deck[1].points, 1, "The value of card number 1 is incorrect, should be 1.")
        self.assertEqual(self.deck.card_deck[3].points, 3, "The value of card number 4 is incorrect, should be 3.")
        self.assertEqual(self.deck.card_deck[6].points, 11, "The value of card number 7 is incorrect, should be 11.")


if __name__ == '__main__':
    unittest.main()