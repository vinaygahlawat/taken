import unittest
from source.card import Card

class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.card = Card(33, 7)

    def test_number_value(self):
        self.assertEqual(self.card.number, 33, "The card number value is incorrect.")
    
    def test_points_value(self):
        self.assertEqual(self.card.points, 7, "The card point value is incorrect.")

if __name__ == '__main__':
    unittest.main()
