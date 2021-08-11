#First try adventure game
#Cameron Hale
#Feb 8 2021

from colorama import init as colorama_init
from colorama.ansi import Fore, Back, Style
from colorama.initialise import reset_all
from game.portal import Portal
import random
from game.inventory import Inventory
import game

colorama_init()

def print_coloured_string(s, colour = Fore.WHITE, bg_colour = Back.BLACK, **kwargs):
    print(f"{colour}{bg_colour}{s}{Style.RESET_ALL}", **kwargs)

def get_input(prompt):
    print_coloured_string(prompt, Fore.GREEN, end=" ")
    return input().lower()

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

print("")
print_coloured_string("Welcome to your adventure. In this game there are no take-backs, no save points, and no bathroom breaks.")
print("")
startchoice = get_input("Would you like to begin? y/n:")
if startchoice != "y":
    print("")
    print_coloured_string("Well screw you, then", Fore.RED)
    print("")
    exit()
elif startchoice == "y":
    print("")
    print_coloured_string("Starting in 3...2...1...", Fore.CYAN)
    print("")
    location = "start"

inventory = Inventory()
last_room = ""


while True:
    current_room = game.rooms.get(location)

    if current_room is None:
        print_coloured_string('Where the heck are you?!', Fore.RED)
        exit()

    if current_room.is_game_over:
        print_coloured_string(current_room.desc)
        print("")
        print_coloured_string("You died.", Fore.RED)
        print("")
        yorn = get_input('Play again?')
        print("")
        if yorn == 'y':
            location = 'start'
            continue
        else:
            print_coloured_string('kthxbye', Fore.RED)
            exit()
    elif current_room.is_win_game:
        print_coloured_string(current_room.desc)
        print("")
        print_coloured_string("Congerations! You done it!", Fore.BLACK, Back.WHITE)
        print("")
        restart = get_input("Would you like to play again?")
        print("")
        if restart == "y":
            location="start"
            continue
        else:
            print("Thank you for playing!")
            exit()

    if current_room != last_room:
        print_coloured_string(current_room.desc)
        print("")
        print(f'{Fore.CYAN}{Back.BLACK}Exits are:', ", ".join(current_room.get_exit_directions()), end=f"{Fore.WHITE}{Back.RESET}\n")
        print("")
        last_room = current_room

    command = get_input("What will you do?")

    verb, noun = translate_command(command)
    
    print("")
    if verb == 'go':
        direction = noun

        portal = current_room.get_exit(direction)
        if portal is None:
            print_coloured_string('Not allowed', Fore.CYAN)
            print("")

            continue

        if portal.can_pass(inventory):
            if portal.pass_message is not None:
                print_coloured_string(portal.pass_message, Fore.CYAN)
                print("")
            last_room = current_room
            location = portal.get_dest(inventory)
        
        else:
            if portal.blocked_message is not None:
                print_coloured_string(portal.blocked_message, Fore.CYAN)
                print("")
        
        continue

    elif verb == 'look':
        print_coloured_string(current_room.desc)
        items = current_room.get_items()
        if len(items) == 0:
            print("")
            print_coloured_string('There\'s nothing here', Fore.MAGENTA)
            print("")
        else:
            print("")
            print(f'{Fore.MAGENTA}{Back.BLACK}You find:', ", ".join(items), end=f"{Fore.WHITE}{Back.RESET}\n")
            print("")
        continue

    elif verb == 'pickup':
        item_name = noun

        item = current_room.get_item(item_name)
        if item is None:
            print("")
            print_coloured_string("There isn't a %s here" % item_name, Fore.MAGENTA)
            print("")
            continue
        print("")
        print_coloured_string("You got it!", Fore.MAGENTA)
        print("")
        inventory.pocket(item)
        current_room.remove_item(item)
        continue
    
    elif verb == "inventory":
        items = inventory.get_items()
        if len(items) == 0:
            print_coloured_string('You don\'t have anything :(', Fore.MAGENTA)
            print("")
        else:
            print(f"{Fore.MAGENTA}{Back.BLACK}You have:", ", ".join(items), end=f"{Fore.WHITE}{Back.RESET}\n")
            print("")
    
    elif verb == "help":
        print_coloured_string("Commands are: n/north, s/south, w/west, e/east, i/inventory, l/look, and pickup 'item'", Fore.BLACK, Back.YELLOW)
        print("")
    
    else:
        print("")
        print_coloured_string(random.choice([
            'Huh?',
            'Wha?',
            'Are you talkin\' to me?',
            'Nope',
            'Oh I don\'t think so',
        ]), Fore.GREEN)
        print("")
    