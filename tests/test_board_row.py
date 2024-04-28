import unittest
from collections import deque
from source.board_row import BoardRow
from source.card import Card

class TestBoardRow(unittest.TestCase):

    def test_max_size(self):
        row = BoardRow(0, 3)
        self.assertEqual(row.max_size, 3)

    def test_add_card(self):
        row = BoardRow(0, 5)
        row.add(Card(4,3))
        row.add(Card(6,1))
        self.assertEqual(row.peek(), 6)
        self.assertFalse(row.is_full())

    def test_row_full(self):
        row = BoardRow(0, 5)
        row.add(Card(4,3))
        row.add(Card(5,1))
        row.add(Card(7,11))
        row.add(Card(21,7))
        self.assertFalse(row.is_full())
        row.add(Card(33,2))
        self.assertTrue(row.is_full())
        row.add(Card(45,1))
        self.assertTrue(row.is_full())

    def test_row_reset(self):
        row = BoardRow(0, 5)
        row.add(Card(4,3))
        row.add(Card(5,1))
        row.add(Card(7,11))
        row.add(Card(21,7))
        self.assertFalse(row.is_full())
        row.add(Card(33,2))
        self.assertTrue(row.is_full())
        contents = row.reset(Card(2,1))
        self.assertTrue(isinstance(contents, deque))
        self.assertTrue(isinstance(contents[0], Card))
        self.assertEqual(len(contents), 5)
        self.assertEqual(row.max_size, 5)
        self.assertEqual(row.peek(), 2)
        self.assertFalse(row.is_full())


if __name__ == '__main__':
    unittest.main()