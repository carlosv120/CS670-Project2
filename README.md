# Cluedo Game - Project 2 Part 1

## Introduction

 - This project is a simplified version of the Cluedo (Clue) game.  
 - It was created for CS670 - Artificial Intelligence - Spring 2025.  
 - The game allows multiple players to move through a mansion and make suggestions to simulate solving the mystery.

## How to Run the Game (Option 1)

1. Make sure you have **Python 3** installed on your computer.
2. Download and unzip the folder **CarlosVanegas_Project2_SourceCode**.
3. Open **Visual Studio Code**.
4. Open the folder **CarlosVanegas_Project2_SourceCode** in Visual Studio Code.
5. Open a new terminal inside Visual Studio Code.
6. Run the following command inside the bash terminal:```python main.py```
7. Follow the on-screen instructions to start playing the game.

## How to Run the Game (Option 2)

1. Make sure you have **Python 3** installed on your computer.
2. Clone the repository from GitHub: [https://github.com/carlosv120/CS670-Project2_Part1](https://github.com/carlosv120/CS670-Project2_Part1)
3. Open **Visual Studio Code**.
4. Open the folder **CarlosVanegas_Project2_SourceCode** inside Visual Studio Code.
5. Open a new terminal inside Visual Studio Code.
6. Run the following command inside the bash terminal:```python main.py```
7. Follow the on-screen instructions to start playing the game.

## Project Structure

- `main.py`: Main file of the game. Includes player turns, and game prompts.
- `mansion.py`: Contains the list of rooms inside the mansion.
- `characters.py`: Contains the list of characters.
- `weapons.py`: Contains the list of weapons.
- `player_actions.py`: Handles player movement, suggestions, and input validation.
- `solution_selector.py`: Randomly selects the character, weapon, and room forming the hidden murder solution.

## Game Features

- Random selection of the murder solution (character, weapon, and room).
- Support for **2 to 6 players** with input validation.
- Turn-based system where players:
  - Move between rooms.
  - Make suggestions based on their current location.
- Defensive programming to validate all user inputs.
- For testing purposes, the solution is printed at the start of the game.
- Players are prompted before each turn to confirm if the player is ready.

## Notes

- The game does not currently support accusations or win/lose conditions.  
  These features are planned for Project 2 Part 2.
- Exiting the game is done manually by choosing 'exit' during a move prompt.
- Only basic console output is used. No graphical user interface is included in Part 1.
- The project includes two versions of the README file:
  - `CarlosVanegas_Readme.md`: Created to meet the specific instructions provided in the Project 2 Part 1 assignment.
  - `README.md`: Standard GitHub convention to ensure the README is properly displayed on the main page of the repository.


## Requirements

- Python 3.x
- No external libraries are required.

## Author

Carlos Vanegas - Spring 2025 - CS670 Project 2 Part 1
