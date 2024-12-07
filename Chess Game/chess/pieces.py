class Piece:
    def __init__(self, name):
        self.name = name

    def is_empty(self, board, x, y):
        return board[x][y] == "    "

class Knight(Piece):
    def __init__(self, name="Knight"):
        super().__init__(name)

    def is_valid_move(self, x, y, new_x, new_y):
        return (new_x, new_y) in [
            (x - 2, y - 1), (x - 2, y + 1),
            (x + 2, y - 1), (x + 2, y + 1),
            (x - 1, y - 2), (x - 1, y + 2),
            (x + 1, y - 2), (x + 1, y + 2)
        ]
