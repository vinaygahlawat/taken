import unittest
from source.player import Player
from source.card import Card

class TestPlayer(unittest.TestCase):

    def test_player_init(self):
        player = Player(None, '0')
        self.assertListEqual(player.hand, [])
        self.assertEqual(player.id, '0')

    def test_player_set_hand(self):
        player = Player(None, '0')
        test_hand = [Card(1, 1), Card(7,3)]
        player.hand = test_hand
        self.assertListEqual(player.hand, test_hand)
        self.assertEqual(player.hand[0].number, 1)
        self.assertEqual(player.hand[0].number, test_hand[0].number)
        self.assertEqual(player.hand[1].points, 3)
        self.assertEqual(player.hand[1].points, test_hand[1].points)

    def test_choose_card(self):
        player = Player(None, '0')
        player.hand = [Card(2, 7), Card(7,3)]
        card = player.choose_card()
        self.assertEqual(card.number, 2)
        self.assertEqual(card.points, 7)


if __name__ == '__main__':
    unittest.main()