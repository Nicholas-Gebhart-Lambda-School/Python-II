# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """
    Adventure Room!
    """

    def __init__(self, name, description, items):
        self.name = name
        self.description = description

        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name}, {self.description}, {self.items}"

    def list_items(self):
        """
        List all the items inside of the room
        """
        if len(self.items) > 0:
            print("In the room you find:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}")
            return ""
        print('There are no items here')
        return ""
