# Fermi-Pico-Bagel-Game
Fermi Pico Bagel is a Python logic game where players guess a secret 3-digit number with unique digits. Clues—fermi, pico, and bagels—guide each guess. It’s a fun way to sharpen deduction skills, with clean input validation, replayability, and future upgrade potential.
Overview
A Python implementation of the classic deduction game where players guess a secret 3-digit number with unique digits. After each guess, clues like fermi, pico, and bagels guide the player toward the correct answer. It’s fun, fast, and perfect for sharpening logic skills.

Gameplay Rules
- The secret number has 3 unique digits.
- After each guess:
- fermi   – correct digit in the correct position
- pico    – correct digit in the wrong position
- bagels  – digit not present at all
- Keep guessing until you crack the code!
- Replay option available after each round.

How to Run
Make sure you have Python 3 installed. No external libraries required.

Features
- Random number generation with unique digits
- Input validation (length, digit-only, no repeats)
- Clue-based feedback system
- Replayability and attempt tracking
- Clean, modular code structure

File Structure
game.py                 # Main game logic
README.md               # Project overview and instructions
LICENSE                 # Apache 2.0 license



Future Enhancements
- Emoji-based clue feedback
- Difficulty levels (e.g., 4-digit mode)
- GUI version using Tkinter or Flask
- Scoreboard or timer

Author
Arjun GD
M.Tech in Computer Science – Rajeev Institute of Technology, Hassan
Passionate about logic puzzles, clean code, and creative game design 

License
This project is licensed under the MIT See the LICENSE file for details.

Contributions
Pull requests, forks, and feedback are welcome! If you spot a bug or have an idea, feel free to open an issue or suggest an improvement.

Acknowledgments
Inspired by the original Bagels game from Invent Your Own Computer Games with Python by Al Sweigart. Reimagined with a clean structure and playful logic.


