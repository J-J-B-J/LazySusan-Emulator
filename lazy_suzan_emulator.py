items_file = 'items.txt'

raw_input = ""


def read_items(susan):
    try:
        with open(items_file, 'r') as file:  # Try to read the file
            read_data = file.readlines()
    except FileNotFoundError:  # If the file doesn't exist
        with open(items_file, 'w') as file:  # Create the file
            file.write("Items:\n")
            # Write this line at the start
        with open(items_file, 'r') as file:
            read_data = file.readlines()
    read_data = read_data[1:]  # Remove first line of file, which is "Items:"
    if not read_data:
        print("No Data Found.")
        return None
    else:
        new_read_data = []  # New read data gets set to the old read data, but
        # without the newlines at the end of each line.
        for line in read_data:
            new_read_data.append(line.rstrip("\n"))
        read_data = new_read_data
        print("Data Found!")

        restore = get_input("Do you want to restore items? ")
        while restore != "Yes" and restore != "No":  # Check for a valid answer
            restore = get_input("Invalid answer. Do you want to restore items?"
                                )
        if restore == "Yes":
            print("Item data saved!")
            lines = 0
            for line in read_data:  # Save the old data to this program
                TableObject(str(line[4:]), susan, int(line[:3]),
                            True)
                lines += 1
            return
        else:
            with open(items_file, 'w') as file:  # Clear the file
                file.write("Items:\n")
            print("Item data deleted!")
            return


def add_item(item, position):
    position = str(position)
    for _ in range(0, 3 - len(position)):
        position = "0" + str(position)  # Make positions 3-digit numbers.
        # E.g. 12 becomes 012
    position += " "  # Add a space at the end of position
    text = position + item + "\n"
    try:
        with open(items_file, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        with open(items_file, 'w') as file:
            file.write("Items:\n" + text)


def get_input(prompt="Cancel"):  # This enables the input of text from a
    # test file
    if __name__ == '__main__':  # If this is the main program, just run the
        # normal input function
        return_value = str(input(prompt))
    else:  # If in testing mode, return the input from the test program
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
    def __init__(self, name, parent_susan, position=0, use=False):
        self.name = name
        self.position = position
        self.use = use
        self.parent_susan = parent_susan

        if self.use:
            self.used(name, list_items=False)  # Enable, but don't list items
            self.position = position

        # Add this object to the all_objects dictionary in its parent susan
        self.parent_susan.all_objects[self.name] = self

    # Goto turns table so that the chosen item is facing the chosen person
    def goto(self, mod):
        print("Going to " + self.name + ".")  # Say where the table should go

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
                                                        turn))  # Update
            # position var

        # Deal with turns > 360˚ and < -360˚
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

    def used(self, new_name, list_items=True):  # This function enables the
        # item
        self.use = True  # Enable in object
        self.parent_susan.objects[self.name] = self  # Enable in objects
        # dictionary
        self.position = self.parent_susan.current_position  # Set new
        # position of item
        self.name = new_name
        if list_items:
            self.parent_susan.list_items()  # Print updated table items
            add_item(str(self.name), int(self.position))

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
        for ID in self.objects.values():  # For each id in objects
            print(" - Name: '" + str(ID.name) + "' Position: " +
                  str(ID.position))
            # Print name of object in bullet point format
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
        try:
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
        except ValueError:
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
        # Check if the item is enabled
        toggle_item_exists = False  # Haven't found the item yet
        toggle_identifier = ""
        for obj, identifier in self.objects.items():  # Repeat with all enabled
            # items
            if str(obj) == toggle:  # If item in all_objects matches user input
                toggle_identifier = identifier  # Store the ID of the object
                toggle_item_exists = True  # The item the user asked for exists
        if toggle_item_exists:
            toggle_identifier.unused()
        else:
            obj = TableObject(toggle, self)
            obj.used(toggle)
            return obj

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
        if edit_item_exists:
            if edit_identifier.is_used():  # If the item is enabled
                # Set the item's position to the current position
                edit_identifier.position = self.current_position
            else:  # If the item is disabled
                edit_identifier.used(edit)  # Enable the item
        else:
            obj = TableObject(edit, self, use=True)
            return obj


def main():
    default_susan = LazySusan()
    default_susan.print_current_position()
    read_items(default_susan)
    default_susan.list_items()

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
