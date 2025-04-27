# Cluedo Game - Project 2 Part 1

## How to Run the Game

1. Install Python 3 on your computer if it is not already installed.
2. Download and unzip the folder **CarlosVanegas_Project2_SourceCode**.
3. Open **Visual Studio Code**.
4. Open the folder **CarlosVanegas_Project2_SourceCode** in Visual Studio Code.
5. Open a new terminal inside Visual Studio Code.
6. In the terminal, run the following command: python main.py
7. Follow the prompts to start the game.

## Folder Structure

- `main.py`: Main program that controls the overall game flow.
- `mansion.py`: Defines the list of rooms available in the mansion.
- `characters.py`: Defines the list of playable characters.
- `weapons.py`: Defines the list of available weapons.
- `player_actions.py`: Handles player movement, suggestions, and validation.
- `solution_selector.py`: Randomly selects the character, weapon, and room for the murder solution.

## Game Overview

- The game randomly selects one character, one weapon, and one room as the hidden solution.
- Players take turns moving between rooms and making suggestions about the solution.
- Input validation is used to avoid invalid moves or suggestions.
- For testing purposes, the solution is printed at the beginning of the game.
- The game continues until players exit manually.
