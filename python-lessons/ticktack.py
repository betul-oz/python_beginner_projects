def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Yatay ve dikey kontrol
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Çapraz kontrol
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Oyuncu {current_player}, satır seçin (0, 1, 2): "))
        col = int(input(f"Oyuncu {current_player}, sütun seçin (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Oyuncu {current_player} kazandı!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Oyun berabere bitti.")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Bu hücre zaten dolu. Lütfen başka bir hücre seçin.")

if __name__ == "__main__":
    tic_tac_toe()
