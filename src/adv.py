from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Bat", "Hits hard"),Item("Flamethrower", "Burns stuff")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Tennis Ball", "Fun to throw")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
# room["outside"].add_item_to_room(Item("Bat", "Hits hard"))
# room["outside"].add_item_to_room(Item("Flamethrower", "Burns stuff"))
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
player = Player("Michael")
player.currentRoom = room["outside"]
print("Welcome to Adventure Game!")
print(f"You are currently in {player.currentRoom}")
valid_directions = ["n", "s", "e", "w "]
while True:
    print(f"")
    user_input = input("Enter your command: ")
    if user_input.lower() == "q":
        exit()
    answer = player.move(user_input)
    if answer is False:
        print(f"You cannot move in the direction!")
    else:
        print(f"You are now in {player.currentRoom} Items: {player.currentRoom.items}")
    if len(player.currentRoom.items) > 0:
        print(f"There are items here in {player.currentRoom.name}")
        print("Which items would you like to pick up")
        for item in player.currentRoom.items:
            print(f"")
        item_choice = input(f"Which items")

