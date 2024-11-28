# Guess Number Game

## Description

This project is a Python program where the user guesses a randomly drawn number within a given range. The program ensures user inputs are valid and provides feedback for every guess, guiding the user until they correctly guess the number.

## How It Works

1. **Define Range**:
    - The user provides a minimum and maximum value for the range.
    - The program ensures the input values are valid:
        - Both values must be integers.
        - The maximum must be greater than the minimum.
        - The minimum and maximum values cannot be equal.
2. **Draw Number**:
    - The program randomly selects a number within the given range.
3. **Guessing Game**:
    - The user attempts to guess the drawn number.
    - After each guess, the program provides feedback:
        - *"Too high"* if the guess is higher than the drawn number.
        - *"Too low"* if the guess is lower than the drawn number.
    - The game continues until the correct number is guessed.
4. **Game Over**:
    - Once the correct number is guessed, the program displays the total number of guesses and ends the game.

## Example Usage

```plaintext
Enter min range:
10
Enter max range:
20
Guess number from range: 10 to 20. Good Luck!
Enter valid number:
15
Too high
Enter valid number:
12
Too low
Enter valid number:
13
You won! Your numbers of guesses: 3
Game Over
```

## Requirements

- **Python 3.8 or higher.**

## How to Run

1. Clone the repository.
2. Run the script using the following command:
    ```bash
    python guess_number_game.py
    ```
3. Follow the prompts in the terminal to play the game.



## Notes

- Ensure the range is valid before proceeding with the game.
- Invalid inputs will prompt the user to try again.
- Enjoy the challenge of guessing the number! 😊