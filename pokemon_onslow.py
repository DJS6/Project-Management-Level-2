def battle(your_name, your_hp, your_type, your_attacks,
           enemy_name, enemy_hp, enemy_type, enemy_attacks):
    """Starts the combat loop, and returns relevant info at the end."""
    # Repeats until combat finished.
    while True:
        # Display information (and graphic?) to user.
        # Displays enemy's name, as well as their health.
        # And the type of pokemon they are.
        print("""
ENEMY POKÉMON:                                      YOUR POKÉMON:
Name: {}                                            Name: {}
HP: {}                                              HP: {}
{} Type                                             {} Type""".format(
            enemy_name, your_name, enemy_hp, your_hp, enemy_type, your_type))
        # Let them make choice around which attack to use.
        print("{}'s Attacks:".format(your_name))
        # Calculate damage.
        # Inform user of updates.
        # Check if defeated, if so exit.
        # Switch to enemy.
        # Choose attack for enemy.
        # Calculate damage.
        # Inform user of updates.
        # Check if defeated, if so exit.
        # Switch to user.
