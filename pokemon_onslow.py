from random import randint
# Defines character list and constants for access.
all_characters_list = [["Name", 1000, "Type1", ["Attack1", "Attack2"]],
                       ["Name2", 1500, "Type1", ["Attack3", "Attack4"]]]
CHARACTERS_NAMES_INDEX = 0
CHARACTERS_HP_INDEX = 1
CHARACTERS_TYPES_INDEX = 2
CHARACTERS_ATTACKS_INDEX = 3
money = 100
# Common Functions.


def check_str_input(question: str, choices: list):
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
            return randint(225, 350)
        # If it is only moderately effective, it deals between 100-200.
        elif attacker_attack_choice == "Type1_moderately_effective_attack":
            return randint(113, 225)
        # If it is not effective it can deal no more than 100.
        elif attacker_attack_choice == "Type1_not_effective_attack":
            return randint(1, 112)


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
        print("""\nENEMY POKÉMON: Name: {} HP: {} Type: {}\n
YOUR POKÉMON: Name: {} HP: {} Type: {}""".format(
            enemy_name, enemy_hp, enemy_type, your_name, your_hp, your_type))
        # Let them make choice around which attack to use.
        # Prints out all attacks in a list.
        print("\n{}'s Attacks:".format(your_name))
        print(", ".join(your_attacks))
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
        # Every pokemon has 1000 hp total.
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
        # Check if defeated, if so exit.
        if enemy_hp <= 0:
            print("\n{} is defeated!".format(enemy_name))
            # Returns current HP, so user can heal pokemon later.
            return your_hp
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
        # Check if defeated, if so exit.
        if your_hp <= 0:
            print("\n{} is defeated!".format(your_name))
            # Returns current HP, so user can heal pokemon later.
            # As your pokemon is defeated however, program can just return 0.
            return 0


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
                print("You now have {} HP and ${:2f}".format())
                # Returns updated figures for cost and health.
                return hp, money


# For testing.
user_name, user_hp, user_type, user_attacks = character_selection(
    all_characters_list)
print(user_name)
print(user_hp)
print(user_type)
print(user_attacks)
current_user_hp = user_hp
user_hp = battle(
    "Playername", 750, "Type1", ["Type1_effective_attack",
                                 "Type1_moderately_effective_attack",
                                 "Type1_not_effective_attack"],
    "Enemyname", 700, "Type1", ["Type1_effective_attack",
                                "Type1_moderately_effective_attack",
                                "Type1_not_effective_attack"])
current_user_hp, money = heal(money, current_user_hp, user_hp)
