import random
import os
import time

# Global Constants
HIGHSCORE_FILE = "highscore.txt"

class GameState:
    """Class to hold and manage all game state variables."""
    def __init__(self):
        self.player_name = ""
        self.difficulty = 1
        self.health = 100
        self.score = 0
        self.level = 1
        self.inventory = []
        self.achievements = []
        self.max_attempts = 5
        self.guess_range = 20
        self.monster_strength = "Weak"

    def set_difficulty(self, choice):
        self.difficulty = choice
        if choice == 1:
            self.guess_range = 20
            self.max_attempts = 5
            self.monster_strength = "Weak"
        elif choice == 2:
            self.guess_range = 50
            self.max_attempts = 4
            self.monster_strength = "Medium"
        elif choice == 3:
            self.guess_range = 100
            self.max_attempts = 3
            self.monster_strength = "Strong"

    def add_achievement(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)
            print(f"\n*** ACHIEVEMENT UNLOCKED: {achievement} ***\n")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"\n[+] Added to inventory: {item}\n")

    def take_damage(self, amount):
        self.health -= amount
        print(f"\n[-] You took {amount} damage. Current Health: {self.health}\n")

    def add_score(self, amount):
        self.score += amount
        print(f"\n[+] Score increased by {amount}. Current Score: {self.score}\n")

    def deduct_score(self, amount):
        self.score = max(0, self.score - amount)
        print(f"\n[-] Score decreased by {amount}. Current Score: {self.score}\n")

    def show_stats(self):
        print("\n" + "=" * 30)
        print("PLAYER STATS".center(30))
        print("=" * 30)
        print(f"Name: {self.player_name}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Level: {self.level}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("=" * 30 + "\n")


# --- HELPER FUNCTIONS ---

def get_valid_input(prompt, valid_options=None, input_type=int):
    """Handles input validation and exception handling for user inputs."""
    while True:
        try:
            value = input_type(input(prompt))
            if valid_options and value not in valid_options:
                print(f"Invalid choice. Please enter one of {valid_options}.")
                continue
            return value
        except ValueError:
            print("Invalid input format. Please enter a valid number.")

def load_high_score():
    """Reads high score from the file."""
    try:
        if os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, 'r') as file:
                data = file.readline().strip().split(',')
                if len(data) == 2:
                    return data[0], int(data[1])
    except Exception as e:
        print(f"Error loading high score: {e}")
    return "None", 0

def save_high_score(name, score):
    """Writes the new high score to the file."""
    try:
        with open(HIGHSCORE_FILE, 'w') as file:
            file.write(f"{name},{score}")
    except Exception as e:
        print(f"Error saving high score: {e}")


# --- MENU FUNCTIONS ---

def view_rules():
    print("\n" + "=" * 40)
    print("RULES OF SMART ADVENTURE QUEST".center(40))
    print("=" * 40)
    print("1. Complete challenges to earn score and items.")
    print("2. Your health starts at 100. It decreases if you fail.")
    print("3. If health reaches 0, the game is over.")
    print("4. Your decisions affect the final outcome.")
    print("5. Try to unlock all achievements and get a high score!")
    input("\nPress Enter to return to main menu...")

def view_high_score():
    name, score = load_high_score()
    print("\n" + "=" * 40)
    print("HIGH SCORE".center(40))
    print("=" * 40)
    if name != "None":
        print(f"Player: {name}")
        print(f"Highest Score: {score}")
    else:
        print("No high score recorded yet.")
    input("\nPress Enter to return to main menu...")
    
def view_achievements():
    print("\n" + "=" * 40)
    print("POSSIBLE ACHIEVEMENTS".center(40))
    print("=" * 40)
    print("- Puzzle Solver (Win Number Guessing)")
    print("- Quiz Master (Perfect score in Quiz)")
    print("- Monster Slayer (Defeat the Monster)")
    print("- Treasure Hunter (Find the correct path)")
    print("- Legend of Eldoria (Secret Ending unlocked)")
    input("\nPress Enter to return to main menu...")


# --- GAME LEVELS ---

def level1_number_guessing(game):
    print("\n" + "=" * 40)
    print("LEVEL 1 - NUMBER GUESSING CHALLENGE".center(40))
    print("=" * 40)
    print("An ancient wizard has locked the door with a magic number.")
    
    target = random.randint(1, game.guess_range)
    attempts = game.max_attempts
    
    print(f"Guess the number between 1 and {game.guess_range}. You have {attempts} attempts.")
    
    for i in range(attempts):
        guess = get_valid_input(f"Attempt {i+1}/{attempts} - Enter your guess: ")
        
        if guess == target:
            print("Correct Guess! The magic door unlocks.")
            game.add_score(50)
            game.add_item("Ancient Key")
            game.add_achievement("Puzzle Solver")
            game.level += 1
            return True
        elif guess < target:
            print("Too Low!")
        else:
            print("Too High!")
            
    print(f"\nOut of attempts! The correct number was {target}.")
    print("The wizard punishes you for failing.")
    game.take_damage(10)
    game.level += 1
    return True

def level2_quiz(game):
    print("\n" + "=" * 40)
    print("LEVEL 2 - QUIZ CHALLENGE".center(40))
    print("=" * 40)
    print("A sphinx blocks your path. Answer its questions to proceed.")
    
    # 10 Tech MCQ Questions
    questions = [
        {"q": "Which language is most commonly used in AI?", "options": ["HTML", "CSS", "Python", "XML"], "ans": 3},
        {"q": "What data structure uses LIFO (Last In First Out)?", "options": ["Queue", "Stack", "Array", "Tree"], "ans": 2},
        {"q": "Which of the following is not an operating system?", "options": ["Windows", "Linux", "Oracle", "macOS"], "ans": 3},
        {"q": "Who is known as the father of computers?", "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"], "ans": 2},
        {"q": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "ans": 3},
        {"q": "What does CPU stand for?", "options": ["Central Process Unit", "Computer Personal Unit", "Central Processing Unit", "Central Processor Unit"], "ans": 3},
        {"q": "Which protocol is used for secure communication over the internet?", "options": ["HTTP", "FTP", "HTTPS", "SMTP"], "ans": 3},
        {"q": "What does SQL stand for?", "options": ["Structured Query Language", "Strong Question Language", "Structured Question Language", "Simple Query Language"], "ans": 1},
        {"q": "Which of these is a front-end web framework?", "options": ["Django", "React", "Flask", "Node.js"], "ans": 2},
        {"q": "What is the time complexity of binary search?", "options": ["O(n)", "O(n^2)", "O(log n)", "O(1)"], "ans": 3}
    ]
    
    selected_qs = random.sample(questions, 5)
    score_this_level = 0
    
    for i, q in enumerate(selected_qs):
        print(f"\nQuestion {i+1}: {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"{j+1}. {opt}")
            
        ans = get_valid_input("Your choice (1-4): ", [1, 2, 3, 4])
        if ans == q['ans']:
            print("Correct!")
            game.add_score(20)
            score_this_level += 20
        else:
            print(f"Wrong! The correct answer was {q['ans']}.")
            game.deduct_score(5)
            game.take_damage(5)
            if game.health <= 0:
                return False
                
    if score_this_level == 100:
        game.add_achievement("Quiz Master")
    
    print("\nYou found a Magic Scroll among the sphinx's belongings.")
    game.add_item("Magic Scroll")
    game.level += 1
    return True

def level3_monster_battle(game):
    print("\n" + "=" * 40)
    print("LEVEL 3 - MONSTER BATTLE".center(40))
    print("=" * 40)
    
    monsters = ["Goblin", "Skeleton", "Dragon"]
    monster = random.choice(monsters)
    print(f"A wild {monster} appears! ({game.monster_strength} strength)")
    
    monster_health = 50 if game.difficulty == 1 else (75 if game.difficulty == 2 else 100)
    max_rounds = 4
    
    for round_num in range(1, max_rounds + 1):
        if monster_health <= 0 or game.health <= 0:
            break
            
        print(f"\n--- Round {round_num}/{max_rounds} ---")
        print(f"Monster Health: {monster_health} | Your Health: {game.health}")
        print("Choose your action:")
        print("1. Sword Attack")
        print("2. Magic Spell")
        print("3. Shield Defense")
        
        action = get_valid_input("Action (1-3): ", [1, 2, 3])
        monster_action = random.choice(["attack", "defend"])
        
        # Player Turn
        if action == 1:
            damage = random.randint(15, 25)
            if monster_action == "defend":
                damage //= 2
                print(f"The {monster} defended! Reduced damage.")
            monster_health -= damage
            print(f"You struck with a sword for {damage} damage!")
        elif action == 2:
            if "Magic Scroll" in game.inventory:
                damage = random.randint(30, 50)
                monster_health -= damage
                print(f"You cast a magic spell for {damage} damage!")
            else:
                print("You try to cast a spell, but you don't have a Magic Scroll! It fails.")
        elif action == 3:
            print("You raise your shield, bracing for impact!")
            
        if monster_health <= 0:
            break
            
        # Monster Turn
        if monster_action == "attack":
            # Damage scales with difficulty
            monster_dmg = random.randint(10, 20) * game.difficulty
            if action == 3: # Player defended
                monster_dmg //= 2
                print("Your shield blocked half the damage!")
            print(f"The {monster} attacks you for {monster_dmg} damage!")
            game.take_damage(monster_dmg)
        else:
            print(f"The {monster} holds its ground.")
            
    if game.health <= 0:
        return False
        
    if monster_health <= 0:
        print(f"\nVictory! You defeated the {monster}!")
        game.add_score(100)
        game.add_achievement("Monster Slayer")
        game.add_item("Sword")
    else:
        print(f"\nDefeat! You failed to kill the {monster} in time and must flee.")
        print("You lost 20 Health during the escape.")
        game.take_damage(20)
        
    game.level += 1
    return True

def level4_treasure_hunt(game):
    print("\n" + "=" * 40)
    print("LEVEL 4 - TREASURE HUNT".center(40))
    print("=" * 40)
    
    print("You reach a crossroads with three mysterious paths:")
    print("1. Left Cave")
    print("2. Dark Forest")
    print("3. Ancient Temple")
    
    choice = get_valid_input("Choose your path (1-3): ", [1, 2, 3])
    treasure_path = random.randint(1, 3)
    
    if choice == treasure_path:
        print("\nYou chose correctly! You discovered the hidden treasure!")
        game.add_score(150)
        game.add_item("Treasure Chest")
        game.add_achievement("Treasure Hunter")
    else:
        print("\nWrong path! You triggered an ancient trap.")
        game.take_damage(15)
        
    game.level += 1
    return True

def game_summary(game):
    """Displays the final game summary and handles high scores."""
    print("\n" + "=" * 40)
    print("GAME SUMMARY".center(40))
    print("=" * 40)
    
    print(f"Player Name: {game.player_name}")
    diff_map = {1: "Easy", 2: "Medium", 3: "Hard"}
    print(f"Difficulty: {diff_map[game.difficulty]}")
    print(f"Final Score: {game.score}")
    print(f"Health Remaining: {game.health}")
    print(f"Levels Completed: {game.level - 1}")
    print(f"Items Collected: {', '.join(game.inventory) if game.inventory else 'None'}")
    print(f"Achievements: {', '.join(game.achievements) if game.achievements else 'None'}")
    
    # Calculate Rank
    rank = "Beginner"
    if game.score >= 501: rank = "Legend"
    elif game.score >= 301: rank = "Hero"
    elif game.score >= 201: rank = "Warrior"
    elif game.score >= 101: rank = "Explorer"
    else: rank = "Beginner"
    print(f"Rank: {rank}")
    
    # Secret Ending Check
    required_items = {"Ancient Key", "Magic Scroll", "Sword", "Treasure Chest"}
    if game.score > 500 and required_items.issubset(set(game.inventory)):
        print("\n*** SECRET ENDING UNLOCKED ***")
        print("Congratulations! You have become the Legendary Guardian of Eldoria")
        print("and discovered the hidden treasure of the Ancient Kingdom.")
        game.add_achievement("Legend of Eldoria")
        
    # High Score Update
    old_name, old_score = load_high_score()
    if game.score > old_score:
        print("\nNEW HIGH SCORE ACHIEVED!")
        save_high_score(game.player_name, game.score)
        
    print("=" * 40 + "\n")


# --- MAIN ENTRY POINT ---

def start_new_game():
    game = GameState()
    
    print("\n" + "=" * 40)
    print("PLAYER SETUP".center(40))
    print("=" * 40)
    
    while True:
        name = input("Enter your Player Name: ").strip()
        if name:
            game.player_name = name
            break
        print("Name cannot be empty.")
        
    print("\nSelect Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    diff = get_valid_input("Choice (1-3): ", [1, 2, 3])
    game.set_difficulty(diff)
    
    print(f"\nWelcome to Eldoria, {game.player_name}! Let the quest begin...")
    time.sleep(1)
    
    # Sequence of levels
    levels = [level1_number_guessing, level2_quiz, level3_monster_battle, level4_treasure_hunt]
    
    for level in levels:
        if game.health <= 0:
            break
            
        game.show_stats()
        success = level(game)
        
        if game.health <= 0:
            print("\n" + "=" * 40)
            print("GAME OVER".center(40))
            print("You have lost all your health.")
            print("=" * 40)
            break
        
        time.sleep(1)
        
    game_summary(game)
    input("Press Enter to return to main menu...")

def main():
    while True:
        print("\n" + "=" * 40)
        print("SMART ADVENTURE QUEST".center(40))
        print("=" * 40)
        print("1. Start New Game")
        print("2. View Rules")
        print("3. View High Score")
        print("4. View Achievements")
        print("5. Exit")
        
        choice = get_valid_input("Enter your choice: ", [1, 2, 3, 4, 5])
        
        if choice == 1:
            start_new_game()
        elif choice == 2:
            view_rules()
        elif choice == 3:
            view_high_score()
        elif choice == 4:
            view_achievements()
        elif choice == 5:
            print("Thank you for playing SMART ADVENTURE QUEST!")
            break

if __name__ == "__main__":
    main()
