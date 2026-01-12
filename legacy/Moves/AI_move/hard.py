from Game_logic.checking import *
def make_ai_move_hard(board):
    best_move = None
    best_score = -float('inf')

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move