# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        # 1) Adding these as attributes in the constructor is optional;
        # in python you can arbitrarily set attributes on instances
        # 2) the `: Room` syntax is a typehint. It just serves as a reminder
        # for other developers that self.n_to is storing a Room object (as opposed to a str)
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

    def remove_item(self, item):
        del self.item[item]

    def add_item(self, item):
        self.item.append(item)
