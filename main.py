import get_input as g
from file_manager import FileManager
from table_object import TableObject
from lazy_susan import LazySusan

"""This is the main module for the program. It calls the other .py files."""


def main():
    default_susan = LazySusan()
    default_susan.print_current_position()
    item_data = FileManager().recover_items()
    if item_data:
        for item in item_data:
            TableObject(item[0], default_susan, item[1])
    default_susan.list_items()

    while True:
        # Ask what the user wants to do
        action = str(g.get("Action: "))

        if action == "Goto":  # If the user wants to turn the table:
            default_susan.goto()

        elif action == "Toggle":  # If the user wants to change the items on
            # the table
            default_susan.toggle()

        elif action == "Bulk Toggle":  # If the user wants to change many
            # items on the table
            print("Enter cancel to end the bulk toggle.")
            default_susan.toggle(bulk=True)

        elif action == "Edit":  # Edit the position of an item
            default_susan.edit()

        # Turn the table manually
        elif action == "Turn":
            default_susan.turn()

        # Edit the users list
        elif action == "Users":
            FileManager().edit_users()

        # Clear the items list
        elif action == "Clear":
            FileManager().clear_items()

        # Clear the items list
        elif action == "Preset":
            item_data = FileManager().preset()
            if item_data:
                for item in item_data:
                    TableObject(item[0], default_susan, item[1])
            default_susan.list_items()

        # Clear the items list
        elif action == "Edit Presets":
            FileManager().clear_items()

        else:  # If the action provided isn't valid
            print("The action you entered wasn't valid")


if __name__ == '__main__':
    main()
