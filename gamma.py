# Project Gamma
# Prototype text-game engine in python

# Initial Creation Date : 2023-04-15
# by Robert Raymond Alpizar, Stop Being Logical Software

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####

class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.role = ""
        self.brawn = 0
        self.swiftness = 0
        self.cleverness = 0
        self.health = 0
        self.savvy = 0
        self.allure = 0
        self.status_effects = []
        self.location = ""
        self.game_over = False

myPlayer = player()

#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() # Placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() # Placeholder
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('###########################')
    print('# Welcome to the Text RPG #')
    print('###########################')
    print('          - Play -         ')
    print('          - Help -         ')
    print('          - Quit -         ')
    print('      - Copyright Me -     ')
    title_screen_selections()

def help_menu():
    print('#######################################')
    print('#       Welcome to the Text RPG       #')
    print('#######################################')
    print(' - Use Up, Down, Left, Right to move - ')
    print(' - Type your commands to do them - ')
    print(' - Use "look" to inspect something - ')
    print(' - Good luck and have fun! - ')
    title_screen_selections()


#### Game Interactivity ####

def print_location():
    print('\n' + ('#' * (4 * len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 * len(myPlayer.location))))

def prompt():
    print("\n" + "==================")
    print('What would you like to do?')
    action = input("> ")
    accecptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in accecptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myaction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    print("You can do something...")

#### Game Functionality ####
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # blah blah



#### Map ####

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

zonemap = {
    'a1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        UP: 'a2',
        DOWN: 'a3',
        LEFT: 'a4',
        RIGHT: 'a5',
    }
}

def setup_game():
    os.system('clear')

    ### Name Collection ###
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name    
    
    question2 = "Hello, what's your role?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'priest', 'mage']
    if player_job.lower() in valid_jobs:
        myPlayer.role = player_job    
        print("You are now a " + player_job + "\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.role = player_job    
            print("You are now a " + player_job + "\n")

    if myPlayer.role is 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.role is 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.role is 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60

    os.system('clear')

    main_game_loop()

title_screen()