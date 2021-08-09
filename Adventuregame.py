#First try adventure game
#Cameron Hale
#Feb 8 2021

from game.portal import Portal
import random
from game.inventory import Inventory
import game

def translate_command(command):
    tokens = command.split(' ')
    if len(tokens) == 1:
        if 'north'.startswith(tokens[0]):
            return 'go', 'north'
        elif 'south'.startswith(tokens[0]):
            return 'go', 'south'
        elif 'east'.startswith(tokens[0]):
            return 'go', 'east'
        elif 'west'.startswith(tokens[0]):
            return 'go', 'west'
        elif "look".startswith(tokens[0]):
            return 'look', None
        elif "inventory".startswith(tokens[0]):
            return "inventory", None
        elif "help".startswith(tokens[0]):
            return "help", None
        else:
            return None, None
    elif len(tokens) == 2:
        return tokens[0], tokens[1]
    elif len(tokens) > 2:
        return tokens[0], " ".join(tokens[1:])
    return None, None

print("Welcome to your adventure. In this game there are no take-backs, no save points, and no bathroom breaks.")
startchoice = input("Would you like to begin? y/n: ")
if startchoice != "y":
    print("Well screw you, then")
    exit()
elif startchoice == "y":
    print("Starting in 3...2...1...")
    location = "start"

inventory = Inventory()

while True:
    current_room = game.rooms.get(location)

    if current_room is None:
        print('Where the heck are you?!')
        exit()


    print(current_room.desc)

    if current_room.is_game_over:
        print("You died.")
        yorn = input('Play again?').lower()
        if yorn == 'y':
            location = 'start'
            continue
        else:
            print('kthxbye')
            exit()

    print('Exits are:', ", ".join(current_room.get_exit_directions()))

    command = input("What will you do? ").lower()

    verb, noun = translate_command(command)

    if verb == 'go':
        direction = noun

        portal = current_room.get_exit(direction)
        if portal is None:
            print('Not allowed')
            continue

        if portal.can_pass(inventory):
            location = portal.dest
        
        else:
            print("Hmm, looks like you need something to open this door.")
        
        continue

    elif verb == 'look':
        items = current_room.get_items()
        if len(items) == 0:
            print('There\'s nothing here')
        else:
            print('You find:', ", ".join(items))
        continue

    elif verb == 'pickup':
        item_name = noun

        item = current_room.get_item(item_name)
        if item is None:
            print("There isn't a %s here" % item_name)
            continue
        print("You got it!")
        inventory.pocket(item)
        current_room.remove_item(item)
        continue
    
    elif verb == "inventory":
        items = inventory.get_items()
        if len(items) == 0:
            print('You don\'t have anything')
        else:
            print("You have:", ", ".join(items))
    
    elif verb == "help":
        print("Commands are: n/north, s/south, w/west, e/east, i/inventory, l/look, and pickup 'item'")
    
    else:
        print(random.choice([
            'Huh?',
            'Wha?',
            'Are you talkin\' to me?',
            'Nope',
            'Oh I don\'t think so',
        ]))
    