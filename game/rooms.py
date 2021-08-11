from .room import Room
from .portal import Portal, LockedPortal, WinPortal, ClearingWinPortal

    # Write hidden descriptions!
rooms = {
    "start": Room(
        "start",
        "You find yourself standing in an open field. To the north is a house. To the east is a long dirt road. To the south is a forest too dense to pass through. To the west is a hill with only one tree atop it.",
        {
            "north": Portal("outside_house"),
            "east": Portal("dirt_road_east"),
            "south": Portal("forest_mouth"),
            "west": Portal("tree_hill")
        }, 
        objects = ["grass"]
    ),
    "tree_hill": Room(
        "tree hill", 
        "You climb to the top of the hill where you find a mighty oak tree. There are lanterns hanging from the branches, giving off an eerie green light. There is a plaque on the tree that marks the final resting place of one Jeffrey Green. To the east is an open grass field. To the west is a hill with a small structure on it.",
        {
            "east": Portal("start"),
            "west": Portal("well_hill")
        }, 
        objects = ["twig", "oak leaf"]
    ), 
    "well_hill": Room(
        "well hill",
        "You climb up a short hill topped with a decrepit old well. The bucket has broken off the rope and lies at the bottom amidst rotting bones. The smells seem to be of seawater and sulfur. To the west, the forest begins with a dense wall of green. To the east is a hill with a tall tree atop it.", 
        {
            "west": Portal("forest_middle_west"),
            "east": Portal("tree_hill")
        },
        objects = ["house key", "old skull", "moldy blindfold"],
    ), 
    "forest_middle_west": Room(
        "forest middle west", 
        "You come to a wall of foliage that blocks your path. You think you can see movement beyond the leaves and vines, but there is no possible passage through. To the east is a hill with a small structure on it.", 
        {
            "east": Portal("well_hill")
        },
        objects = [] 
    ), 
    "outside_house": Room(
        "outside house", 
        "The house is small but cozy-looking. The walls are overgrown with vines, giving a feeling that it has been abandoned for some time, but the two lanterns hanging in the doorway are still alight. To the south is an open grass field. To the north is the inside of the house.", 
        {
            "north": LockedPortal(
                "inside_house", 
                "house key",
                blocked_message = "This door is locked. Maybe someone left a house key somewhere?",
                pass_message = "You twist the house key in the lock, and the door creaks open. The sound echoes through the house.",
            ), 
            "south": Portal("start")
        },
        objects = ["rusty key"] 
    ), 
    "inside_house": Room(
        "inside house", 
        "The inside of the house appears ransacked, with books and furniture haphazardly thrown everywhere. When you look closely, you see a thin line of silver in all of the windowframes. To the north, the house exits to the backyard. To the south, the house exits to the front yard. To the west, a door and stairs lead to the basement.", 
        {
            "north": Portal("backyard"), 
            "south": Portal("outside_house"), 
            "west": LockedPortal(
                "basement",
                "wooden key",
                blocked_message = "This door is locked. You can see splinters in the keyhole. Surely there's a key somewhere, right?",
                pass_message = "You see that the wooden key fits here! You can hear the key splintering a little as you turn it in the lock, but the door opens with a satisfying click!",
            )
        },
        objects = ["ripped book", "crowbar"] 
    ), 
    "basement": Room(
        "basement", 
        "You walk down the creaky set of stairs to the basement. There are a few chairs on a stone floor. To the north, there is a hole in the wall leading to a damp, dimly lit cave. You can enter the cave to the north or go back to the main floor of the house to the east.", 
        {
            "east": Portal(
                "inside_house",
                pass_message = "You unlatch the door and walk through, but you slip and it slams shut behind you. You will need the key to unlock it from this side."
                ), 
            "north": Portal("cave_entrance"), 
        },
        objects = ["chair leg", "nails", "broken board", "rope"] 
    ), 
    "cave_entrance": Room(
        "cave entrance", 
        "You stand in the entrance to a dripping cave,the stone pathway going deeper underground to the north. To the south is a hole in a wooden wall leading to a basement.", 
        {
            "south": Portal("basement"),
            "north": Portal(
                "cave_crossroads", 
                pass_message = "The path branches ahead of you."
                )
        },
        objects = ["rough stone", "road flare"] 
    ), 
    "cave_crossroads": Room(
        "cave crossroads", 
        "You see a steel door to the west and a path to to the surface to the east blocked by a stone outcrop. In front of you is a rough rock wall. To the south is a pathway that branches towards a hole in a wall in one direction and towards the surface in another.", 
        {
            "south": Portal("cave_entrance"), 
            "west": WinPortal(
                "ritual_chamber",
                "4 character passkey", 
                "road flare",
                "strange mold",
                "ritual_win_room",
                blocked_message = "There is a keypad on the door. You try to guess the code a few times, but nothing works. Maybe someone left the code lying around somewhere?",
                pass_message = "The keypad beeps, and the door swings open to reveal a small chamber.",
            ),
            "east": LockedPortal(
                "forest_wall_north_of_house", 
                "rope", 
                blocked_message = "There is a rock outcrop blocking your path. Theres a hook at the top though. If only you had something to attach there.",
                pass_message = "You attach your rope to the hook and climb up. At the top, you continue east to the surface.",
            )
        },
        objects = ["mud clump", "broken house key"]
    ), 
    "ritual_chamber": Room(
        "ritual chamber", 
        "As you enter this room, the steel door locks behind you. You see strange markings on the wall that appear to be written in blood. On the far west side of the room, there is a deep pool of water. As you look closer, a slimy tentacled beast crawls up from the depths. This creature seems to have a connection to this area. If you could find something connected to it and destroy it here, you might be able to kill the monster. Your vision goes black.", 
        {
            "y": Portal("start")
        },
        objects = [],
        is_game_over=True
    ), 
    "forest_wall_north_of_house": Room(
        "forest wall north of house", 
        "You stare into a solid wall of foliage. There is no way of entering the forest from here. To the south you see the backyard of the house, and to the west you see a cave opening.", 
        {
            "south": Portal("backyard"),
            "west": Portal(
                "cave_crossroads",
                pass_message = "You hop down what looks like a short outcrop. Upon landing and hurting your ankles, you see that it is higher than you thought."
            )
        },
        objects = ["wooden key"]
    ), 
    "backyard": Room(
        "backyard", 
        "You stand behind the house in a small fenced area populated only by a small tree and three gravestones. They read(from left to right) Roseanne Tyler-Green, Ashleigh Green, and Jessie Green. You can continue north to the wall of the forest, or south to the inside of the house.", 
        {
            "north": Portal("forest_wall_north_of_house"),
            "south": Portal("inside_house")
        },
        objects = ["charred fingerbone", "4 character passkey"]
    ),
    "forest_mouth": Room(
        "forest mouth", 
        "You stand at the mouth of a forest full of trees and vines. The foliage is so densely packed that it would be near impossible to pass through. You can head north to an open field, or continue south and press into the forest.", 
        {
            "north": Portal("start"),
            "south": ClearingWinPortal(
                "forest_death_clearing",
                "old skull",
                "charred fingerbone",
                "forest_win_room"
            )
        },
        objects = [] 
    ),
    "forest_death_clearing": Room(
        "forest death clearing", 
        "You enter a clearing in the forest. The woods around you are covered in sinewy vines that sway in the wind. Your vision goes dark as vines wrap around your throat. Before you lose consciousness, you notice a few things. First, the forest seems confused, swinging branches without wind, and reaching up to the sky. Maybe you could shock the forest out of confusion? You also see that this forest is filled with trees like the one on the hill to the west. Could there be a connection to the man there?", 
        {
            "y": Portal("start")
        },
        objects = [],
        is_game_over=True
    ), 
    "dirt_road_east": Room(
        "dirt road east", 
        "You walk down a worn dirt road that is damp, despite there being no moisture anywhere else. It leads you to a crossroads branching to the north and south as well as continuing east after 20 minutes of walking. Will you go west to where you began, east to a large barn, north to a wall of vibrant foliage, or south to a wall of decaying vines and leaves?", 
        {
            "north": Portal("forest_wall_north_dirt_road"),
            "south": Portal("forest_wall_south_dirt_road"),
            "west": Portal("start"),
            "east": Portal("outside_barn")
        },
        objects = []
    ), 
    "forest_wall_north_dirt_road": Room(
        "forest wall north of dirt road", 
        "You stand before a solid wall of foliage, its leaves and vines block any thoughts of attempted passage. To the south is a long dirt road.", 
        {
            "south": Portal("dirt_road_east")
        },
        objects = []
    ), 
    "forest_wall_south_dirt_road": Room(
        "forest wall south of dirt road", 
        "You stand before a solid wall of foliage, its leaves and vines block any thoughts of attempted passage. To the north is a long dirt road.", 
        {
            "north": Portal("dirt_road_east")
        },
        objects = []
    ), 
    "outside_barn": Room(
        "outside barn", 
        "You stand outside a worn down barn, its gates closed and splintered in places. A trail of moldy smelling air leads to the inside to the east. To the west is a long dirt road.", 
        {
            "east": LockedPortal(
                "inside_barn", 
                "crowbar",
                blocked_message = "This barn door is closed. Maybe you could pry it open if you found the right tool?",
                pass_message = "You wedge the crowbar into a crack and pull. The huge doors splinter more as you pry one open to reveal a barn that has clearly not seen use in years.",
            ),
            "west": Portal("dirt_road_east")
        }, 
        objects = ["used road flare", "broken board"] 
    ), 
    "inside_barn": Room(
        "inside barn", 
        "The inside of the barn is in a state of disrepair. Straw appears to have been sprayed onto every wall, and in the center of the barn there is a small crater. Colourful mold grows in the crater. Vines and foliage have taken over the east wall. To the west is the door to the outside of the barn.", 
        {
            "west": Portal("outside_barn")
        },
        objects = ["straw", "strange mold"]
    ),
    "ritual_win_room": Room(
        "ritual win room",
        "You step through the stiff doorframe into the small stone room, noticing that the bloody markings all over the walls are shaped like spirals around a hastily drawn door. A tentacled beast emerges from a pool on the side opposite you. You strike the road flare and use it to burn the mold you found in the barn, severing the creature's connection to this place. Purple lights spark to life in mid-air, swirling around the monster, sucking it into a now growing orb of light. Intrigued, you move closer, getting sucked in yourself. You are pulled in all directions at once, seeing colours you never even imagined could exist as you fall through what looks like a hallway tipped on it's side. when you reach the bottom, you see it. The door that was drawn in blood. It opens and faster than you can blink, you are pulled through. When you open your eyes, only one thought passes through your head. 'This is not earth'. Your vision goes dark.",
        {
            "y": Portal("start")
        },
        is_win_game = True
    ),
    "forest_win_room": Room(
        "forest win clearing",
        "You present the old skull and the charred fingerbone. The forest recoils in what looks like grief and shock. Vines and tress part, wilt, and disappear into the ground moving towards the great oak tree. The forest that was surrounding the farm is gone, revealing the lifeless bodies of those who came before you, a lake to the north, wilted fields to the east, and gravel roads to the south and west. As you walk away to the south, you realize that the forest was never supposed to be there. You keep walking anyway, going on to live a happy life. Or do you?",
        {
            "y": Portal("start")
        },
        is_win_game = True
    )
    }