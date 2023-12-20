Chess Game Variant with Pygame

Introduction
Welcome to the Chess Game Variant project. This Python application employs Pygame to create an interactive and visually engaging chess game, featuring an advanced AI opponent. The game is perfect for both beginners and experienced players who want to test their skills against a challenging computer opponent.

Features
Interactive GUI for a full chess experience.
Sophisticated AI opponent using minimax algorithm with alpha-beta pruning.
Enforcement of chess rules for legal moves.

Prerequisites
Ensure you have the following installed:

Python 3.x
Pygame library

Installation
To set up the game:

Clone the Repository:

Use git clone to clone the repository to your machine.
Install Dependencies:

It's recommended to use a virtual environment. Create and activate it, then install Pygame using pip install pygame.

Running the Game:

In the project directory, run python ChessVarPygame.py.

AI Opponent: Minimax with Alpha-Beta Pruning
The game features an AI opponent that uses the minimax algorithm with alpha-beta pruning for decision making. This algorithm is a popular choice in two-player games like chess where it simulates the possible moves and their outcomes to choose the best move.

Minimax Algorithm
Minimax is a backtracking algorithm used in decision-making and game theory. It provides an optimal move for the player assuming that the opponent is also playing optimally.
In chess, the minimax algorithm evaluates all possible moves, forecasts their outcomes, and selects the move that maximizes the player's chance of winning.
Alpha-Beta Pruning
Alpha-Beta Pruning is an optimization technique for the minimax algorithm. It significantly reduces the number of nodes that are evaluated in the decision tree.
This pruning method skips evaluating moves that won't be selected by minimax, thus speeding up the decision-making process.
By using these techniques, the AI opponent can quickly calculate the best moves, providing a challenging and engaging game of chess.

How to Play
After starting the game, make your moves on the GUI. The AI will respond with its move, calculated through the minimax algorithm with alpha-beta pruning.
