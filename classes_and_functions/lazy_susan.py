import classes_and_functions.get_input as g
from classes_and_functions.table_object import TableObject
from txt_managers.item_manager import ItemManager
from txt_managers.preset_manager import PresetManager
from txt_managers.user_manager import UserManager


class LazySusan:  # Class to keep track of an emulated lazy susan
    """A class to represent a lazy susan"""

    def __init__(self, starting_position=int(0)):
        self.current_position = starting_position
        self.objects = {}

    def run(self):
        self.print_current_position()
        item_data = ItemManager().recover_items()
        if item_data:
            for item in item_data:
                TableObject(item[0], self)
        self.list_items()

        while True:
            # Ask what the user wants to do
            action = str(g.get("Action: "))

            if action == "Goto":  # If the user wants to turn the table:
                self.goto()

            elif action == "Toggle":  # If the user wants to change the
                # items on
                # the table
                self.toggle()

            elif action == "Bulk Toggle":  # If the user wants to change many
                # items on the table
                print("Enter cancel to end the bulk toggle.")
                self.toggle(bulk=True)

            elif action == "Edit":  # Edit the position of an item
                self.edit()

            # Turn the table manually
            elif action == "Turn":
                self.turn()

            # Edit the users list
            elif action == "Users":
                UserManager().edit_users()

            # Clear the items list
            elif action == "Clear":
                ItemManager().clear_items()

            # Clear the items list
            elif action == "Preset":
                item_data = PresetManager().preset()
                if item_data:
                    for item in item_data:
                        TableObject(item[0], self)
                self.list_items()

            # Clear the items list
            elif action == "Edit Presets":
                ItemManager().clear_items()

            else:  # If the action provided isn't valid
                print("The action you entered wasn't valid")

    def list_items(self):
        # This function prints out all the objects in turn
        # It's used when a change to the objects' dictionary occurs
        if self.objects:  # If there are objects:
            print("\nItems on table:")
            for ID in self.objects.values():  # For each id in objects
                print(f" - {str(ID.name)}")
                # Print name of object in bullet point format
            print("\n")
        else:  # If there are no objects:
            print("There are no objects on the table now.")

    def print_current_position(self):  # This function prints table's
        # current position
        print(f"The table is now in position {str(self.current_position)}.")

    def turn(self, turn=None):
        if not turn:
            turn = g.get("By how much? ")  # Get a turn amount
            if turn is None:
                print("Cancelled")
                return

        if "-" in str(turn):  # Deal with negative turns
            turn_is_negative = True
            new_turn = ""
            for character in str(turn):
                if character != "-":
                    new_turn = new_turn + character
            turn = new_turn
        else:
            turn_is_negative = False
        try:
            turn = int(turn)
        except ValueError:
            print("The turn you entered wasn't an integer")
            return
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
            print(f"The table turned {str(turn)} anticlockwise.")
        elif turn == 0:  # i.e. table is already in correct position
            print("The table did not move.")
        else:
            # Print the turn as clockwise
            print(f"The table turned {str(turn)} clockwise.")

        self.print_current_position()  # Show the table's updated position

    def goto(self):
        modifier = UserManager().get_modifier()
        if modifier is None:
            print("Cancelled")
            return
        goto = g.get("Where to? ")  # Ask what item the person wants
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

    def toggle(self, bulk=False):
        toggle = g.get("Item: ")  # Ask for item
        if toggle is None:
            if bulk:
                print("Bulk ended.")
            else:
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
            obj.used(toggle, self)
            if not bulk:
                return obj
        if bulk:
            self.toggle(bulk=True)

    def edit(self):
        edit = g.get("Item to Edit? ")
        # Ask for item
        if edit is None:
            print("Cancelled")
            return
        # Check the existence of the item (it's presence in all_objects)
        edit_item_exists = False  # Haven't found the item yet
        edit_identifier = ""
        for obj, identifier in self.objects.items():
            if str(obj) == edit:  # If item in all_objects matches user input
                edit_identifier = identifier  # Store the ID of the object
                edit_item_exists = True  # The item the user asked for exists
        if edit_item_exists:
            if edit_identifier in self.objects.values():  # If the item is
                # enabled, set the item's position to the current position
                edit_identifier.position = self.current_position
            else:  # If the item is disabled
                edit_identifier.used(edit)  # Enable the item
        else:
            obj = TableObject(edit, self)
            return obj
