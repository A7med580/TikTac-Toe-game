# RUNNING MANUAL

This guide explains how to run the Modern Tic-Tac-Toe Game step-by-step.

## 1. Prerequisites
You need **Python** installed on your computer.

## 2. Installation
Open your terminal (Terminal.app) and run the following command to install the required library (Flask):

```bash
pip install flask
```

## 3. Running the Game
To start the game, run this command in your terminal inside the project folder:

```bash
python run.py
```

You should see output like:
```
* Running on http://127.0.0.1:5001
```

## 4. Playing the Game
1.  Open your Web Browser (Chrome, Safari, etc.).
2.  Go to this address: **http://127.0.0.1:5001**
3.  The game will load.
4.  **Important**: To play **Hard Mode**:
    *   Select **Hard** from the dropdown menu.
    *   **Click the "New Game" button**. (You must click this to apply the change!)
    *   Start playing. The AI will now be unbeatable.

## Troubleshooting
-   **"Hard Mode isn't working"**: Make sure you clicked **"New Game"** after selecting Hard from the dropdown. The difficulty only updates when a new game starts.
-   **Port in use**: If it says "Address already in use", restart your computer or find the process using port 5001.
