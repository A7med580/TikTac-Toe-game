import tkinter as tk
from Game_logic.checking import *
from Moves.AI_move.easy import *
from Moves.AI_move.hard import *
def player_move(row, col):
    if board[row][col] == " ":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED, bg="#90EE90")  # Light green color

        if check_win(board, "X"):
            highlight_winner("X")
            result_label.config(text="You win!", fg="#006400")  # Dark green color
            disable_buttons()
        elif is_full(board):
            result_label.config(text="It's a tie!", fg="#000080")  # Navy blue color
            disable_buttons()
        else:
            ai_move()

def ai_move():
    if ai_difficulty.get() == "Easy":
        move = make_ai_move_easy(board)
    else:
        move = make_ai_move_hard(board)

    if move:
        row, col = move
        board[row][col] = "O"
        buttons[row][col].config(text="O", state=tk.DISABLED, bg="#FF6347")  # Tomato color

        if check_win(board, "O"):
            highlight_winner("O")
            result_label.config(text="AI wins!", fg="#FF0000")  # Red color
            disable_buttons()
        elif is_full(board):
            result_label.config(text="It's a tie!", fg="#000080")  # Navy blue color
            disable_buttons()

def highlight_winner(player):
    for combination in win_combinations:
        for row, col in combination:
            buttons[row][col].config(bg="#FFFF00")  # Yellow color
        if player == "X":
            result_label.config(text="You win!", fg="#006400")  # Dark green color
        else:
            result_label.config(text="AI wins!", fg="#FF0000")  # Red color

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

def reset_game():
    global board, win_combinations
    board = [[" " for _ in range(3)] for _ in range(3)]
    win_combinations = []  # Updated to store winning combinations for highlighting
    result_label.config(text="", fg="black")  # Reset label color
    for row in buttons:
        for button in row:
            button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")  # Default system color

root = tk.Tk()
root.title("Tic-Tac-Toe Game")

board = [[" " for _ in range(3)] for _ in range(3)]
win_combinations = []  # To store winning combinations for highlighting
buttons = []

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="", width=8, height=3, command=lambda r=row, c=col: player_move(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=3, columnspan=3)

reset_button = tk.Button(root, text="Restart", command=reset_game)
reset_button.grid(row=4, columnspan=3)

ai_difficulty = tk.StringVar()
ai_difficulty.set("Easy")

easy_radio = tk.Radiobutton(root, text="Easy Mode (AI makes random moves)", variable=ai_difficulty, value="Easy")
easy_radio.grid(row=5, columnspan=3)

hard_radio = tk.Radiobutton(root, text="Hard Mode (AI uses minimax algorithm)", variable=ai_difficulty, value="Hard")
hard_radio.grid(row=6, columnspan=3)

root.mainloop()