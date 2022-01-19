import classes_and_functions.func_get_input as g
from txt_managers.manager_items import ItemManager


class TableObject:
    """A class to represent real-world items placed on the lazy susan."""
    def __init__(self, name, parent_susan, emulator, position=int(0)):
        self.name = name
        self.emulator = emulator
        self.position = g.get(f"What is the position of {self.name}? ",
                              self.emulator)
        self.parent_susan = parent_susan

        self.used(name, parent_susan, list_items=False)  # Enable, but
        # don't list items
        self.position = position

    # Goto turns table so that the chosen item is facing the chosen person
    def goto(self, mod):
        self.emulator.out.print_this(f"Going to {self.name}.")
        # Say where the table should go

        turn = (int(self.position) + int(
            mod)) - self.parent_susan.current_position  # Calculate turn
        if "-" in str(turn):  # Deal with negative turns
            turn_is_negative = True
            new_turn = ""
            for character in str(turn):
                if character != "-":
                    new_turn = new_turn + character
            turn = new_turn
        else:
            turn_is_negative = False
        turn = int(turn)
        if turn_is_negative:
            self.parent_susan.current_position = int(
                self.parent_susan.current_position - int(
                    turn))  # Update position var
        else:
            self.parent_susan.current_position = int(self.parent_susan.
                                                     current_position + int(
                                                      turn))  # Update pos var

        # Deal with turns > 360˚ and < -360˚
        while self.parent_susan.current_position >= 360:
            self.parent_susan.current_position -= 360
        while self.parent_susan.current_position < -360:
            self.parent_susan.current_position += 360
        # The following converts turns greater than 180 into negative numbers
        # E.g. 260 turn becomes -100 turn
        if int(turn) > 180:
            turn = (360 - int(turn)) * -1
        if turn_is_negative:
            # Print the turn as anticlockwise
            self.emulator.out.print_this(
                f"The table turned {turn} anticlockwise.")
        elif turn == 0:  # i.e. table is already in correct position
            self.emulator.out.print_this("The table did not move.")
        else:
            # Print the turn as clockwise
            self.emulator.out.print_this(f"The table turned {turn} clockwise.")

        self.parent_susan.print_current_position()  # Show the table's
        # updated position

    def used(self, new_name, parent_susan, list_items=True):  # This
        # function enables the item
        self.parent_susan.objects[self.name] = self  # Enable in objects
        # dictionary
        self.position = parent_susan.current_position  # Set new
        # position of item
        self.name = new_name
        if list_items:
            self.parent_susan.list_items()  # Print updated table items
        ItemManager(self.emulator).add_item(str(self.name), int(self.position))

    def unused(self):  # This function disables the item
        del self.parent_susan.objects[self.name]  # Disable in objects
        # dictionary
        self.parent_susan.list_items()  # Print updated table items
        ItemManager(self.emulator).remove_item(self.name)
