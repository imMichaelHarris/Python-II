# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f"{self.name}"

    def add_item_to_room(self, item):
        self.items.append(item)

    def remove_item_from_room(self, item):
        self.items.remove(item)