import classes_and_functions.get_input as g
from txt_managers.item_manager import ItemManager


class TableObject:
    """A class to represent real-world items placed on the lazy susan."""

    def __init__(self, name, parent_susan):
        self.name = name
        self.position = g.get(
            f"What is the position of {self.name}? ")
        self.parent_susan = parent_susan

        self.used(name, list_items=False)  # Enable, but
        # don't list items

    # Goto turns table so that the chosen item is facing the chosen person
    def goto(self, mod):
        print(f"Going to {self.name}.")  # Say where the table should go

        turn = (int(self.position) - int(
            mod)) - self.parent_susan.current_position  # Calculate turn
        self.parent_susan.turn(turn)

    def used(self, new_name, list_items=True):  # This
        # function enables the item
        self.parent_susan.objects[self.name] = self  # Enable in objects
        # dictionary
        self.position = int(g.get(f"What is the position of {self.name}?"))
        # Set new position of item
        self.name = new_name
        if list_items:
            self.parent_susan.list_items()  # Print updated table items
        ItemManager().add_item(str(self.name), int(self.position))

    def unused(self):  # This function disables the item
        try:
            del self.parent_susan.objects[self.name]  # Disable in objects
            # dictionary
        except KeyError:
            pass
        self.parent_susan.list_items()  # Print updated table items
        ItemManager().remove_item(self.name)
