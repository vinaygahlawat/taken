from source.board_row import BoardRow

class Board:

    def __init__(self, board_size: int, max_board_row_size: int) -> None:

        # Set up board
        self.board_rows: list[BoardRow] = []
        for row_id in range(board_size):
            self.board_rows.append(BoardRow(row_id, max_board_row_size))
