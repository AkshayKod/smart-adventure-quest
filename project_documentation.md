# 1. Project Title
**SMART ADVENTURE QUEST – Advanced Text-Based Adventure Game**

---

# 2. Abstract
The "Smart Adventure Quest" is an interactive, text-based adventure game built entirely in Python. Designed to demonstrate strong foundational programming logic, this project encapsulates key computer science concepts such as condition handling, iterative loops, modular functions, list and dictionary manipulations, and file handling. The game immerses players in the Kingdom of Eldoria where they must conquer sequential challenges—ranging from mathematical guessing to technical quizzes and RPG-style battles—ultimately striving to unlock the secret ending through wise decision-making and optimal gameplay.

---

# 3. Problem Statement
Many beginner to intermediate computer science students struggle with applying theoretical programming concepts (like File I/O, Error Handling, and Data Structures) to real-world or engaging applications. This project serves as a comprehensive solution, providing a fun and interactive way to showcase technical skills suitable for college mini-projects, internship assessments, and placement portfolios, while maintaining clean and modular code standards.

---

# 4. Objectives
- To develop an interactive, menu-driven command-line game using Python.
- To implement dynamic gameplay logic utilizing conditional statements and loops.
- To demonstrate proficiency in core Python structures (Lists, Dictionaries).
- To utilize Exception Handling for robust input validation.
- To apply File Handling for persistent storage of player High Scores.
- To provide a fully functional, well-documented portfolio piece demonstrating industry-standard PEP-8 coding practices.

---

# 5. Features
- **Dynamic Difficulty Modes:** Easy, Medium, and Hard scaling that affects gameplay logic, monster strengths, and damage calculations.
- **Player Progression System:** Tracks player stats including Health, Score, Level, and Inventory items.
- **Diverse Challenges (Levels):**
  - *Level 1:* Random Number Guessing (Logical deductions).
  - *Level 2:* Technology & Programming Quiz (Knowledge testing).
  - *Level 3:* Turn-based Monster Battle (RPG-style risk management).
  - *Level 4:* Randomized Treasure Hunt (Luck & exploration).
- **Persistent High Score:** Uses file operations (`highscore.txt`) to save and retrieve the highest score achieved.
- **Robust Exception Handling:** Implements `try-except` blocks preventing game crashes from invalid inputs.
- **Achievement System:** Unlocks badges and a Secret Ending for exceptional gameplay.

---

# 6. Technologies Used
- **Programming Language:** Python 3.x
- **Standard Libraries:** `random`, `os`, `time`
- **Environment:** Any standard Python IDE or Terminal/Command Prompt.

---

# 7. System Architecture
The application follows a modular Monolithic console architecture relying on a central state machine.
1. **Main Menu Loop:** The game root directing player flow.
2. **Game State Manager (`GameState` Class):** Object managing player health, inventory, score, and rank globally for the session.
3. **Level Modules:** Dedicated functions for each level interacting with the Game State.
4. **Data Persistence Module:** Reads and writes to `highscore.txt` for enduring statistics.

---

# 8. Algorithm
1. **Start**
2. Display Main Menu.
3. If Player chooses to View Rules, High Score, or Achievements, display relevant data and return to Menu.
4. If Player chooses Start Game:
   1. Initialize `GameState` object.
   2. Input player name and validate.
   3. Choose difficulty and set game configuration limits (Range, Attempts, Damage multipliers).
5. **Level 1 (Number Guessing):** Loop until attempts run out or correct number guessed. Adjust state (Health/Score).
6. **Level 2 (Quiz):** Ask 5 random dictionary-driven questions. Validate answers, adjust state.
7. **Level 3 (Monster Battle):** Loop battle sequence until Monster defeated, Player defeated, or max rounds reached. Process attacks, spell checks, and defenses. Adjust state.
8. **Level 4 (Treasure Hunt):** Prompt for path selection. Determine randomized outcome.
9. **Game Over / Summary:**
   1. Display final Score, Health, Inventory, Achievements.
   2. Determine Player Rank based on Score.
   3. Check Secret Ending criteria (Score > 500 + Full Inventory).
   4. Compare score with File IO. If greater, overwrite `highscore.txt`.
10. Return to Main Menu.
11. **Exit Game -> End**

---

# 9. Flowchart (Text Format)

```text
[ START ]
   |
   V
[ MAIN MENU ] <-----------------------------------------+
   |-- 2. Rules --> [ Display Rules ] ------------------|
   |-- 3. Highscore --> [ File Read ] ------------------|
   |-- 4. Achievements --> [ Display Achv ] ------------|
   |-- 5. Exit --> [ END ]
   |
   |-- 1. Start Game
         |
         V
[ PLAYER SETUP ] (Name, Difficulty)
         |
         V
[ LEVEL 1: NUMBER GUESS ] --> Pass/Fail -> Update Stats
         |
         V
[ LEVEL 2: TECH QUIZ ] -----> Pass/Fail -> Update Stats
         |
         V
[ LEVEL 3: BATTLE ] --------> Pass/Fail -> Update Stats
         |
         V
[ LEVEL 4: TREASURE ] ------> Pass/Fail -> Update Stats
         |
         V
[ GAME SUMMARY ]
   |-- Calculate Rank
   |-- Check Secret Ending
   |-- Update Highscore File
   |
   +----------------------------------------------------+
```

---

# 10. Source Code Explanation
- **`GameState` Class:** Acts as a centralized data structure. Contains methods to `take_damage`, `add_score`, and `set_difficulty` to keep global logic grouped.
- **`get_valid_input()`:** A highly reusable helper function implementing a `while True` loop and `try-except` block to ensure valid user integer selections.
- **`load_high_score()` / `save_high_score()`:** Utilizes the `with open(...)` paradigm in Python for safe file handling without leaking file descriptors.
- **`level1_number_guessing()`:** Utilizes the `random.randint` method paired with a `for` loop dictated by the player's difficulty setting.
- **`level2_quiz()`:** Employs a List of Dictionaries. Utilizes `random.sample()` to pull unique questions every playthrough.
- **`level3_monster_battle()`:** Uses a turn-based `while` (or bounded `for`) loop. Introduces conditional checks on the Inventory (checking for the `Magic Scroll`).
- **`game_summary()`:** Evaluates final logic, assigns ranks using `if/elif` ladders, and leverages sets (`issubset`) to check if all secret items were collected.

---

# 11. Sample Output

```text
========================================
         SMART ADVENTURE QUEST          
========================================
1. Start New Game
2. View Rules
3. View High Score
4. View Achievements
5. Exit
Enter your choice: 1

========================================
              PLAYER SETUP              
========================================
Enter your Player Name: Alex

Select Difficulty:
1. Easy
2. Medium
3. Hard
Choice (1-3): 1

Welcome to Eldoria, Alex! Let the quest begin...

==============================
         PLAYER STATS         
==============================
Name: Alex
Health: 100
Score: 0
Level: 1
Inventory: Empty
==============================

========================================
  LEVEL 1 - NUMBER GUESSING CHALLENGE   
========================================
An ancient wizard has locked the door with a magic number.
Guess the number between 1 and 20. You have 5 attempts.
Attempt 1/5 - Enter your guess: 10
Too High!
Attempt 2/5 - Enter your guess: 5
Correct Guess! The magic door unlocks.

[+] Score increased by 50. Current Score: 50
[+] Added to inventory: Ancient Key

*** ACHIEVEMENT UNLOCKED: Puzzle Solver ***
```

---

# 12. Test Cases

| Test Case ID | Description | Input | Expected Output | Pass/Fail |
|--------------|-------------|-------|-----------------|-----------|
| TC-01 | Main Menu Invalid Input | 'A', '9' | "Invalid input format/choice." loops back. | Pass |
| TC-02 | Name Entry | "John" | Accepts name and proceeds. | Pass |
| TC-03 | Level 1: Out of Bounds | '25' on Easy | Accepts input but logic responds "Too High!" | Pass |
| TC-04 | Level 2: Wrong Answer | Answer 1 for Q3 | Checks answer, subtracts health/score. | Pass |
| TC-05 | Level 3: Magic without Scroll | Choice 2 | Displays "You try to cast a spell, but you don't have a Magic Scroll! It fails." | Pass |
| TC-06 | File Handle: No File | View Highscore | "No high score recorded yet." | Pass |
| TC-07 | End Game: Rank assignment | Score 350 | Prints "Rank: Hero" in Summary. | Pass |

---

# 13. Future Enhancements
- **Graphical User Interface (GUI):** Transitioning the text-based application to a visual application using Tkinter or Pygame.
- **Database Integration:** Replacing the flat-file `highscore.txt` with SQLite to maintain a leaderboard of multiple top players.
- **Save State:** Allow players to save mid-game and resume later.
- **Expanded Levels:** Adding more branching paths and interactive riddles.

---

# 14. Conclusion
The Smart Adventure Quest project successfully fulfills all initial requirements, proving to be a highly effective portfolio piece. It encapsulates core programming methodologies—ranging from fundamental constructs to advanced handling and data structures—creating an entertaining and seamlessly operating application without abrupt crashes.

---

# 15. Viva Questions & Answers

**Q1: Why did you use Exception Handling (`try-except`) in this project?**
**A1:** Exception handling was used specifically in the `get_valid_input` function to handle `ValueError`s. If a user inputs a string when an integer is expected, the program catches the exception and prompts the user again instead of crashing abruptly.

**Q2: How is the High Score persisted between different game sessions?**
**A2:** It uses File Handling. The `save_high_score` function opens `highscore.txt` in write mode (`'w'`) and saves the name and score. The `load_high_score` function opens it in read mode (`'r'`) to retrieve the data.

**Q3: Explain the use of Dictionaries in your project.**
**A3:** Dictionaries are used in Level 2 (The Quiz). Each question is a dictionary containing keys for the question text (`'q'`), the options list (`'options'`), and the correct answer index (`'ans'`). This makes the data structured and easy to read.

**Q4: What is the purpose of the `GameState` class?**
**A4:** The `GameState` class employs Object-Oriented Programming (OOP) principles to bundle all player-related variables (health, score, inventory, difficulty limits) into a single object. This avoids the messy use of global variables and makes it easy to reset the game by simply instantiating a new `GameState` object.

**Q5: How does the random module contribute to the game?**
**A5:** The `random` module is heavily used to ensure replayability. It randomizes the target number in Level 1, shuffles the questions in Level 2 (`random.sample`), selects the enemy and calculates variable damage in Level 3, and randomizes the treasure path in Level 4.
