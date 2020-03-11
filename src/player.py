# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, currentRoom = None):
        self.name = name
        self.currentRoom = currentRoom

    
    def move(self, direction):
        if direction == "n":
            self.currentRoom = self.currentRoom.n_to
        elif direction == "s":
            self.currentRoom = self.currentRoom.s_to 
        elif direction == "e":
            self.currentRoom = self.currentRoom.e_to 
        elif direction == "w":
            self.currentRoom = self.currentRoom.w_to  