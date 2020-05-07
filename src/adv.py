from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["sword","torch"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

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
player = Player(room['outside'], ['compass'], name=input("Enter your character's name: "))

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
print('\n')
print("***********************************INSTRUCTIONS***********************************")
print("To quit the game, enter 'q', 'quit', or 'exit'")
print("To go to the next room, enter 'n','e','s', or 'w'")
print("To take an item in a room, enter 'get' or 'take' followed by the item's name. Example: 'get sword'")
print("To drop an item you are holding, enter 'drop' followed by the item's name. Example: 'drop sword'")
print("To check your inventory, enter 'i' or 'inventory'")
print("If you forget what to do next, enter 'h' or 'help' for more information.")
print("***********************************INSTRUCTIONS***********************************")
print('\n')

quit = "false"
while quit != "true":
    for current_room in room:
        if room[current_room].name == player.room.name:
            print(f'{player.name} is currently in room: {player.room.name}')
            print(f'{player.room.description}')
            print(f'In the room, you see: {room[current_room].items}')

            user_input = input(f"What will {player.name} do next? ")

            if len(user_input.split()) == 1:
                if user_input == "q" or user_input == 'quit' or user_input == 'exit':
                    print("THANK YOU FOR PLAYING!")
                    quit = "true"
                    break
                elif user_input == "help" or user_input == "h":
                    print('\n')
                    print('*****************************************HELP MENU**********************************************')
                    print("To quit the game, enter 'q', 'quit', or 'exit'")
                    print("To go to the next room, enter 'n','e','s', or 'w'")
                    print("To take an item in a room, enter 'get' or 'take' followed by the item's name. Example: 'get sword'")
                    print("To drop an item you are holding, enter 'drop' followed by the item's name. Example: 'drop sword'")
                    print("To see a list of items in your inventory, enter 'i' or 'inventory'")
                    print('*****************************************HELP MENU**********************************************')
                    print('\n')
                elif user_input == "i" or user_input == "inventory":
                    print('\n')
                    print(f"********************{player.name}'s inventory************************")
                    if len(player.items) == 0:
                        print(f"Empty")
                    else:
                        print(f"{player.items}")
                    print(f"********************{player.name}'s inventory************************")
                    print('\n')
                elif user_input == "n" or user_input == 'north':
                    if hasattr(player.room, 'n_to'):
                        print('\n')
                        print('*******************************************')
                        print(f'{player.name} moves north to: {player.room.n_to.name}')
                        print('*******************************************')
                        player.room = player.room.n_to
                        print('\n')
                    else:
                        print('\n')
                        print('*********************************')
                        print(f"{player.name} cannot go north from here.")
                        print('*********************************')
                        print('\n')
                elif user_input == "e" or user_input == 'east':
                    if hasattr(player.room, 'e_to'):
                        print('\n')
                        print('*******************************************')
                        print(f'{player.name} moves east to: {player.room.e_to.name}')
                        player.room = player.room.e_to
                        print('*******************************************')
                        print('\n')
                    else:
                        print('\n')
                        print('********************************')
                        print(f"{player.name} cannot go east from here.")
                        print('********************************')
                        print('\n')
                elif user_input == "s" or user_input == 'south':
                    if hasattr(player.room, 's_to'):
                        print('\n')
                        print('*******************************************')
                        print(f'{player.name} moves south to: {player.room.s_to.name}')
                        player.room = player.room.s_to
                        print('*******************************************')
                        print('\n')
                    else:
                        print('\n')
                        print('********************************')
                        print(f"{player.name} cannot go south from here.")
                        print('********************************')
                        print('\n')
                elif user_input == "w" or user_input == 'west':
                    if hasattr(player.room, 'w_to'):
                        print('\n')
                        print('*******************************************')
                        print(f'{player.name} moves west to: {player.room.w_to.name}')
                        player.room = player.room.w_to
                        print('*******************************************')
                        print('\n')
                    else:
                        print('\n')
                        print('********************************')
                        print(f"{player.name} cannot go west from here.")
                        print('********************************')
                        print('\n')
                else:
                    print(f"Invalid input. To quit, enter 'q'. To continue, choose an action: [get 'item'], [drop 'item'], or choose a direction to go: n,e,s, or w")
                    print('\n')
            elif len(user_input.split()) == 2:
                split_user_input = user_input.split()
                if split_user_input[0] == 'get' or split_user_input[0] == 'take':
                    item_found = False
                    for item in room[current_room].items:
                        if item == split_user_input[1]:
                            item_found = True
                            player.items.append(item)
                            room[current_room].items.remove(item)
                            print('\n')
                            print('********************************')
                            print(f"{player.name} put the {item} into their inventory.")
                            print('********************************')
                            print('\n')
                    if item_found != True:
                        print('\n')
                        print('********************************')
                        print(f"'{split_user_input[1]}' is not an item in the room.")
                        print('********************************')
                        print('\n')
                elif split_user_input[0] == 'drop':
                    item_found = False
                    for item in player.items:
                        if item == split_user_input[1]:
                            item_found = True
                            player.items.remove(item)
                            room[current_room].items.append(item)
                            print('\n')
                            print('********************************')
                            print(f"{player.name} removed the {item} from their inventory and left it in the {room[current_room].name}.")
                            print('********************************')
                            print('\n')
                    if item_found != True:
                        print('\n')
                        print('********************************')
                        print(f"'{split_user_input[1]}' is not a item in {player.name}'s inventory.'")
                        print('********************************')
                        print('\n')
                else:
                    print('\n')
                    print('********************************')
                    print(f"'{split_user_input[0]}' is not a possible action.")
                    print('********************************')
                    print('\n')


