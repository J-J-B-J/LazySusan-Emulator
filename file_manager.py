import get_input as g


class FileManager:
    """A class to manage the .txt files that are part of this program."""
    def __init__(self):
        self.items_file = 'items.txt'
        self.users_file = 'users.txt'
        self.presets_file = 'presets.txt'

    def clear_items(self):
        with open(self.items_file, 'w') as File:
            File.write("Items:\n")
        print("Items Cleared!")

    def recover_items(self):
        try:
            with open(self.items_file, 'r') as file:  # Try to read the file
                read_data = file.readlines()
        except FileNotFoundError:  # If the file doesn't exist
            with open(self.items_file, 'w') as file:  # Create the file
                file.write("Items:\n")
                # Write this line at the start
            with open(self.items_file, 'r') as file:
                read_data = file.readlines()
        read_data = read_data[1:]  # Remove first line of file, which is
        # "Items:"
        if not read_data:
            print("No Data Found.")
            return None
        else:
            new_read_data = []  # New read data gets set to the old read
            # data, but
            # without the newlines at the end of each line.
            for line in read_data:
                new_read_data.append(line.rstrip("\n"))
            read_data = new_read_data
            print("Data Found!")

            item_data = []
            for line in read_data:  # Save the old data to this program
                item_data.append((str(line[4:]), int(line[:3])))
            print("Item data saved!")
            return item_data

    def preset(self):
        try:
            with open(self.presets_file, 'r') as File:
                read_data = File.readlines()
        except FileNotFoundError:
            with open(self.presets_file, 'w') as File:
                File.write("Presets:\n")
            print("There are no presets.")
            return None
        read_data = read_data[1:]  # Remove first line, which is "Presets:"
        preset = g.get("What preset do you want? ").upper()

        # The code below accesses and decodes the preset
        correct_preset = []
        line_in_preset = False
        for line in read_data:
            if line.upper() == line and preset in line:  # Lines in UPPER
                # are names of presets
                line_in_preset = True
            elif line_in_preset:
                if line == "\n":
                    break
                else:
                    correct_preset.append(line.rstrip("\n"))
        if correct_preset:
            item_data = []
            for item in correct_preset:
                try:
                    position = g.get(f"What is the position of {item}? ")
                    item_data.append((item, int(position)))
                except ValueError:
                    print(
                        f"You entered an invalid value. {item} was not added.")
            return item_data
        else:
            print("That is not a valid preset.")
            return

    def add_item(self, item, position):
        position = str(position)
        for _ in range(0, 3 - len(position)):
            position = f"0{position}"  # Make positions 3-digit numbers.
            # E.g. 12 becomes 012
        position += " "  # Add a space at the end of position
        text = position + item + "\n"
        try:
            with open(self.items_file, 'a') as file:
                file.write(text)
        except FileNotFoundError:
            with open(self.items_file, 'w') as file:
                file.write("Items:\n{text}")

    def remove_item(self, item):
        newlines = ""
        try:
            with open(self.items_file, 'r') as file:
                old_lines = file.readlines()
        except FileNotFoundError:
            with open(self.items_file, 'w') as file:
                file.write("Items:\n")
            print("File Not Found.")
            return
        for line in old_lines[1:]:
            if item not in line:
                newlines += line
                newlines += "\n"
        with open(self.items_file, 'w') as file:
            file.write("Items:\n")
        with open(self.items_file, 'a') as file:
            file.write(newlines)

    def get_users(self):
        try:
            with open(self.users_file, 'r') as file:  # Try to read the file
                read_data = file.readlines()
        except FileNotFoundError:  # If the file doesn't exist
            with open(self.users_file, 'w') as file:  # Create the file
                file.write("Users:\n")
                # Write this line at the start
            with open(self.items_file, 'r') as file:
                read_data = file.readlines()
        read_data = read_data[1:]  # Remove first line of file, which is
        # "Users:"
        if not read_data:
            return {}
        else:
            new_read_data = []  # New read data gets set to the old read
            # data, but without the newlines at the end of each line.
            for line in read_data:
                new_read_data.append(line.rstrip("\n"))
            read_data = new_read_data

            users = {}
            for line in read_data:  # Save the old data to this program
                users[line[4:]] = line[:3]
            return users

    def edit_users(self):
        user = g.get("User: ")
        try:
            with open(self.users_file, 'r') as file:  # Try to read the file
                read_data = file.readlines()
        except FileNotFoundError:  # If the file doesn't exist
            with open(self.users_file, 'w') as file:  # Create the file
                file.write("Users:\n")
                # Write this line at the start
            with open(self.users_file, 'r') as file:
                read_data = file.readlines()
        new_read_data = []
        for line in read_data:
            if user not in line:
                new_read_data.append(line)
        if new_read_data == read_data:  # If user is not in users file,
            # create them
            modifier = g.get("Modifier: ")
            for _ in range(0, 3 - len(modifier)):
                modifier = f"0{modifier}"  # Make positions 3-digit
                # numbers.
                # E.g. 12 becomes 012
            modifier += " "  # Add a space at the end of modifier
            text = modifier + user + "\n"
            with open(self.users_file, 'a') as file:
                file.write(text)
            print("User added!")
        else:  # If user is in users file, remove them
            # Convert read_data to string
            read_data = new_read_data
            new_read_data = ""
            for line in read_data:
                new_read_data += (line + "\n")
            with open(self.items_file, 'w') as file:
                file.write(new_read_data)
            print("User Deleted!")

    def get_modifier(self):  # This function returns the modifier for the
        # specified user
        user = g.get("User? ")
        if user is None:
            return None
        try:
            users = self.get_users()
            return users[user]  # Return the modifier once the user has
            # given a valid answer
        except KeyError:
            print("That is not a valid user.")
