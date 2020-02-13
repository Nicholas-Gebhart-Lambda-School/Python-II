from room import Room
import sys
from player import Player

# Declare all the ROOMs

ROOM = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#


def input_options():
    """
    Prints game opions
    """

    print("""
=============== HELP ME ===============
==      Use [n, s, e ,w ] to move    ==
==         Press q to quit           ==
==      Press h for this menu        ==
=======================================
    """)


VIABLE = ["n", "s", "e", "w", "h", "q"]


def main():
    """
    Initialize game state
    """

    # Make a new player object that is currently in the 'outside' ROOM.
    player = Player("Nicholas", ROOM['outside'])
# Write a loop that:

    while True:
        print(player.current_room.name)
        print(player.current_room.description)
        result = input("Where would you like to go? [n/s/e/w] ").lower()

        if result in VIABLE:
            if result == "h":
                input_options()
            if result == "q":
                print('\nGoodbye!\n')
                sys.exit()
        else:
            print("""
=============== WARNING ===============
==    That is not a real command!    ==
==         Press h for help          ==
=======================================
""")


# * Prints the current ROOM name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the ROOM there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
if __name__ == "__main__":
    main()
