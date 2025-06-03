def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'

    print("=== Tic-Tac-Toe ===")
    print("Player 1: X, Player 2: O")
    print_board(board)

    while True:
        move = input(f"Player {current_player}, choose a cell (1-9): ")
        
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please choose a number from 1 to 9.")
            continue

        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("Cell already taken. Try again.")
            continue

        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
