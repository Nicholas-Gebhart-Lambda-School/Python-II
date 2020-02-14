# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """
    Player instance
    """

    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __repr__(self):
        return f"{self.name}, {self.current_room}"

    def __str__(self):
        return f"{self.name}, {self.current_room}"

    def travel(self, direction):
        """
        Send your adventurer to another room
        """
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
        else:
            print('\nThere is nothing there, adventurerer.\n')

    def pickup(self, item):
        """
        Pick up an item from the room
        """
        for ground_item in self.current_room.items:
            if ground_item.name == item:
                self.current_room.items.remove(ground_item)
                self.inventory.append(ground_item)
                print(f"picked up {item}!")

    def drop(self, item):
        """
        Pick up an item from the room
        """
        for held_item in self.inventory:
            if held_item.name == item:
                self.current_room.items.append(held_item)
                self.inventory.remove(held_item)
                print(f"you dropped the {item}!")

    def list_inventory(self):
        """
        Show items in inventory
        """
        if len(self.inventory) > 0:
            print("You're currently carrying:")
            for item in self.inventory:
                print(f"{item.name}")
            return ""
        print('Nothing in inventory')
        return ""

