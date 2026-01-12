from flask import Blueprint, render_template, jsonify, request
from app.logic.checking import check_win, is_full
from app.ai.easy import make_ai_move_easy
from app.ai.hard import make_ai_move_hard

main = Blueprint('main', __name__)

# Game State
# In a real multi-user app, this should be in a database or session.
# For this local demo, we'll keep it simple with a global variable.
game_state = {
    "board": [[" " for _ in range(3)] for _ in range(3)],
    "difficulty": "Easy",
    "winner": None,
    "game_over": False
}

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/reset', methods=['POST'])
def reset():
    global game_state
    game_state = {
        "board": [[" " for _ in range(3)] for _ in range(3)],
        "difficulty": request.json.get('difficulty', 'Easy'),
        "winner": None,
        "game_over": False
    }
    return jsonify({"message": "Game reset", "state": game_state})

@main.route('/move', methods=['POST'])
def move():
    global game_state
    if game_state['game_over']:
        return jsonify({"message": "Game over", "state": game_state})

    data = request.json
    row = data.get('row')
    col = data.get('col')

    # Player Move
    if game_state['board'][row][col] == " ":
        game_state['board'][row][col] = "X"
    else:
        return jsonify({"message": "Invalid move", "state": game_state}), 400

    # Check Player Win
    if check_win(game_state['board'], "X"):
        game_state['winner'] = "You (X)"
        game_state['game_over'] = True
        return jsonify({"message": "Player wins", "state": game_state})
    
    # Check Tie
    if is_full(game_state['board']):
        game_state['winner'] = "Tie"
        game_state['game_over'] = True
        return jsonify({"message": "Tie", "state": game_state})

    # AI Move
    difficulty = game_state['difficulty']
    ai_move = None
    if difficulty == "Easy":
        ai_move = make_ai_move_easy(game_state['board'])
    else:
        ai_move = make_ai_move_hard(game_state['board'])

    if ai_move:
        ai_row, ai_col = ai_move
        game_state['board'][ai_row][ai_col] = "O"

        # Check AI Win
        if check_win(game_state['board'], "O"):
            game_state['winner'] = "AI (O)"
            game_state['game_over'] = True
        elif is_full(game_state['board']):
             game_state['winner'] = "Tie"
             game_state['game_over'] = True

    return jsonify({"message": "Move processed", "state": game_state})
