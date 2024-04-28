import unittest
from source.board import Board

class TestBoard(unittest.TestCase):

    def test_board_init(self):
        board = Board(4, 5)
        self. assertEqual(len(board.board_rows), 4)