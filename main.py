# main.py

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):  # row
            return True
        if all(board[j][i] == player for j in range(3)):  # column
            return True
    if all(board[i][i] == player for i in range(3)):  # main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # anti diagonal
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column, e.g., 1 2): ")
            row, col = map(int, move.strip().split())
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Invalid input. Use numbers from 1 to 3.")
        except:
            print("Invalid format. Please enter two numbers separated by space.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!\n")
    print_board(board)
    
    while True:
        row, col = get_move(current_player)

        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
