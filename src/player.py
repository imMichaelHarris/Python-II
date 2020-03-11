# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, currentRoom = None):
        self.name = name
        self.currentRoom = currentRoom

    
    def move(self, direction):
        # self.currentRoom = self.currentRoom.
        direction = direction.lower()
        if direction == "n" and self.currentRoom.n_to is not None:
            self.currentRoom = self.currentRoom.n_to
        elif direction == "s"  and self.currentRoom.s_to is not None:
            self.currentRoom = self.currentRoom.s_to 
        elif direction == "e"  and self.currentRoom.e_to is not None:
            self.currentRoom = self.currentRoom.e_to 
        elif direction == "w"  and self.currentRoom.w_to is not None:
            self.currentRoom = self.currentRoom.w_to
        else:
            return False 