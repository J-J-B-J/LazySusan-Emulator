raw_input = ""


def get_input(prompt = "Cancel"):  # This enables the input of text from a
    # test file
    if __name__ == '__main__':
        return_value = str(input(prompt))
    else:
        return_value = str(raw_input)
    if "Cancel" in return_value:
        return None
    return return_value


def get_modifier():  # This function returns the modifier for the specified
    # user
    modifier = get_input("Modifier? ")
    if modifier is None:
        return None
    return modifier  # Return the modifier once the user has given a valid
    # answer


# This class is for real-world objects that can be placed on the lazy susan
class TableObject:
    def __init__(self, name, parent_susan):
        # Name, Position on table, Currently on table?
        self.name = name
        self.position = 0
        self.use = False
        self.parent_susan = parent_susan

        # Add this object to the all_objects dictionary in its parent susan
        self.parent_susan.all_objects[self.name] = self

    # Goto turns table so that the chosen item is facing the chosen person
    def goto(self, mod):
        print("Going to " + self.name + ".")  # Say where the table should go

        turn = (int(self.position) + int(
            mod)) - self.parent_susan.current_position  # Calculate turn
        if "-" in str(turn):
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
                                                        turn))  # Update
            # position var
        while self.parent_susan.current_position >= 360:
            self.parent_susan.current_position = \
                self.parent_susan.current_position - 360
        while self.parent_susan.current_position < 0:
            self.parent_susan.current_position = \
                self.parent_susan.current_position + 360
        # The following converts turns greater than 180 into negative numbers
        # E.g. 260 turn becomes -100 turn
        if int(turn) > 180:
            turn = (360 - int(turn)) * -1
        if turn_is_negative:
            # Print the turn as anticlockwise
            print("The table turned " + str(turn) + " anticlockwise.")
        elif turn == 0:  # i.e. table is already in correct position
            print("The table did not move.")
        else:
            # Print the turn as clockwise
            print("The table turned " + str(turn) + " clockwise.")

        self.parent_susan.print_current_position()  # Show the table's
        # updated position

    def used(self):  # This function enables the item
        self.use = True  # Enable in object
        self.parent_susan.objects[self.name] = self  # Enable in objects
        # dictionary
        self.position = self.parent_susan.current_position  # Set new
        # position of item
        print("Position set.")
        self.parent_susan.list_items()  # Print updated table items

    def unused(self):  # This function disables the item
        self.use = False  # Disable in object
        del self.parent_susan.objects[self.name]  # Disable in objects
        # dictionary
        self.parent_susan.list_items()  # Print updated table items

    def is_used(self):  # Checks weather or not the item is enabled
        if self.use:
            return True
        return False


class LazySusan:  # Class to keep track of an emulated lazy susan
    def __init__(self, starting_position=int(0)):
        self.current_position = starting_position
        self.objects = {}
        self.all_objects = {}

    def list_items(self):
        # This function prints out all the objects in turn
        # It's used when a change to the objects' dictionary occurs
        print("\nItems on table:        *UPDATED*")
        for table_obj, ID in self.objects.items():  # For each obj & id in
            # objects
            print(" - " + table_obj)  # Print name of object in bullet point
            # format
        print("\n")

    def print_current_position(self):  # This function prints table's
        # current position
        print("The table is now in position " + str(self.current_position) +
              ".")

    def turn(self):
        turn = get_input("By how much? ")  # Get a turn amount
        if turn is None:
            print("Cancelled")
            return
        valid_turn = True
        valid_characters = (
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-")
        for character in str(turn):
            if character not in valid_characters:
                valid_turn = False

        if valid_turn:
            if "-" in str(turn):
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
                self.current_position = int(
                    self.current_position - int(turn))  # Update position var
            else:
                self.current_position = int(
                    self.current_position + int(turn))  # Update position var
            while self.current_position >= 360:
                self.current_position = self.current_position - 360
            while self.current_position < 0:
                self.current_position = self.current_position + 360
            # The following converts turns greater than 180 into negative
            # numbers. E.g. 260 turn becomes -100 turn
            if int(turn) > 180:
                turn = (360 - int(turn)) * -1
            if turn_is_negative:
                # Print the turn as anticlockwise
                print("The table turned " + str(turn) + " anticlockwise.")
            elif turn == 0:  # i.e. table is already in correct position
                print("The table did not move.")
            else:
                # Print the turn as clockwise
                print("The table turned " + str(turn) + " clockwise.")

            self.print_current_position()  # Show the table's updated position
        else:
            print("The turn you entered wasn't an integer")

    def goto(self):
        modifier = get_modifier()
        if modifier is None:
            print("Cancelled")
            return
        goto = get_input("Where to? ")  # Ask what item the
        # person wants
        if goto is None:
            print("Cancelled")
            return
        valid_answer_found = False  # The user hasn't yet provided valid answer
        for obj, goto_identifier in self.objects.items():  # Repeat w all
            # objects on table
            # If the item the user entered matches a table object
            if str(obj) == goto:
                goto_identifier.goto(modifier)  # Turn table to the table
                # object
                valid_answer_found = True
        if not valid_answer_found:
            print("You can't go to that item or modifier now.")  # Give an
            # error

    def toggle(self):
        toggle = get_input("Item to Toggle? ")  # Ask for item
        if toggle is None:
            print("Cancelled")
            return
        # Check the existence of the item (it's presence in all_objects)
        toggle_item_exists = False  # Haven't found the item yet
        toggle_identifier = ""
        for obj, identifier in self.all_objects.items():  # Repeat with all
            # items
            if str(obj) == toggle:  # If item in all_objects matches user input
                toggle_identifier = identifier  # Store the ID of the object
                toggle_item_exists = True  # The item the user asked for exists
        if not toggle_item_exists:
            print("The item you asked for doesn't exist.")
        else:
            # Toggle the item the user entered
            if toggle_identifier.is_used():  # If the item is enabled
                toggle_identifier.unused()  # Disable the item
            else:  # If the item is disabled
                toggle_identifier.used()  # Enable the item

    def edit(self):
        edit = get_input("Item to Edit? ")
        # Ask for item
        if edit is None:
            print("Cancelled")
            return
        # Check the existence of the item (it's presence in all_objects)
        edit_item_exists = False  # Haven't found the item yet
        edit_identifier = ""
        for obj, identifier in self.all_objects.items():
            if str(obj) == edit:  # If item in all_objects matches user input
                edit_identifier = identifier  # Store the ID of the object
                edit_item_exists = True  # The item the user asked for exists
        if not edit_item_exists:
            print("The item you asked for doesn't exist.")
        else:
            if edit_identifier.is_used():  # If the item is enabled
                # Set the item's position to the current position
                edit_identifier.position = self.current_position
            else:  # If the item is disabled
                edit_identifier.used()  # Enable the item


def main():
    default_susan = LazySusan()
    default_susan.print_current_position()
    # These are the objects that can be enabled:
    cutlery = TableObject("Cutlery", default_susan)
    tom_sauce = TableObject("Tomato Sauce", default_susan)
    bbq_sauce = TableObject("BBQ Sauce", default_susan)
    chilli_sauce = TableObject("Sweet Chilli Sauce", default_susan)
    salad = TableObject("Salad", default_susan)
    salt = TableObject("Salt", default_susan)
    pepper = TableObject("Pepper", default_susan)
    bible = TableObject("Bible", default_susan)
    olive_oil = TableObject("Olive Oil", default_susan)

    while True:
        # Ask what the user wants to do
        action = str(get_input("Action: "))

        if action == "Goto":  # If the user wants to turn the table:
            default_susan.goto()

        elif action == "Toggle":  # If the user wants to change the items on
            # the table
            default_susan.toggle()

        elif action == "Edit":  # Edit the position of an item
            default_susan.edit()

        # Turn the table manually, relative to seat with modifier 0
        elif action == "Turn":
            default_susan.turn()

        else:  # If the action provided isn't valid
            print("The action you entered wasn't valid")


if __name__ == '__main__':
    main()
