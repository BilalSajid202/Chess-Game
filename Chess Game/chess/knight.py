class Knight:
    def __init__(self, board):
        self.board = board
        self.position = (0, 1)  
    def knight_movement(self):
        try:
            print("\nMove the Knight to a new position:")
            new_row = int(input("Row (1-8): ")) - 1
            new_col = int(input("Column (1-8): ")) - 1

            if self.is_valid_move(new_row, new_col):
                self.board.update_position(self.position, (new_row, new_col), "W_Kn")
                self.position = (new_row, new_col)
                print(f"Knight moved to ({new_row + 1}, {new_col + 1}).")
            else:
                print("Invalid move. Knights move in an L-shape only.")
        except ValueError:
            print("Invalid input. Please enter numeric values between 1 and 8.")
        except IndexError as e:
            print(f"Error: {e}")

    def is_valid_move(self, new_row, new_col):
        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            return False
        row_diff = abs(new_row - self.position[0])
        col_diff = abs(new_col - self.position[1])
        return (row_diff, col_diff) in [(2, 1), (1, 2)]


    def display_possible_moves(self):
        """Display the board with all possible moves for the Knight."""
        possible_moves = self.get_possible_moves()
        temp_board = [['.' for _ in range(8)] for _ in range(8)]

        for row, col in possible_moves:
            temp_board[row][col] = '*'
 
        temp_board[self.position[0]][self.position[1]] = 'N'

        print("\nPossible Moves:")
        for row in temp_board:
            print(' '.join(row))

    def get_possible_moves(self):
        """Calculate all possible moves for the Knight from its current position."""
        possible_moves = []
        row, col = self.position
        knight_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                possible_moves.append((new_row, new_col))

        return possible_moves


