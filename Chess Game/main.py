from chess.board import ChessBoard
from chess.knight import Knight
from chess.utils import display_group_details
from chess.linked_list import LinkedList

def main():
    try:
        reset = LinkedList()
        back = LinkedList()

        # Initialize board and knight logic
        board = ChessBoard()
        knight = Knight(board)
  
        reset.transfer_board(board.arr)
        back.transfer_board(board.arr)

        display_group_details()
        input("Press Enter to continue...")

        while True:
            board.display_board()
            knight.display_possible_moves()

            move = input("\nMove Knight? (y/n): ").lower()
            if move == 'y':
                back.transfer_board(board.arr)
                knight.knight_movement()
            elif move == 'n':
                print("\nThanks for playing!")
                break

            reset_game = input("\nReset game? (y/n): ").lower()
            if reset_game == 'y':
                reset.traverse_to_board(board.arr)

            go_back = input("Go back once? (y/n): ").lower()
            if go_back == 'y':
                back.traverse_to_board(board.arr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


main()
