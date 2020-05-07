from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "A campfire blazes next to your camp. North of you, the cave mouth beckons."),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run in every direction."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. In the back of the room, you notice a groove in the wall that is in the shape of an octagon. The only exit is to the south."),

    'storage': Room("Storage Room", "This room seems to have been used to store all sorts of items. The only exit is to the east.", [Item('cup','A small bowl-shaped container for drinking from.'), Item('bowl','A round, deep dish or basin used for food or liquid.'), Item('box','A square, wooden container with a flat base and sides. Hidden inside, you find an octagonal jewel and put it into your inventory.'), Item('torch','A portable means of illumination consisting of cloth soaked in oil, attached to the end of a pole. Currently not lit.')]),

    'true_treasure': Room("Hidden Treasure Chamber", "The true treasure room hidden behind a false treasure room. Gold and jewels adorn every inch of the room.", [Item('coins','Round pieces of gold, used as currency.'), Item('chalice','A large, golden, jewel-adorned cup.'), Item('diamonds','Precious stones consisting of a clear and colorless crystalline.'), Item('rubies','Precious stones consisting of an intense purplish-red color.')])

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['storage']
room['storage'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [Item('compass','An instrument used for navigation and orientation.')], name=input("Enter your character's name: "))

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
print("********************************** INSTRUCTIONS **********************************")
print("To quit the game, enter 'q', 'quit', or 'exit'")
print("To go to the next room, enter 'n','e','s', or 'w'")
print("To take an item in a room, enter 'get' or 'take' followed by the item's name. Example: 'get sword'")
print("To drop an item you are holding, enter 'drop' followed by the item's name. Example: 'drop sword'")
print("To examine an item in your inventory or in the room, enter 'examine' followed by the item's name. Example: 'examine sword'")
print("To use an item in your inventory, enter 'use' followed by the item's name. Example 'use sword'")
print("To check your inventory, enter 'i' or 'inventory'")
print("If you forget what to do next, enter 'h' or 'help' for more information.")
print("********************************** INSTRUCTIONS **********************************")
print('\n')

print(f"Welcome to your python treasure-hunting adventure, {player.name}!")
quit = "false"
treasure_found = False
jewel_found = False
has_torch = False
torch_lit = False
true_treasure_has_torch = False
while quit != "true":
    for current_room in room:
        if room[current_room].name == player.room.name:
            print(f'{player.name} is currently in room: {player.room.name}')
            print(f'{player.room.description}')
            print(f'In the current room, you see the following items: {room[current_room].item_names}')

            user_input = input(f"What will {player.name} do next? ")

            if len(user_input.split()) == 1:
                if user_input == "q" or user_input == 'quit' or user_input == 'exit':
                    print('\n')
                    print('*********************************************')
                    if treasure_found == True:
                        print("Congratulations! You found the hidden treasure!")
                    elif jewel_found == True:
                        print("You did not find the hidden treasure this time, but you did find the hidden jewel.")
                    else:
                        print("You did not find the hidden treasure this time.")
                    print("THANK YOU FOR PLAYING!")
                    print('*********************************************')
                    print('\n')
                    quit = "true"
                    break
                elif user_input == "help" or user_input == "h":
                    print('\n')
                    print('**************************************** HELP MENU *********************************************')
                    print("To quit the game, enter 'q', 'quit', or 'exit'")
                    print("To go to the next room, enter 'n','e','s', or 'w'")
                    print("To take an item from a room, enter 'get' or 'take' followed by the item's name. Example: 'get sword'")
                    print("To drop an item from your inventory, enter 'drop' followed by the item's name. Example: 'drop sword'")
                    print("To examine an item in your inventory or in the room, enter 'examine' followed by the item's name. Example: 'examine sword'")
                    print("To use an item in your inventory, enter 'use' followed by the item's name. Example 'use sword'")
                    print("To see a list of items in your inventory, enter 'i' or 'inventory'")
                    print('**************************************** HELP MENU *********************************************')
                    print('\n')
                elif user_input == "i" or user_input == "inventory":
                    print('\n')
                    print(f"******************* {player.name}'s inventory ***********************")
                    if len(player.items) == 0:
                        print(f"Empty")
                    else:
                        for item in player.items:
                            print(item.name)
                            # print(f"{item.name}")
                    print(f"******************* {player.name}'s inventory ***********************")
                    print('\n')
                elif user_input == "n" or user_input == 'north':
                    if hasattr(player.room, 'n_to'):
                        hidden_room_found = False
                        for this_room in room:
                            if this_room == 'treasure' and current_room == 'treasure':
                                hidden_room_found = True
                                if has_torch == True and torch_lit == True:
                                    print('\n')
                                    print('*******************************************')
                                    print(f'{player.name} moves north to: {player.room.n_to.name}')
                                    print('*******************************************')
                                    player.room = player.room.n_to
                                    treasure_found = True
                                    print('\n')
                                elif torch_lit == True and true_treasure_has_torch == True:
                                    print('\n')
                                    print('*******************************************')
                                    print(f'{player.name} moves north to: {player.room.n_to.name}')
                                    print('*******************************************')
                                    player.room = player.room.n_to
                                    treasure_found = True
                                    print('\n')
                                else:
                                    print('\n')
                                    print('*******************************************')
                                    print(f'The hidden passageway leads to a room that is pitch black. You dare not enter the darkness.')
                                    print('*******************************************')
                                    print('\n')
                                break
                        if hidden_room_found == False:
                            print('\n')
                            print('*******************************************')
                            print(f'{player.name} moves north to: {player.room.n_to.name}')
                            print('*******************************************')
                            player.room = player.room.n_to
                            print('\n')
                    else:
                        print('\n')
                        print('*********************************')
                        print(f"{player.name} cannot go north from {room[current_room].name}.")
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
                        print(f"{player.name} cannot go east from {room[current_room].name}.")
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
                        print(f"{player.name} cannot go south from {room[current_room].name}.")
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
                        print(f"{player.name} cannot go west from {room[current_room].name}.")
                        print('********************************')
                        print('\n')
                else:
                    print('\n')
                    print('********************************')
                    print(f"'{user_input}' is not a valid input. To quit, enter 'q'. To continue, choose an action. Enter 'h' for more information.")
                    print('********************************')
                    print('\n')
            elif len(user_input.split()) == 2:
                split_user_input = user_input.split()
                if split_user_input[0] == 'get' or split_user_input[0] == 'take':
                    item_found = False
                    for item in room[current_room].items:
                        if item.name == split_user_input[1]:
                            item_found = True
                            player.items.append(item)
                            room[current_room].items.remove(item)
                            room[current_room].item_names.remove(item.name)
                            if item.name == 'torch':
                                has_torch = True
                            if current_room == "true_treasure" and item.name == 'torch':
                                true_treasure_has_torch = False
                            print('\n')
                            print('********************************')
                            print(f"{player.name} put the {item.name} into their inventory.")
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
                        if item.name == split_user_input[1]:
                            item_found = True
                            if item.name == 'torch':
                                has_torch = False
                            if current_room == "treasure":
                                room[current_room].description = "Recently rediscovered, in the past the treasure chamber held hidden treasure. The only exit is to the south."
                            if current_room == "true_treasure" and item.name == 'torch':
                                true_treasure_has_torch = True
                            player.items.remove(item)
                            room[current_room].items.append(item)
                            room[current_room].item_names.append(item.name)
                            print('\n')
                            print('********************************')
                            print(f"{player.name} removed the {item.name} from their inventory and left it in the {room[current_room].name}.")
                            print('********************************')
                            print('\n')
                    if item_found != True:
                        print('\n')
                        print('********************************')
                        print(f"'{split_user_input[1]}' is not an item in {player.name}'s inventory.'")
                        print('********************************')
                        print('\n')
                elif split_user_input[0] == 'examine':
                    item_found = False
                    for item in player.items:
                        if split_user_input[1] == 'box' and item.name == 'box' and jewel_found == False:
                            print('\n')
                            print('********************************')
                            print(f"{player.name} examines the {item.name}...{item.description}")
                            print('********************************')
                            print('\n')
                            jewel_found = True
                            item_found = True
                            player.items.append(Item('jewel','An octagonal, blood-red jewel. It seems extremely valuable.'))
                            item.description = "A square, wooden container with a flat base and sides. Nothing seems to be inside."
                        elif item.name == split_user_input[1]:
                            item_found = True
                            print('\n')
                            print('********************************')
                            print(f"{player.name} examines the {item.name}...{item.description}")
                            print('********************************')
                            print('\n')
                    for item in room[current_room].items:
                        if split_user_input[1] == 'box' and item.name == 'box' and jewel_found == False:
                            print('\n')
                            print('********************************')
                            print(f"{player.name} examines the {item.name}...{item.description}")
                            print('********************************')
                            print('\n')
                            jewel_found = True
                            item_found = True
                            player.items.append(Item('jewel','An octagonal, blood-red jewel. It seems extremely valuable.'))
                            item.description = "A square, wooden container with a flat base and sides. Nothing seems to be inside."
                        elif item.name == split_user_input[1]:
                            item_found = True
                            print('\n')
                            print('********************************')
                            print(f"{player.name} examines the {item.name}...{item.description}")
                            print('********************************')
                            print('\n')
                    if item_found != True:
                        print('\n')
                        print('********************************')
                        print(f"'{split_user_input[1]}' is not an item in {player.name}'s inventory or an item in the room.'")
                        print('********************************')
                        print('\n')
                elif split_user_input[0] == 'use':
                    item_found = False
                    for item in player.items:
                        if split_user_input[1] == item.name:
                            item_found = True
                            if item.name == 'jewel' and split_user_input[1] == "jewel" and jewel_found == True and current_room == 'treasure':
                                print('\n')
                                print('********************************')
                                print(f"{player.name} carefully places the {item.name} into the groove in the back of the room. The room shakes as a hidden passageway in the north of the room opens.")
                                print('********************************')
                                print('\n')
                                player.items.remove(item)
                                room['treasure'].n_to = room['true_treasure']
                                room['true_treasure'].s_to =  room['treasure']
                                room[current_room].description = "Recently rediscovered, the treasure chamber holds hidden treasures. The exit is to the south, but you also spot a hidden passageway in north of the room."
                            elif item.name == 'torch' and split_user_input[1] == 'torch' and has_torch == True and current_room == 'outside':
                                torch_lit = True
                                item.description = "A portable means of illumination. It currently blazes brightly and even can light up a dark room."
                                print('\n')
                                print('********************************')
                                print(f"{player.name} lights the {item.name} using the campfire. The torch blazes brightly.")
                                print('********************************')
                                print('\n')
                            else:
                                print('\n')
                                print('********************************')
                                print(f"{player.name} tried to use the {split_user_input[1]} but nothing happened.")
                                print('********************************')
                                print('\n')
                    if item_found != True:
                        print('\n')
                        print('********************************')
                        print(f"'{split_user_input[1]}' is not an item in {player.name}'s inventory.'")
                        print('********************************')
                        print('\n')
                else:
                    print('\n')
                    print('********************************')
                    print(f"'{split_user_input[0]}' is not a possible action.")
                    print('********************************')
                    print('\n')


