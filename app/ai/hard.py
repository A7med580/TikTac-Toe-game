from app.logic.checking import minimax

def make_ai_move_hard(board):
    """Minimax-based move for Hard difficulty."""
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
