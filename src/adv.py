from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f'Current room: {player.room.name}')
    print(f'Room description: {player.room.description}')
    user_input = input('Pick a direction to go: ')

    if user_input == "q" or user_input == 'quit' or user_input == 'exit':
        print("THANK YOU FOR PLAYING!")
        break
    elif user_input == "n" or user_input == 'north':
        # if current room has .n_to then:
        # player.room = current room.n_to
        # else print that direction doesnt exist
        if hasattr(player.room, 'n_to'):
            print(f'You move north to: {player.room.n_to.name}')
            player.room = player.room.n_to
            print('\n')
        else:
            print(f"You cannot go north from here.")
            print('\n')
    elif user_input == "e" or user_input == 'east':
        if hasattr(player.room, 'e_to'):
            print(f'You move east to: {player.room.e_to.name}')
            player.room = player.room.e_to
            print('\n')
        else:
            print(f"You cannot go east from here.")
            print('\n')
    elif user_input == "s" or user_input == 'south':
        if hasattr(player.room, 's_to'):
            print(f'You move south to: {player.room.s_to.name}')
            player.room = player.room.s_to
            print('\n')
        else:
            print(f"You cannot go south from here.")
            print('\n')
    elif user_input == "w" or user_input == 'west':
        if hasattr(player.room, 'w_to'):
            print(f'You move west to: {player.room.w_to.name}')
            player.room = player.room.w_to
            print('\n')
        else:
            print(f"You cannot go west from here.")
            print('\n')
    else:
        print(f"Invalid input. To quit, enter 'q'. To choose a direction to proceed, enter: n,e,s, or w")
        print('\n')

