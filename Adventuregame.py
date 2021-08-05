#First try adventure game
#Cameron Hale
#Feb 8 2021

from game.game import rooms

inventory = []          #come back to this

class pickup:                   #item that can be picked up and inspected
    def __init__(self, name, appearance, desc):
        self.name = name
        self.appearance = appearance
        self.desc = desc
    
    def inspect(desc):          #dont fully know how im gonna do this yet
        print(desc)

def pocket(pickup):             #puts pickup item in inventory list when called
    inventory.append(pickup)

Objects = {

}

print("Welcome to your adventure. In this game there are no take-backs, no save points, and no bathroom breaks.")
startchoice = input("Would you like to begin? y/n: ")
if startchoice != "y":
    print("Well screw you, then")
    exit()
elif startchoice == "y":
    print("Starting in 3...2...1...")
    location = "start"

while True:
    current_room = rooms.get(location)

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
    direction = input('Which way will you go? ').lower()

    next_location = current_room.get_exit(direction)
    if next_location is None:
        print('Not allowed')
        continue

    location = next_location
    continue