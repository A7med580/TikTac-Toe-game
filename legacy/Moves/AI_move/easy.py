import random
def make_ai_move_easy(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    return None
