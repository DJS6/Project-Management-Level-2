from random import randint
# Common Functions.


def check_str_input(question: str, choices: list):
    """Asks user a question, then checks user's input against a list of
       possible choices and ensures it's in it"""
    # Repeats until value returned.
    while True:
        # Asks question and saves answer.
        user_input = str(input(question))
        # Checks it against choices list.
        if user_input in choices:
            # If in list, returns value.
            return user_input
        else:
            # Else tells user to enter a valid option.
            print("Please enter one of the options"
                  " as listed above.")


def check_int_input(question):
    """Takes a question and keeps asking user until a valid answer is entered,
    which it then returns"""
    # Repeats until correct input entered.
    while True:
        try:
            # Asks question program inputs.
            user_input = int(input(question))
        # If it's not an int it tells the user.
        except ValueError:
            print("Please enter a positive integer")
        else:
            if user_input < 0:
                print("Please enter a positive integer")
            else:
                return(user_input)
# Program Specific Functions.


def damage_calculator(attacker_attack_choice, type_of_attacked) -> int:
    """Uses attack chosen and type of pokemon attacked to calculate damage,
    Based on which attacks are which effective against which types."""
    # TODO: Function.
    # Example Structure, can copy and fill names after feedback.
    # Gets the type of pokemon that is being attacked.
    if type_of_attacked == "Type1":
        # If attack is effective against this type, it can deal 200-300 damage.
        if attacker_attack_choice == "Type1_effective_attack":
            return randint(200, 300)
        # If it is only moderately effective, it deals between 100-200.
        elif attacker_attack_choice == "Type1_moderately_effective_attack":
            return randint(100, 200)
        # If it is not effective it can deal no more than 100.
        elif attacker_attack_choice == "Type1_not_effective_attack":
            return randint(1, 100)


def battle(your_name: str, your_hp: int, your_type: str, your_attacks: list,
           enemy_name: str, enemy_hp: int, enemy_type: str,
           enemy_attacks: list):
    """Starts the combat loop, and returns health of user's pokemon at the end.
    All input strings must have proper capitalisation."""
    # Repeats until combat finished.
    while True:
        # Display information (and graphic?) to user.
        # Displays enemy's name, as well as their health.
        # And the type of pokemon they are.
        print("""ENEMY POKÉMON: Name: {} HP: {} Type: {}
YOUR POKÉMON: Name: {} HP: {} Type: {}""".format(
            enemy_name, enemy_hp, enemy_type, your_name, your_hp, your_type))
        # Let them make choice around which attack to use.
        # Prints out all attacks in a list.
        print("\n{}'s Attacks:".format(your_name))
        print(", ".join(your_attacks))
        # Asks user to choose one and saves choice.
        your_attack_choice = check_str_input("Choose your Attack: ",
                                             your_attacks)
        # For debug, comment out later.
        print(your_attack_choice)
        # Calculate damage.
        # Uses enemy type and attack chosen to determine damage.
        your_attack_damage = damage_calculator(your_attack_choice, enemy_type)
        # Inform user of updates.
        print("{} used {}!".format(your_name, your_attack_choice))
        # Every pokemon has 1000 hp total.
        # Message saying how effective it was based on damage ranges.
        # If between 0 and 50 then it's not effective.
        if your_attack_damage < 50:
            print("{}'s attack was ineffective!".format(your_name))
        # 50-150 is effective, but not very.
        elif your_attack_damage < 150:
            print("{}'s attack was somewhat effective!".format(your_name))
        # 150-215 is more effective, but it can still be better.
        elif your_attack_damage < 215:
            print("{}'s attack was effective!".format(your_name))
        # 215 and upwards (to max of 300) is the most effective kind.
        else:
            print("{}'s attack was VERY EFFECTIVE!".format(your_name))
        enemy_hp -= your_attack_damage
        print("{} lost {} HP!".format(enemy_name, your_attack_damage))
        # Check if defeated, if so exit.
        if enemy_hp <= 0:
            print("{} is defeated!".format(enemy_name))
            # Returns current HP, so user can heal pokemon later.
            return your_hp
        # Switch to enemy.
        # Choose attack for enemy.
        # Randomly selects attack from list.
        enemy_attack_choice = enemy_attacks[randint(0, len(enemy_attacks) - 1)]
        # Calculate damage.
        enemy_attack_damage = damage_calculator(enemy_attack_choice, your_type)
        # Inform user of updates.
        print("{} used {}!".format(enemy_name, enemy_attack_choice))
        # Message saying how effective it was based on damage ranges.
        # If between 0 and 50 then it's not effective.
        if enemy_attack_damage < 50:
            print("{}'s attack was ineffective!".format(enemy_name))
        # 50-150 is effective, but not very.
        elif enemy_attack_damage < 150:
            print("{}'s attack was somewhat effective!".format(enemy_name))
        # 150-215 is more effective, but it can still be better.
        elif enemy_attack_damage < 215:
            print("{}'s attack was effective!".format(enemy_name))
        # 215 and upwards (to max of 300) is the most effective kind.
        else:
            print("{}'s attack was VERY EFFECTIVE!".format(enemy_name))
        your_hp -= enemy_attack_damage
        print("{} lost {} HP!".format(your_name, enemy_attack_damage))
        # Check if defeated, if so exit.
        if your_hp <= 0:
            print("{} is defeated!".format(your_name))
            # Returns current HP, so user can heal pokemon later.
            # As your pokemon is defeated however, program can just return 0.
            return 0


# For testing.
battle("Playername", 750, "Type1", ["Type1_effective_attack",
                                    "Type1_moderately_effective_attack",
                                    "Type1_not_effective_attack"],
       "Enemyname", 700, "Type1", ["Type1_effective_attack",
                                   "Type1_moderately_effective_attack",
                                   "Type1_not_effective_attack"])
