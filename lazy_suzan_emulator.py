current_position = 0  # Set the num of degrees the table has turned = 0

raw_input = ""


def get_input(prompt):  # This enables the input of text from a test file
    if __name__ == '__main__':
        return input(prompt)
    else:
        return raw_input


objects = {}  # Contains the objects and their identifiers that are on the table.
all_objects = {}  # Contains all the objects and their identifiers.


# This function prints out all the objects in turn
# It's used when a change to the objects' dictionary occurs
def list_items_on_table():
    print("\nItems on table:        *UPDATED*")
    for table_obj, ID in objects.items():  # For each obj & id in objects
        print(" - " + table_obj)  # Print name of object in bullet point format
    print("\n")


def print_current_position():  # This function prints table's current position
    print("The table is now in position " + str(current_position) + ".")


def get_modifier():  # This function returns the modifier for the specified user
    modifier = get_input("Modifier? ")
    return modifier  # Return the modifier once the user has given a valid answer


# This class is for real-world objects that can be placed on the lazy susan
class TableObject:
    def __init__(self, name):
        # Name, Position on table, Currently on table?
        self.name = name
        self.position = 0
        self.use = False

        # Add this object to the all_objects dictionary
        all_objects[self.name] = self

    # Goto turns table so that the chosen item is facing the chosen person
    def goto(self, mod):
        global current_position  # So that goto can change that table's position
        print("Going to " + self.name + ".")  # Say where the table should go

        turn = (int(self.position) + int(mod)) - current_position  # Calculate turn
        current_position = (current_position + turn) % 360  # Update pos var

        # The following converts turns greater than 180 into negative numbers
        # E.g. 260 turn becomes -100 turn
        if turn > 180:
            turn = (360 - turn) * -1

        if turn < 0:
            # Print the turn as anticlockwise
            print("The table turned " + str(turn * -1) + " anticlockwise.")
        if turn > 0:
            # Print the turn as clockwise
            print("The table turned " + str(turn) + " clockwise.")
        if turn == 0:  # i.e. table is already in correct position
            print("The table did not move.")
        print_current_position()  # Show the table's updated position

    def used(self):  # This function enables the item
        self.use = True  # Enable in object
        objects[self.name] = self  # Enable in objects dictionary
        self.position = current_position  # Set new position of item
        print("Position set.")
        list_items_on_table()  # Print updated table items

    def unused(self):  # This function disables the item
        self.use = False  # Disable in object
        del objects[self.name]  # Disable in objects dictionary
        list_items_on_table()  # Print updated table items

    def is_used(self):  # Checks weather or not the item is enabled
        if self.use:
            return True
        return False


# These are the objects that can be enabled:
cutlery = TableObject("Cutlery")
tom_sauce = TableObject("Tomato Sauce")
bbq_sauce = TableObject("BBQ Sauce")
chilli_sauce = TableObject("Sweet Chilli Sauce")
salad = TableObject("Salad")
salt = TableObject("Salt")
pepper = TableObject("Pepper")
bible = TableObject("Bible")
olive_oil = TableObject("Olive Oil")


def goto():
    modifier = get_modifier()  # Get the modifier for a specific person
    goto = get_input("Where to? ")  # Ask what item the person wants
    valid_answer_found = False  # The user hasn't yet provided valid answer
    for obj, goto_identifier in objects.items():  # Repeat w all objects on table
        # If the item the user entered matches a table object
        if str(obj) == goto:
            goto_identifier.goto(modifier)  # Turn table to the table object
            valid_answer_found = True
    if not valid_answer_found:
        print("You can't go to that item or modifier now.")  # Give an error


def toggle():
    toggle = get_input("Item to Toggle? ")  # Ask for item
    # Check the existence of the item (it's presence in all_objects)
    toggle_item_exists = False  # Haven't found the item yet
    toggle_identifier = ""
    for obj, identifier in all_objects.items():  # Repeat with all items
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


def edit():
    edit = get_input("Item to Edit? ")  # Ask for item

    # Check the existence of the item (it's presence in all_objects)
    edit_item_exists = False  # Haven't found the item yet
    edit_identifier = ""
    for obj, identifier in all_objects.items():  # Repeat with all items
        if str(obj) == edit:  # If item in all_objects matches user input
            edit_identifier = identifier  # Store the ID of the object
            edit_item_exists = True  # The item the user asked for exists
    if not edit_item_exists:
        print("The item you asked for doesn't exist.")
    else:
        if edit_identifier.is_used():  # If the item is enabled
            # Set the item's position to the current position
            edit_identifier.position = current_position
        else:  # If the item is disabled
            edit_identifier.used()  # Enable the item


def turn():
    turn = get_input("By how much? ")   # Get a turn amount
    if type(turn) is int:
        global current_position
        current_position = (current_position + int(turn)) % 360  # Update position var
        # The following converts turns greater than 180 into negative numbers
        # E.g. 260 turn becomes -100 turn
        if int(turn) > 180:
            turn = (360 - int(turn)) * -1
        if turn < 0:
            # Print the turn as anticlockwise
            print("The table turned " + str(turn * -1) + " anticlockwise.")
        if turn > 0:
            # Print the turn as clockwise
            print("The table turned " + str(turn) + " clockwise.")
        if turn == 0:  # i.e. table is already in correct position
            print("The table did not move.")
        print_current_position()  # Show the table's updated position
    else:
        print("The turn you entered wasn't an integer")


def main():
    # Ask what the user wants to do
    action = str(get_input("Action: "))

    if action == "Goto":  # If the user wants to turn the table:
        goto()

    elif action == "Toggle":  # If the user wants to change the items on the table
        toggle()

    elif action == "Edit":  # Edit the position of an item
        edit()

    # Turn the table manually, relative to seat with modifier 0
    elif action == "Turn":
        turn()

    else:  # If the action provided isn't valid
        print("The action you entered wasn't valid")


if __name__ == '__main__':
    print_current_position()  # Run the above function upon program run
    while True:
        main()
