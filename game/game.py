class Room:
    def __init__(self, name, desc, hidden_desc, exits, is_game_over = False):
        self.name = name
        self.desc = desc
        self.hidden_desc = hidden_desc
        self.exits = exits
        self.is_game_over = is_game_over
    
    def get_exit(self, direction):
        return self.exits.get(direction)
    
    def get_exit_directions(self):
        return list(self.exits.keys())
        


    # Write hidden descriptions!
rooms = {
    "start": Room(
        "start",
        "You find yourself standing in an open field. To the north is a house. To the east is a long dirt road. To the south is a forest too dense to pass through. To the west is a hill with only one tree atop it.",
        "",
        {
            "north": "outside_house",
            "east": "dirt_road",
            "south": "forest_mouth",
            "west": "tree_hill"
        }
    ),
    "tree_hill": Room(
        "tree hill", 
        "You climb to the top of the hill where you find a mighty oak tree. There are lanterns hanging from the branches, giving off an eerie green light. There is a plaque on the tree that marks the final resting place of one Jeffrey Greenly. You can travel west past the hill or east back to where you began.",
         "",
        {
            "east": "start",
            "west": "well_hill"
        }
    ), 
    "well_hill": Room(
        "well hill",
        "You climb up a short hill topped with a decrepit old well. The bucket has broken off the rope and lies at the bottom amidst rotting bones. The smells seem to be of seawater and sulfur.", 
        "", 
        {
            "west": "forest_middle_west",
            "east": "tree_hill"
        }
    ), 
    "forest_middle_west": Room(
        "forest middle west", 
        "You come to a wall of foliage that blocks your path. You think you can see movement beyond the leaves and vines, but there is no possible passage through.", 
        "",
        {
            "east": "well_hill"
        } 
    ), 
    "outside_house": Room(
        "outside house", 
        "The house is small but cozy-looking. The walls are overgrown with vines, giving a feeling that it has been abandoned for some time, but the two lanterns hanging in the doorway are still alight.", 
        "",
        {
            "north": "inside_house", 
            "south": "start"
        } 
    ), 
    "inside_house": Room(
        "inside house", 
        "The inside of the house appears ransacked, with books and furniture haphazardly thrown everywhere. When you look closely, you see a thin line of silver in all of the windowframes.", 
        "",
        {
            "north": "backyard", 
            "south": "outside_house", 
            "west": "basement"
        } 
    ), 
    "basement": Room(
        "basement", 
        "You walk down the creaky set of stairs to the basement. There are a few chairs on a stone floor. To the north, there is a hole in the wall leading to a damp, dimly lit cave. You can enter the cave or go back to the main floor of the house to the east.", 
        "",
        {
            "east": "inside_house", 
            "north": "cave_entrance", 
        } 
    ), 
    "cave_entrance": Room(
        "cave entrance", 
        "You stand in the entrance to a dripping cave,the stone pathway branching in front of you to go deeper underground to the north and towards the surface to the west.", 
        "",
        {
            "south": "basement",
            "west": "cave_west_to_hill", 
            "north": "cave_crossroads"
        } 
    ), 
    "cave_crossroads": Room(
        "cave crossroads", 
        "Your path branches again, showing a steel door to the west and a path to to the surface to the east. In front of you is a rough rock wall.", 
        "", 
        {
            "south": "cave_entrance", 
            "west": "ritual_chamber",
            "east": "forest_wall_north_of_house"
        }
    ), 
    "ritual_chamber": Room(
        "ritual chamber", 
        "As you enter this room, the steel door locks behind you. You see strange markings on the wall that appear to be written in blood. On the far west side of the room, there is a deep pool of water. As you look closer, a slimy tentacled beast crawls up from the depths. Your vision goes black.", 
        "",
        {
            "y": "start"
        },
        True
    ), 
    "forest_wall_north_of_house": Room(
        "forest wall north of house", 
        "You stare into a solid wall of foliage. There is no way of entering the forest from here. You can go south to the backyard from here or west to a cave system.", 
        "", 
        {
            "south": "backyard",
            "west": "cave_crossroads"
        }
    ), 
    "backyard": Room(
        "backyard", 
        "You stand behind the house in a small fenced area populated only by a small tree and three gravestones. They read(from left to right) Roseanne Tyler-Greenly, Ashleigh Greenly, and Jessie Greenly. You can continue north to the wall of the forest, or back to where you came from.", 
        "", 
        {
            "north": "forest_wall_north_of_house",
            "south": "inside_house"
        }
    ),
    "forest_mouth": Room(
        "forest mouth", 
        "You stand at the mouth of a forest full of trees and vines. The foliage is so densely packed that it would be near impossible to pass through. You can head north to where you began, or continue south and press into the forest.", 
        "",
        {
            "north": "start",
            "south": "forest_death_clearing"
        } 
    ),
    "forest_death_clearing": Room(
        "forest death clearing", 
        "You enter a clearing in the forest. The woods around you are covered in sinewy vines that sway in the wind. Your vision goes dark as vines wrap around your throat.", 
        "",
        {
            "y": "start"
        },
        True
    ), 
    "dirt_road_east": Room(
        "dirt road east", 
        "You walk down a worn dirt road that is damp, despite there being no moisture anywhere else. It leads you to a crossroads branching to the north and south as well as continuing east after 20 minutes of walking. Will you go west to where you began, north, south, or east?", 
        "", 
        {
            "north": "forest_wall_north_dirt_road",
            "south": "forest_wall_south_dirt_road",
            "west": "start",
            "east": "outside_barn"
        }
    ), 
    "forest_wall_north_dirt_road": Room(
        "forest wall north of dirt road", 
        "You stand before a solid wall of foliage, its leaves and vines block any thoughts of attempted passage.", 
        "",
        {
            "south": "dirt_road_east"
        } 
    ), 
    "forest_wall_south_dirt_road": Room(
        "forest wall south of dirt road", 
        "You stand before a solid wall of foliage, its leaves and vines block any thoughts of attempted passage.", 
        "", 
        {
            "north": "dirt_road_east"
        }
    ), 
    "outside_barn": Room(
        "outside barn", 
        "You stand outside a worn down barn, its gates lie open and splintered in places. A trail of moldy smelling air leads to the inside.", 
        "",
        {
            "east": "inside_barn",
            "west": "dirt_road_east"
        } 
    ), 
    "inside_barn": Room(
        "inside barn", 
        "The inside of the barn is in a state of disrepair. Straw appears to have been sprayed onto every wall, and in the center of the barn there is a small crater. Colourful mold grows in the crater. Vines and foliage have taken over the east wall.", 
        "", 
        {
            "west": "outside_barn"
        }
    ),
    }