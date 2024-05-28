from source.card import Card
from collections import deque

'''
A BoardRow is essentially a stack data structure containing 
Card objects. It also has the ability to return the value of 
the largest numbered card currently in the row, along with 
the ability to clear the stack to start fresh with a new Card.
'''
class BoardRow:

    def __init__(self, id: int, max_size: int) -> None:
        self.board_row = deque()
        self.id = id
        self.max_size = max_size

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    def peek(self) -> int:
        return self.board_row[0].number

    def add(self, new_card: Card) -> None:
        self.board_row.appendleft(new_card)

    def is_full(self) -> bool:
        if (len(self.board_row) >= self.max_size):
            return True
        return False

    def reset(self, new_start_card: Card) -> deque[Card]:
        # Get all elements of the board row to return to caller
        row_contents = self.board_row.copy()

        # Clear the queue of existing Card objects
        self.board_row.clear()

        # Set new start card for board row
        self.board_row.appendleft(new_start_card)

        return row_contents

    def sum_row(self) -> int:
        sum: int = 0
        for card in self.board_row:
            sum += card.points
        return sum