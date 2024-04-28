import unittest
from source.dealer import Dealer

class TestDealer(unittest.TestCase):

    def test_dealer_init(self):
        dealer = Dealer(2, 10, 104, 4, {7:11,9:3})
        self.assertEqual(len(dealer.game_deck.card_deck), 108)
        self.assertEqual(len(dealer.players), 2)
        self.assertIsNotNone(dealer.players['0'].hand)
        self.assertEqual(len(dealer.board), 4)
