#First try adventure game
#Cameron Hale
#Feb 8 2021

print("Welcome to your adventure. In this game there are no take-backs, no save points, and no bathroom breaks.")
startchoice = input("Would you like to begin? y/n: ")
if startchoice != "y":
    print("Well screw you, then")
    exit()
elif startchoice == "y":
    print("Starting in 3...2...1...")
    location = "start"

while True:

    # Start area
    if location == "start":
        print("You find yourself standing in an open field. To the north is a house. To the east is a long dirt road. To the south is a forest too dense to pass through. To the west is a hill with only one tree atop it.")
        openingchoice = input("Which way will you go? ")
        if openingchoice == "north" or openingchoice == "n":
            location = "outside_house"
        elif openingchoice == "east" or openingchoice == "e":
            location = "dirt_road"
        elif openingchoice == "south" or openingchoice == "s":
            location = "forest_mouth"
        elif openingchoice == "west" or openingchoice == "w":
            location = "tree_hill"
        else:
            print("Try another input")
    
    # Tree hill
    elif location == "tree_hill":
        print("You climb to the top of the hill where you find a mighty oak tree. There are lanterns hanging from the branches, giving off an eerie green light. There is a plaque on the tree that marks the final resting place of one Jeffrey Greenly. You can travel west past the hill or east back to where you began.")
        treehillchoice = input("Which way will you go? ")
        if treehillchoice == "east" or treehillchoice == "e":
            location = "start"
        elif treehillchoice == "west" or treehillchoice == "w":
            location = "well_hill"
        else:
            print("Try another input") 
    
    # Well hill
    elif location == "well_hill":
        print("You climb up a short hill topped with a decrepit old well. The bucket has broken off the rope and lies at the bottom amidst rotting bones. The smells seem to be of seawater and sulfur.")
        wellhillchoice = input("Will you go west to the forest or back to the previous hill? ")
        if wellhillchoice == "w" or wellhillchoice == "west":
            location = "forest_middle_west"
        elif wellhillchoice == "e" or wellhillchoice == "east":
            location = "tree_hill"
        else:
            print("Try another input")

    # Forest middle west
    elif location == "forest_middle_west":
        print("You come to a wall of foliage that blocks your path. You think you can see movement beyond the leaves and vines, but there is no possible passage through.")
        forestmiddlewestchoice = input("Will you go back? ")
        if forestmiddlewestchoice == "y" or forestmiddlewestchoice == "yes":
            location = "well_hill"
        else:
            print("Too bad")
            location = "well_hill"

    # Outside house
    elif location == "outside_house":
        print("The house is small but cozy-looking. The walls are overgrown with vines, giving a feeling that it has been abandoned for some time, but the two lanterns hanging in the doorway are still alight.")
        outsidehousechoice = input("You can go north into the house, or south to where you began. Where will you go?")
        if outsidehousechoice == "north" or outsidehousechoice == "n":
            location = "inside_house"
        elif outsidehousechoice == "south" or outsidehousechoice == "s":
            location = "start"
        else:
            print("Try another input")

    # Inside house
    elif location == "inside_house":
        print("The inside of the house appears ransacked, with books and furniture haphazardly thrown everywhere. When you look closely, you see a thin line of silver in all of the windowframes.")
        insidehousechoice = input("You can exit the house to the south, enter the basement to the west, or exit the back of the house to the north. Where will you go? ")
        if insidehousechoice == "north" or insidehousechoice == "n":
            location = "backyard"
        elif insidehousechoice == "south" or insidehousechoice == "s":
            location = "outside_house"
        elif insidehousechoice == "west" or insidehousechoice == "w":
            location = "basement"
        else:
            print("Try another input")
    
    # Basement
    elif location == "basement":
        print("You walk down the creaky set of stairs to the basement. There are a few chairs on a stone floor. To the north, there is a hole in the wall leading to a damp, dimly lit cave. You can enter the cave or go back to the main floor of the house to the east.")
        basementchoice = input("Where will you go?")
        if basementchoice == "north" or basementchoice == "n":
            location = "cave_entrance"
        elif basementchoice == "east" or basementchoice == "e":
            location = "inside_house"
        else:
            print("Try another input")
    
    # Cave Entrance
    elif location == "cave_entrance":
        print("You stand in the entrance to a dripping cave,the stone pathway branching in front of you to go deeper underground to the north and towards the surface to the west.")
        caveentrancechoice = input("Where will you go?")
        if caveentrancechoice == "north" or caveentrancechoice == "n":
            location = "cave_crossroads"
        elif caveentrancechoice == "south" or caveentrancechoice == "s":
            location = "basement"
        elif caveentrancechoice == "west" or caveentrancechoice == "w":
            location = "cave_west_to_hill"
        else:
            print("Try another input")
    
    # Cave Crossroads
    elif location == "cave_crossroads":
        print("Your path branches again, showing a steel door to the west and a path to to the surface to the east. In front of you is a rough rock wall.")
        cavecrossroadschoice = input("")
        if cavecrossroadschoice == "west" or cavecrossroadschoice == "w":
            location = "ritual_chamber"
        elif cavecrossroadschoice == "east" or cavecrossroadschoice == "e":
            location = "forest_wall_north_of_house"
        elif cavecrossroadschoice == "south" or cavecrossroadschoice == "s":
            location = "cave_entrance"
        else:
            print("Try another input")

    # Ritual Chamber
    elif location == "ritual_chamber":
        print("As you enter this room, the steel door locks behind you. You see strange markings on the wall that appear to be written in blood. On the far west side of the room, there is a deep pool of water. As you look closer, a slimy tentacled beast crawls up from the depths. Your vision goes black.")
        ritualchamberchoice = input("You have died. Would you like to restart? ")
        if ritualchamberchoice == "yes" or ritualchamberchoice == "y":
            location = "start"
        else:
            print("Try another input")

    # Forest Wall North
    elif location == "forest_wall_north_of_house":
        print("You stare into a solid wall of foliage. There is no way of entering the forest from here. You can go south to the backyard from here or west to a cave system.")
        forestwallnorthchoice = input("Where will you go? ")
        if forestwallnorthchoice == "west" or forestwallnorthchoice == "w":
            location = "cave_crossroads"
        if forestwallnorthchoice == "south" or forestwallnorthchoice == "s":
            location = "backyard"
        else:
            print("Try another input")
    
    # Backyard
    elif location == "backyard":
        print("You stand behind the house in a small fenced area populated only by a small tree and three gravestones. They read(from left to right) Roseanne Tyler-Greenly, Ashleigh Greenly, and Jessie Greenly. You can continue north to the wall of the forest, or back to where you came from.")
        backyardchoice = input("Where will you go? ")
        if backyardchoice == "north" or backyardchoice == "n":
            location = "forest_wall_north_of_house"
        elif backyardchoice == "south" or backyardchoice == "s":
            location = "inside_house"
        else:
            print("Try another input")
    
    # Forest Mouth
    elif location == "forest_mouth":
        print("You stand at the mouth of a forest full of trees and vines. The foliage is so densely packed that it would be near impossible to pass through. You can head north to where you began, or continue south and press into the forest.")
        forestmouthchoice = input("Where will you go? ")
        if forestmouthchoice == "north" or forestmouthchoice == "n":
            location = "start"
        elif forestmouthchoice == "south" or forestmouthchoice == "s":
            location = "forest_death_clearing"
        else:
            print("Try another input")
    
    # Forest Death Clearing
    elif location == "forest_death_clearing":
        print("You enter a clearing in the forest. The woods around you are covered in sinewy vines that sway in the wind.")
        forestdeathclearingchoice = input("Your vision goes dark as vines wrap around your throat. Would you like to restart? ")
        if forestdeathclearingchoice == "yes" or forestdeathclearingchoice == "y":
            location = "start"
        else:
            print("Too bad")
            location = "start"
    
    # Dirt road to the east
    elif location == "dirt_road_east":
        print("You walk down a worn dirt road that is damp, despite there being no moisture anywhere else. It leads you to a crossroads branching to the north and south as well as continuing east after 20 minutes of walking. Will you go west to where you began, north, south, or east?")
        dirtroadchoice = input("Where will you go? ")
        if dirtroadchoice == "n" or dirtroadchoice == "north":
            location = "forest_wall_north_dirt_road"
        elif dirtroadchoice == "s" or dirtroadchoice == "south":
            location = "forest_wall_south_dirt_road"
        elif dirtroadchoice == "w" or dirtroadchoice == "west":
            location = "start"
        elif dirtroadchoice == "e" or dirtroadchoice == "east":
            location = "outside_barn"
    
    # Forest wall north of the dirt road
    elif location == "forest_wall_north_dirt_road":
        print("You stand before a solid wall of foliage, its leaves and vines block any thoughts of attempted passage.")
        forestwallnorthdirtroadchoice = input("Would you like to go back? ")
        if forestwallnorthdirtroadchoice == "y" or forestwallnorthdirtroadchoice == "yes":
            location = "dirt_road_east"
        else:
            print("Too bad")
            location = "dirt_road_east"
        
    # Forest wall south of the dirt road
    elif location == "forest_wall_south_dirt_road":
        print("You stand before a solid wall of foliage, its leaves and vines block any thoughts of attempted passage.")
        forestwallsouthdirtroadchoice = input("Would you like to go back? ")
        if forestwallsouthdirtroadchoice == "y" or forestwallsouthdirtroadchoice == "yes":
            location = "dirt_road_east"
        else:
            print("Too bad")
            location = "dirt_road_east"
    
    # Outside the barn
    elif location == "outside_barn":
        print("You stand outside a worn down barn, its gates lie open and splintered in places. A trail of moldy smelling air leads to the inside.")
        outsidebarnchoice = input("Where will you go? ")
        if outsidebarnchoice == "e" or outsidebarnchoice == "east":
            location = "inside_barn"
        elif outsidebarnchoice == "w" or outsidebarnchoice == "west":
            location = "dirt_road_east"
        else:
            print("Invalid input")
    
    # Inside the barn
    elif location == "inside_barn":
        print("The inside of the barn is in a state of disrepair. Straw appears to have been sprayed onto every wall, and in the center of the barn there is a small crater. Colourful mold grows in the crater. Vines and foliage have taken over the east wall.")
        insidebarnchoice = input("Go back outside? ")
        if insidebarnchoice == "y" or insidebarnchoice == "yes":
            location = "outside_barn"
        else:
            print("Too bad")
            location = "outside_barn"
    else:
        print("something is wrong, check ur code")