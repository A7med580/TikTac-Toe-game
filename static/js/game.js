document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('board');
    const cells = document.querySelectorAll('.cell');
    const statusMsg = document.getElementById('status-message');
    const resetBtn = document.getElementById('reset-btn');
    const difficultySelect = document.getElementById('difficulty');

    let gameActive = true;

    // Initialize/Reset
    resetBtn.addEventListener('click', startNewGame);

    function startNewGame() {
        const difficulty = difficultySelect.value;
        statusMsg.textContent = "New Game Started!";
        gameActive = true;
        
        // Reset UI
        cells.forEach(cell => {
            cell.textContent = "";
            cell.classList.remove('x', 'o', 'taken');
            cell.style.pointerEvents = 'auto'; // Re-enable clicks
        });

        // Call backend reset
        fetch('/reset', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ difficulty })
        })
        .then(res => res.json())
        .then(data => {
            console.log("Game Reset", data);
        });
    }

    // Handle Cell Clicks
    cells.forEach(cell => {
        cell.addEventListener('click', (e) => {
            if (!gameActive || cell.classList.contains('taken')) return;

            const row = cell.dataset.row;
            const col = cell.dataset.col;

            // Optimistic UI Update (Player Move)
            cell.textContent = "X";
            cell.classList.add('x', 'taken');
            
            // Allow only one move at a time
            board.style.pointerEvents = 'none';

            sendMove(row, col);
        });
    });

    function sendMove(row, col) {
        fetch('/move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ row: parseInt(row), col: parseInt(col) })
        })
        .then(res => res.json())
        .then(data => {
            updateBoard(data.state);
            board.style.pointerEvents = 'auto'; // Re-enable board
        })
        .catch(err => {
            console.error(err);
            board.style.pointerEvents = 'auto';
        });
    }

    function updateBoard(state) {
        // Sync board state
        const boardData = state.board;
        cells.forEach(cell => {
            const r = cell.dataset.row;
            const c = cell.dataset.col;
            const val = boardData[r][c];

            if (val !== " " && cell.textContent !== val) {
                cell.textContent = val;
                cell.classList.add(val.toLowerCase(), 'taken');
            }
        });

        if (state.game_over) {
            gameActive = false;
            statusMsg.textContent = state.winner === 'Tie' ? "It's a Tie!" : `${state.winner} Wins!`;
            statusMsg.style.color = state.winner.includes('You') ? '#10b981' : (state.winner === 'Tie' ? '#e2e8f0' : '#ef4444');
        } else {
             statusMsg.textContent = "";
        }
    }
});
