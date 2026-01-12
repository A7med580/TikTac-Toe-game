def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    scores = {"O": 1, "X": -1, "Tie": 0}

    if check_win(board, "O"):
        return scores["O"]
    if check_win(board, "X"):
        return scores["X"]
    if is_full(board):
        return scores["Tie"]

    if is_maximizing:
        best_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_eval = max(best_eval, eval)
        return best_eval
    else:
        best_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_eval = min(best_eval, eval)
        return best_eval
