import time
import random
import os
"""
This module enables you to play an adventure game.
"""

def print_sleep(message, wait_time):
    """
    Prints the "message" and sleeps the process shortly
    
    Parameters:
    message (String): The message to be displayed
    wait_time (int): Time in seconds to sleep 
    """
    print(message)
    time.sleep(wait_time)


def print_sleep_2s(message):
    """
    Prints the message and delays the process for 2 seconds.
    
    Parameters:
    message (String): The message to be displayed
    """
    print_sleep(message, 2)


def intro():
    """
    Intro of the game. 
    """
    print_sleep_2s(
        "You find yourself standing in an open field, "
        + "filled with grass and yellow wildflowers."
    )
    print_sleep_2s(
        "Rumor has it that a wicked fairie is somewhere "
        + "around here, and has been terrifying the nearby village."
    )
    starting_choice()


def starting_choice():
    """
    Displays the primary choice where the user stands at the begining
    other times while the game. 
    """
    if OWN_HEALTH > 0:
        if DEAD_ENEMIE in enemies:
            print_sleep("Gerat you defeeded the bad " + DEAD_ENEMIE, 5)
            return
    else:
        print_sleep_2s("It might be a good idea" +
                       " to visit the house more often.")
        return
    print_sleep_2s("In front of you is a house.")
    print_sleep_2s("To your right is a dark cave.")
    print_sleep_2s(
        "In your hand you hold your trusty (but not very effective) "
        + weapon + "."
    )
    print_sleep_2s(
        "Make a choice: Go into the cave (press 1) " +
        "or knock at the door (press 2)"
    )
    next_step = -1
    while next_step not in [1, 2]:
        try:
            next_step = int(input("Make your choice: "))

            # print("Your choice: " + str(next_step))
        except ValueError:
            print("Please help and make a valid choice: 1, or 2")

    os.system("clear")
    if next_step == 1:
        cave()
    elif next_step == 2:
        house()
        os.system("clear")


def fight():
    """
    Simulates the fight of the user against a random enemy. 
    Uses a number of global existing variables:
    OWN_HEALTH, enemies_health, DEAD_ENEMIE, enemy
    """
    # Things that happen when the player fights
    global OWN_HEALTH, enemies_health, DEAD_ENEMIE, enemy
    os.system("clear")
    print_sleep_2s(
        "You take out your weapon: " + weapon +
        " and prepare to fight the enemy."
    )
    hit_minimun = -1 - enemies.index(enemy)
    hit_maximum = 0
    if weapon in weapons:
        hit_maximum = 1 + weapons.index(weapon) % 2
    else:
        hit_maximum = 4
    hit = random.randint(hit_minimun, hit_maximum)
    if hit > 0:
        print_sleep_2s("Great, you hit the " + enemy + " hard.")
        print_sleep_2s("It loses " + str(hit) + " from its health.")
        enemies_health -= hit
        if enemies_health <= 0:
            DEAD_ENEMIE = enemy
            return
    elif hit < 0:
        print_sleep_2s(
            "Oh no, the enemy punched you hard and your health goes down by "
            + str(hit * -1)
        )
        OWN_HEALTH += hit
        if OWN_HEALTH <= 0:
            return
    print_sleep_2s("Now after this round, you seem to have a choice of ")
    print_sleep_2s("Continue the fight by pressing 1 or ")
    print_sleep_2s("hide back to the house and cave by pressing 2")
    next_step = -1
    while next_step not in [1, 2]:
        try:
            next_step = int(input("Make your choice: "))
        except ValueError:
            print("Please help and make a valid choice: 1, or 2")
    if next_step == 1:
        fight()
    elif next_step == 2:
        starting_choice()


def cave():
    """
    Describes the user what he can find in the cave.
    """
    # Things that happen to the player goes in the cave
    global VISIT_CAVE, weapon
    if VISIT_CAVE is False:
        print_sleep_2s("Great you found a sword, this might help you.")
        weapon = "sword"
        VISIT_CAVE = True
    else:
        print_sleep_2s(
            "Nothing has changed here," +
            " now this room seems dark and empty."
        )
    starting_choice()


def field():
    """
    The talk of the enemy before the fight, and calls fight.
    """
    # Things that happen when the player runs back to the field
    print_sleep_2s('"I was waiting for you" says the ' + enemy)
    print_sleep_2s("There is no choice, you have to fight, ")
    print_sleep_2s("now")
    fight()


def house():
    """
    Describes the situation inside the house.
    The user will be healt a little here.
    """
    # Things that happen to the player in the house
    health_plus = random.randint(1, 7)
    print_sleep_2s("A little elf opens the door and welcomes you in.")
    print_sleep_2s(
        "It provides you with food, which increases your health by "
        + str(health_plus)
        + "."
    )
    OWN_HEALTH = add_health(health_plus)
    print_sleep_2s(
        "As you leave the house, you see the evil " + enemy + " on the field."
    )
    field()


def add_health(a):
    """
    Adds helath to the users health, and takes care that the user
    can not have a higher helath than 12
    
    Parameters:
    a (int): The number to increase the health.
    
    Returns: 
    int: The new health of the user
    """
    result = a + OWN_HEALTH
    if result > 12:
        return 12  # or you could return the sum capped at 10
    return result


game_on = True
while game_on is True:
    os.system("clear")
    VISIT_CAVE = False
    DEAD_ENEMIE = ""
    OWN_HEALTH = 10
    HOUSE_VISITS = 0
    weapons = ["dagger", "boomerang", "stick"]
    enemies = ["troll", "wicked fairie", "pirate", "gorgon", "dragon"]
    enemy = random.choice(enemies)
    enemies_health = 8 + enemies.index(enemy)
    weapon = random.choice(weapons)
    intro()
    print("===========")
    print("=GAME OVER=")
    print("===========")
    print_sleep_2s(
        "You have a score of "
        + str(10 + OWN_HEALTH)
        + " and  visited the house "
        + str(HOUSE_VISITS)
    )
    print_sleep_2s(
        "Thanks for playing the Adventure \nbrought to you by Udacity and Uwe"
    )
    replay = input("Would you like to play again? (y/n)")
    if replay not in ["y", "Y"]:
        game_on = False
