from source.board_row import BoardRow
from source.card import Card
from source.utility import print_to_file

class Board:

    def __init__(self, board_size: int, max_board_row_size: int) -> None:

        # Set up board
        self.board_rows: list[BoardRow] = []
        for row_id in range(board_size):
            self.board_rows.append(BoardRow(row_id, max_board_row_size))

    def initialize_rows(self, starting_cards: list[Card]):
        for i in range(len(self.board_rows)):
            self.board_rows[i].add(starting_cards[i])

    def add_card(self, card: Card) -> list[Card]:
        row_to_place: int = -1
        min_diff: int = 1000
        for row in self.board_rows:
            if card.number - row.peek() < min_diff:
                min_diff = card.number - row.peek()
                row_to_place = row.id

        if row_to_place == -1:
            print_to_file(f'Card {card.number} does not fit in any row. Player must choose row to take.')
            return None

        print_to_file(f'\t\t\t\tPlacing {card.number} in row {row_to_place}.')
        if self.board_rows[row_to_place].is_full():
            print_to_file(f'\t\t\t\tRow is full, player will take cards and row will reset.')
            return self.board_rows[row_to_place].reset(card)
        else:
            self.board_rows[row_to_place].add(card)
            return []


    def show_board(self) -> None:
        print_to_file(f'\n\t\t************************************************************')
        for row in self.board_rows:
            board_row = 'Board Row:\t'
            for card in row.board_row:
                board_row += f'\t\t{card.number}|{card.points}'
            print_to_file(f'\t\t{board_row}')
        print_to_file(f'\t\t************************************************************\n')
