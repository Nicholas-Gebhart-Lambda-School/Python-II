import sys
from room import Room
from player import Player
from item import Item

# Declare all the ROOMs

LONG_SWORD = Item('sword', 'stick them with the pointy end')
ROCK = Item('rock', 'this could be useful, I suppose...')

ROOM = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [LONG_SWORD, ROCK]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [ROCK]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link ROOMs together

ROOM['outside'].n_to = ROOM['foyer']
ROOM['foyer'].s_to = ROOM['outside']
ROOM['foyer'].n_to = ROOM['overlook']
ROOM['foyer'].e_to = ROOM['narrow']
ROOM['overlook'].s_to = ROOM['foyer']
ROOM['narrow'].w_to = ROOM['foyer']
ROOM['narrow'].n_to = ROOM['treasure']
ROOM['treasure'].s_to = ROOM['narrow']

# Output
WARNING = """
=============== WARNING ===============
==    That is not a real command!    ==
==         Press h for help          ==
=======================================
"""

OPTIONS = """
=============== HELP ME ===============
==      Use [n, s, e ,w ] to move    ==
== Use [yoink, show, drop] for items ==
==         Press q to quit           ==
==      Press h for this menu        ==
=======================================
"""

VIABLE = ["n", "s", "e", "w", "h", "q", "yoink", "show", "drop"]
DIRECTIONS = ["n", "s", "e", "w"]

#
# Main
#


def main():
    """
    Initialize game state
    """

    # Make a new player object that is currently in the 'outside' ROOM.
    player = Player(input('What is your name? '), ROOM['outside'], [])
# Write a loop that:

    while True:
        print("")
        print(player.current_room.name)
        print(player.current_room.description)
        print(player.current_room.list_items())
        result = input(
            "What would you like to do? ").lower().split()

        if result[0] in VIABLE:
            if result[0] in DIRECTIONS:
                player.travel(result[0])
            if result[0] == "yoink":
                player.pickup(result[1])
            if result[0] == "drop":
                player.drop(result[1])
            if result[0] == "show":
                player.list_inventory()
            if result[0] == "h":
                print(OPTIONS)
            if result[0] == "q":
                print(
                    f"\nQuitting Adventure, {player.name}. You'll a coward!\n")
                sys.exit()
        else:
            print(WARNING)


# * Prints the current ROOM name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the ROOM there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
if __name__ == "__main__":
    main()
