# Cluedo Game - Project 2 Part 2

## What’s New in Part 2

| Feature | Description |
|---------|-------------|
| **Suggestion & Refutation** | When a player suggests a character + weapon + room, the other players are prompted in order to reveal a matching card (if any). Each suggestion, the refuter (if any), and the card shown are stored in the suggesting player’s **Notes**. |
| **Notes System** | Type **`notes`** instead of a room name to view the running log of your own suggestions, refutations, and every card you have seen so far. |
| **Accusation Mechanism** | At any time during a turn, a player can attempt a full accusation. If correct, the game ends and that player wins. If wrong, the accusing player is **eliminated** from further turns but must still answer refutation prompts. |
| **Elimination & Unsolved Crime** | The loop automatically skips eliminated players. If every player is eliminated (or exits) without a correct solution, the game ends and prints “Crime unsolved” with the hidden solution. |
| **Defensive Prompts** | All new inputs (accusation picks, refutation card choices, etc.) are fully validated and re‑prompted on bad input. |
| **Polished Prompts** | Accusation now prints once (`**** ACCUSE ****`), shows clean bullet lists, pauses two seconds for dramatic effect, and then declares the outcome. |

## How to Run (same as Part 1)

> **If you already ran Part 1, you only need to replace the source files.**  
> Steps for both the ZIP workflow and the Git clone workflow remain identical.

1. Ensure **Python 3.x** is installed.  
2. Either unzip **CarlosVanegas_Project2_SourceCode** *or* clone  
   `https://github.com/carlosv120/CS670-Project2_Part1`  
3. Open the folder in **Visual Studio Code**.  
4. Open a terminal.  
5. Run `python main.py` and follow the prompts.

---

# Cluedo Game - Project 2 Part 1

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
  - `CarlosVanegas_Readme.md`: Created to meet the instructions provided in the Project 2 Part 1 assignment.
  - `README.md`: Added so the README content appears on the main page of the GitHub repository.


## Requirements

- Python 3.x
- No external libraries are required.

## Author

Carlos Vanegas - Spring 2025 - CS670 Project 2 Part 1
