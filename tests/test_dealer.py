import unittest
from source.dealer import Dealer

class TestDealer(unittest.TestCase):

    def test_dealer_init(self):
        dealer = Dealer(2, 10, {7:11,9:3})
        self.assertEqual(len(dealer.game_deck.card_deck), 10)
        self.assertEqual(len(dealer.players), 2)
