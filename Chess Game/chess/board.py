class ChessBoard:
    def __init__(self):
        self.EMPTY = "    "
        self.arr = [
            ["W_Rk", "W_Kn", "W_Bi", "W_Kg", "W_Qn", "W_Bi", "W_Kn", "W_Rk"],
            ["W_Pn"] * 8,
            [self.EMPTY] * 8,
            [self.EMPTY] * 8,
            [self.EMPTY] * 8,
            [self.EMPTY] * 8,
            ["B_Pn"] * 8,
            ["B_Rk", "B_Kn", "B_Bi", "B_Qn", "B_Kg", "B_Bi", "B_Kn", "B_Rk"]
        ]
        self.knight_symbol = "W_Kn"  

    def display_board(self):
        print("\n\t\t ______________________________________________________________")
        print("\t\t        1       2       3       4       5       6        7         8")
        for i, row in enumerate(self.arr, start=1):
            print(f"\t\t {i}  ", end="")
            print(" [ " + " ][ ".join(row) + " ]")

    def update_position(self, old_pos, new_pos, symbol):
        """Update the board after moving a piece."""
        old_row, old_col = old_pos
        new_row, new_col = new_pos

        # Clear the old position
        self.arr[old_row][old_col] = self.EMPTY

        # Place the piece at the new position
        self.arr[new_row][new_col] = symbol
