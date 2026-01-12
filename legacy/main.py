import tkinter as tk
from Game_logic.checking import check_win, is_full
from GUI.GUI import reset_game, disable_buttons
from Moves.AI_move.easy import make_ai_move_easy
from Moves.AI_move.hard import make_ai_move_hard

def main():
    # Initialize the main window
    root = tk.Tk()
    root.title("Tic-Tac-Toe Game")

    # Board setup
    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = []

    # Create buttons for the Tic-Tac-Toe grid
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(root, text="", width=8, height=3, )
            button.grid(row=row, column=col)
            button_row.append(button)
        buttons.append(button_row)

    # Label to display the result
    result_label = tk.Label(root, text="", font=("Helvetica", 16))
    result_label.grid(row=3, columnspan=3)

    # Restart button
    reset_button = tk.Button(root, text="Restart", command=lambda: reset_game(board, buttons, result_label))
    reset_button.grid(row=4, columnspan=3)

    # AI difficulty setting (Easy or Hard)
    ai_difficulty = tk.StringVar()
    ai_difficulty.set("Easy")

    easy_radio = tk.Radiobutton(root, text="Easy Mode (AI random moves)", variable=ai_difficulty, value="Easy")
    easy_radio.grid(row=5, columnspan=3)

    hard_radio = tk.Radiobutton(root, text="Hard Mode (AI minimax algorithm)", variable=ai_difficulty, value="Hard")
    hard_radio.grid(row=6, columnspan=3)

    # Start the Tkinter main loop
    root.mainloop()

def ai_move(board, buttons, result_label, ai_difficulty):
    # AI chooses the difficulty level
    if ai_difficulty.get() == "Easy":
        move = make_ai_move_easy(board)
    else:
        move = make_ai_move_hard(board)

    if move:
        row, col = move
        board[row][col] = "O"
        buttons[row][col].config(text="O", state=tk.DISABLED, bg="#FF6347")  # Tomato color for AI move

        if check_win(board, "O"):
            result_label.config(text="AI wins!", fg="#FF0000")  # Red color for AI win
            disable_buttons(buttons)
        elif is_full(board):
            result_label.config(text="It's a tie!", fg="#000080")  # Navy blue for tie
            disable_buttons(buttons)

if __name__ == "__main__":
    main()