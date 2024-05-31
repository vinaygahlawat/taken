import unittest
from source.dealer import Dealer

class TestDealer(unittest.TestCase):

    def test_dealer_init(self):
        dealer = Dealer(2, 10, 104, 4, {7:11,9:3})
        self.assertEqual(dealer.deck_size, 104)
        self.assertEqual(dealer.board_size, 4)
        self.assertEqual(dealer.rounds_per_game, 10)
        self.assertEqual(len(dealer.players), 2)
        self.assertIsNotNone(dealer.players['0'].hand)
        self.assertIsNotNone(dealer.players['1'].hand)
