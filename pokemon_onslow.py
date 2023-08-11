from random import randint
from time import sleep
# Defines character list and constants for access.
ALL_CHARACTERS_LIST = [["Science", 1450, "STEM",
                        ["Chemical chuck", "Safety glasses sunbeam",
                         "Radioactive rumble"]],
                       ["Maths", 1300, "STEM",
                        ["Trigonometry throw", "Mathlete math-yeet",
                         "Calculus crunch"]],
                       ["Digitech", 1500, "STEM",
                        ["Keyboard k.o.", "Software slay",
                         "Rust-y nail roll"]],
                       ["Art", 1100, "Arts",
                        ["Painting punch", "Sculpture smash",
                         "Watercolour wipeout"]],
                       ["Music", 1400, "Arts",
                        ["Saxophone shred", "Drumming destruction",
                         "Double bass drop"]],
                       ["Drama", 1050, "Arts",
                        ["Theatre kid throw", "Blocking blow",
                         "Production prod"]]]
CHARACTERS_NAMES_INDEX = 0
CHARACTERS_HP_INDEX = 1
CHARACTERS_TYPES_INDEX = 2
CHARACTERS_ATTACKS_INDEX = 3
money = 150
STEM_EFFECTIVE_INDEX = 0
STEM_MODERATE_INDEX = 1
STEM_INEFFECT_INDEX = 2
ARTS_INEFFECT_INDEX = 0
ARTS_MODERATE_INDEX = 1
ARTS_EFFECTIVE_INDEX = 2
# Function to use in working out lists.


def effectiveness_list_creator(index: int) -> list:
    """Using an index appends attack for all characters to list and returns."""
    # Sets up list to append to.
    effectiveness_list = []
    # Runs through every character in list.
    for character in ALL_CHARACTERS_LIST:
        # Appends correct attack from each character's list.
        effectiveness_list.append(character[CHARACTERS_ATTACKS_INDEX][index])
    return effectiveness_list


# Lists of which attacks are effective and not against specific types.
# Works out each list by appending the correct attack from each character.
STEM_EFFECTIVE_ATTACKS = effectiveness_list_creator(STEM_EFFECTIVE_INDEX)
STEM_MODERATE_ATTACKS = effectiveness_list_creator(STEM_MODERATE_INDEX)
STEM_INEFFECT_ATTACKS = effectiveness_list_creator(STEM_INEFFECT_INDEX)
ARTS_EFFECTIVE_ATTACKS = effectiveness_list_creator(ARTS_EFFECTIVE_INDEX)
ARTS_MODERATE_ATTACKS = effectiveness_list_creator(ARTS_MODERATE_INDEX)
ARTS_INEFFECT_ATTACKS = effectiveness_list_creator(ARTS_INEFFECT_INDEX)
# Common Functions.


def check_str_input(question: str, choices: list) -> str:
    """Asks user a question, then checks user's input against a list of
       possible choices and ensures it's in it"""
    # Fixes up choices list so it doesn't care about capitalisation.
    lower_choices = []
    for choice in choices:
        # Gets every choice and lowers the case.
        lower_choices.append(choice.lower())
    # Repeats until value returned.
    while True:
        # Asks question and saves answer.
        user_input = str(input(question))
        # Makes it more readable.
        user_input = user_input.lower().strip()
        # Checks it against choices list.
        if user_input in lower_choices:
            # Reformats input case for later in program.
            user_input = user_input.replace(
                user_input[0], user_input[0].upper(), 1)
            # If in list, returns value.
            return user_input
        else:
            # Else tells user to enter a valid option.
            print("Please enter one of the options"
                  " as listed above.")


def check_int_input(question) -> int:
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
    # Example Structure, can copy and fill names after feedback.
    # Gets the type of pokemon that is being attacked.
    if type_of_attacked == "STEM":
        # If attack is effective against this type, it can deal 200-300 damage.
        if attacker_attack_choice in STEM_EFFECTIVE_ATTACKS:
            return randint(225, 350)
        # If it is only moderately effective, it deals between 100-200.
        elif attacker_attack_choice in STEM_MODERATE_ATTACKS:
            return randint(113, 225)
        # If it is not effective it can deal no more than 100.
        elif attacker_attack_choice in STEM_INEFFECT_ATTACKS:
            return randint(1, 112)
    elif type_of_attacked == "Arts":
        # If attack is effective against this type, it can deal 200-300 damage.
        if attacker_attack_choice in ARTS_EFFECTIVE_ATTACKS:
            return randint(225, 350)
        # If it is only moderately effective, it deals between 100-200.
        elif attacker_attack_choice in ARTS_MODERATE_ATTACKS:
            return randint(113, 225)
        # If it is not effective it can deal no more than 100.
        elif attacker_attack_choice in ARTS_INEFFECT_ATTACKS:
            return randint(1, 112)


def enemy_random_select(user_name):
    """Randomly chooses an enemy from the list and returns their attributes."""
    while True:
        random_selection = randint(0, len(ALL_CHARACTERS_LIST) - 1)
        # If the enemy and character names are different it can move on.
        # If they're the same it has to repeat.
        if ALL_CHARACTERS_LIST[
         random_selection][CHARACTERS_NAMES_INDEX] != user_name:
            break
    return ALL_CHARACTERS_LIST[random_selection][
        CHARACTERS_NAMES_INDEX], ALL_CHARACTERS_LIST[
            random_selection][CHARACTERS_HP_INDEX], ALL_CHARACTERS_LIST[
                random_selection][CHARACTERS_TYPES_INDEX], ALL_CHARACTERS_LIST[
                    random_selection][CHARACTERS_ATTACKS_INDEX]


def battle(your_name: str, your_hp: int, your_type: str, your_attacks: list,
           money: int) -> tuple:
    """Start the combat loop, returns health of user's pokemon and their money.
    All input strings must have proper capitalisation."""
    # Randomises enemy choice.
    enemy_name, enemy_hp, enemy_type, enemy_attacks = enemy_random_select(
        your_name)
    # Repeats until combat finished.
    while True:
        # Display information to user.
        # Displays enemy's name, as well as their health.
        # And the type of pokemon they are.
        print("""\nENEMY POKÉMON: Name: {} HP: {} Type: {}\n
YOUR POKÉMON: Name: {} HP: {} Type: {}""".format(
            enemy_name, enemy_hp, enemy_type, your_name, your_hp, your_type))
        sleep(3)
        # Let them make choice around which attack to use.
        # Prints out all attacks in a list.
        print("\n{}'s Attacks:".format(your_name))
        print(", ".join(your_attacks))
        sleep(1)
        # Asks user to choose one and saves choice.
        your_attack_choice = check_str_input("\nChoose your Attack: ",
                                             your_attacks)
        # For debug, comment out later.
        # print(your_attack_choice)
        # Calculate damage.
        # Uses enemy type and attack chosen to determine damage.
        your_attack_damage = damage_calculator(your_attack_choice, enemy_type)
        # Inform user of updates.
        print("\n{} used {}!".format(your_name, your_attack_choice))
        # Message saying how effective it was based on damage ranges.
        # If between 0 and 80 then it's not effective.
        if your_attack_damage < 80:
            print("{}'s attack was ineffective!".format(your_name))
        # 100-160 is effective, but not very.
        elif your_attack_damage < 160:
            print("{}'s attack was somewhat effective!".format(your_name))
        # 160-240 is more effective, but it can still be better.
        elif your_attack_damage < 240:
            print("{}'s attack was effective!".format(your_name))
        # 240 and upwards (to max of 350) is the most effective kind.
        else:
            print("{}'s attack was VERY EFFECTIVE!".format(your_name))
        enemy_hp -= your_attack_damage
        print("\n{} lost {} HP!".format(enemy_name, your_attack_damage))
        sleep(2)
        # Check if defeated, if so exit.
        if enemy_hp <= 0:
            print("\n{} is defeated!\nYOU WIN!".format(enemy_name))
            # Returns current HP, so user can heal pokemon later.
            # Calculates uncertain reward and returns that and your HP.
            money += randint(150, 250)
            return your_hp, money
        # Switch to enemy.
        # Choose attack for enemy.
        # Randomly selects attack from list.
        enemy_attack_choice = enemy_attacks[randint(0, len(enemy_attacks) - 1)]
        # Calculate damage.
        enemy_attack_damage = damage_calculator(enemy_attack_choice, your_type)
        # Inform user of updates.
        print("\n{} used {}!".format(enemy_name, enemy_attack_choice))
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
        print("\n{} lost {} HP!".format(your_name, enemy_attack_damage))
        sleep(1)
        # Check if defeated, if so exit.
        if your_hp <= 0:
            print("\n{} is defeated!\nYOU LOSE!".format(your_name))
            # Returns current HP, so user can heal pokemon later.
            # As your pokemon is defeated however, program can just return 0.
            return 0, money


def character_selection(all_characters_list: list) -> tuple:
    """Allows user to choose a character and returns name, type, [Attacks]"""
    character_names = []
    print("CHOOSE YOUR CHARACTER!")
    # Goes through entire list.
    for character in all_characters_list:
        # Creates a list of all names for when user decides to input.
        character_names.append(character[CHARACTERS_NAMES_INDEX])
        # Prints names, healths, and types of each character.
        print("\n{}: {} HP {} Type\nAttacks:".format(
            character[CHARACTERS_NAMES_INDEX],
            character[CHARACTERS_HP_INDEX], character[CHARACTERS_TYPES_INDEX]))
        # Prints all attacks for each character.
        for attack in character[CHARACTERS_ATTACKS_INDEX]:
            print(attack)
        sleep(3)
    # Asks user for character choice and saves it.
    character_name_choice = check_str_input(
        "\nEnter the Name of Character You Wish to Choose: ", character_names)
    # Finds the index that that name is in the list.
    user_choice_index = character_names.index(character_name_choice)
    # Returns name, index, and attacks in that order.
    return all_characters_list[user_choice_index][
        CHARACTERS_NAMES_INDEX], all_characters_list[user_choice_index][
            CHARACTERS_HP_INDEX], all_characters_list[user_choice_index][
            CHARACTERS_TYPES_INDEX], all_characters_list[user_choice_index][
                CHARACTERS_ATTACKS_INDEX]


def heal(money: int, hp: int, max_hp: int) -> tuple:
    """Ask user how much they want to heal, validates int and charges money."""
    while True:
        # Tells user how much health they have and how much is their max.
        print("\nYou currently have {} HP, and you can heal up to a"
              " maximum of {} HP".format(hp, max_hp))
        # Asks user the question
        heal_amount = check_int_input(
            "How much HP do you want to heal? (Enter 0 if none): ")
        # If user tries to heal over their maximum.
        if heal_amount + hp > max_hp:
            print("You can't heal that much HP as it exceeds your maximum.")
        else:
            # Calculates the cost of the healing.
            # 50 cents per HP healed.
            cost = int(heal_amount * 0.5)
            # If it's too expensive.
            if cost > money:
                print("You cannot afford the cost of "
                      "${:.2f} as you only have ${:.2f}".format(cost, money))
            else:
                # Adds amount to heal to your HP.
                hp += heal_amount
                # Removes cost from your money.
                money -= cost
                # Tells user what just happened.
                print("You have been healed for {} HP, for ${:.2f}".format(
                    heal_amount, cost))
                print("You now have {} HP and ${:.2f}".format(hp, money))
                # Returns updated figures for cost and health.
                return hp, money


# Setting user up with character.
# Welcome Message.
print("WELCOME TO POKÉMON ONSLOW!\n")
sleep(1)
# Character Selection.
user_name, user_hp, user_type, user_attacks = character_selection(
    ALL_CHARACTERS_LIST)
# Sets user hp to maximum.
current_user_hp = user_hp
# Explains the game.
# Can change the number of rounds of pokemon.
print("""\nIn this game you can battle as many Pokémon as you wish,
the more you battle the greater your reward.
The aim is to defeat as many as possible to get the most money,
however you must be strategic, because if you lose against one of them,
you lose the game (and your money).\nGOOD LUCK!\n""")
sleep(1)
input("Press enter to continue: ")
# Main Game Loop.
while True:
    # Starts Battle.
    current_user_hp, money = battle(
        user_name, user_hp, user_type, user_attacks, money)
    # Checks if user lost the battle.
    if current_user_hp == 0:
        # Tells them final score and ends game.
        print("You reached a final score of ${:.2f}".format(money))
        break
    # Asks user if they wish to continue.
    continue_yn = check_str_input(
        "Do you wish to face another Pokémon? (y/n) ", ["y", "n"])
    # If no, tells them final score and leaves programme.
    if continue_yn == "N":
        print("You reached a final score of ${:.2f}".format(money))
        break
    # Heal function.
    current_user_hp, money = heal(money, current_user_hp, user_hp)
