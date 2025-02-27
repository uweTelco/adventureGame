import time
import random
import os

def print_sleep(message, wait_time):
    print(message)
    time.sleep(wait_time)

def print_sleep_2s(message):
    print_sleep(message,1)   

def intro():
    print_sleep_2s("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_sleep_2s("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    starting_choice()
    
    
def starting_choice():
    if own_health > 0:
        if dead_enemie in enemies:
            print_sleep("Gerat you defeeded the bad " + dead_enemie, 5)
            return
    else:
        print_sleep_2s("It might be a good idea to visit the house more often.")
        return
    print_sleep_2s("In front of you is a house.")
    print_sleep_2s("To your right is a dark cave.")
    print_sleep_2s("In your hand you hold your trusty (but not very effective) "+ weapon + ".")
    print_sleep_2s("Make a choice: Go into the cave (press 1) or knock at the door (press 2)")
    next_step = -1
    while next_step not in [1,2]:
        try:
            next_step = int(input("Make your choice: "))
            
            #print("Your choice: " + str(next_step))
        except ValueError:
            print("Please help and make a valid choice: 1, or 2")

    os.system("clear")
    if next_step == 1:
        cave()
    elif next_step == 2:
        house()
        os.system("clear")
   
def fight():
    # Things that happen when the player fights  
    global own_health, enemies_health,dead_enemie,enemy
    os.system("clear")
    print_sleep_2s("You take out your weapon: " + weapon + " and prepare to fight the enemy.")
    hit_minimun = -1 - enemies.index(enemy)
    hit_maximum = 0
    if weapon in weapons:
      hit_maximum = 1 + weapons.index(weapon)%2
    else:
        hit_maximum = 4
    hit = random.randint(hit_minimun,hit_maximum)
    if (hit > 0):
        print_sleep_2s("Great, you hit the " + enemy+ " hard.")
        print_sleep_2s("It loses " + str(hit) + " from its health.")
        enemies_health -= hit
        if enemies_health <= 0:
            dead_enemie = enemy
            return
    elif (hit < 0):
        print_sleep_2s("Oh no, the enemy punched you hard and your health goes down by " + str(hit *-1))
        own_health += hit
        if(own_health <= 0):
            return
    print_sleep_2s("Now after this round, you seem to have a choice of ")
    print_sleep_2s("Continue the fight by pressing 1 or ")
    print_sleep_2s("hide back to the house and cave by pressing 2")
    next_step = -1
    while next_step not in [1,2]:
        try:
            next_step = int(input("Make your choice: "))
            #print("Your choice: " + str(next_step))
        except ValueError:
            print("Please help and make a valid choice: 1, or 2")
    if next_step == 1:
        fight()
    elif next_step == 2:
        starting_choice()


def cave():
    # Things that happen to the player goes in the cave 
    global visit_cave, weapon
    if visit_cave == False: 
        print_sleep_2s("Great you found a sword, this might help you.")
        weapon = "sword"
        visit_cave = True
    else: 
        print_sleep_2s("Nothing has changed here, now this room seems dark and empty.")
    starting_choice()

    
def field():
    # Things that happen when the player runs back to the field
    print_sleep_2s("\"I was waiting for you\" says the " + enemy)
    print_sleep_2s("There is no choice, you have to fight, ")
    print_sleep_2s("now")
    fight()

    
def house():
    # Things that happen to the player in the house
    health_plus = random.randint(1,7)
    print_sleep_2s("A little elf opens the door and welcomes you in.")
    print_sleep_2s("It provides you with food, which increases your health by "+ str(health_plus)+".")
    own_health = add_health(health_plus)
    print_sleep_2s("As you leave the house, you see the evil " + enemy + " on the field.")
    field()


def add_health(a):
    result = a + own_health
    if result > 12:
        return 12  # or you could return the sum capped at 10
    return result

game_on = True

while game_on == True:
    os.system("clear")
    visit_cave = False
    dead_enemie = ""
    own_health = 10
    house_visits = 0
    weapons = ["dagger", "boomerang", "stick"]
    enemies = ["troll", "wicked fairie", "pirate", "gorgon", "dragon"]
    enemy = random.choice(enemies)
    enemies_health = 8 + enemies.index(enemy)
    weapon = random.choice(weapons)
    intro()
    print("GAME OVER")
    print_sleep_2s("You have a score of " + str(10+own_health) + " and  visited the house " + str(house_visits))
    print_sleep_2s("Thanks for playing the Adventure \n brought to you by Udacity and Uwe")
    replay = input("Would you like to play again? (y/n)")
    if replay not in ["y","Y"]:
        game_on = False        

