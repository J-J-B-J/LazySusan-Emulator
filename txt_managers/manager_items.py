class ItemManager:
    """A class to manage saved_items.txt."""

    def __init__(self, emulator):
        self.items_file = 'txt_files/saved_items.txt'
        self.emulator = emulator

    def clear_items(self):
        with open(self.items_file, 'w') as File:
            File.write("Items:\n")
        self.emulator.out.print_this("Items Cleared!")

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
            self.emulator.out.print_this("No Data Found.")
            return None
        else:
            new_read_data = []  # New read data gets set to the old read
            # data, but
            # without the newlines at the end of each line.
            for line in read_data:
                new_read_data.append(line.rstrip("\n"))
            read_data = new_read_data
            self.emulator.out.print_this("Data Found!")

            item_data = []
            for line in read_data:  # Save the old data to this program
                item_data.append((str(line[4:]), int(line[:3])))
            self.emulator.out.print_this("Item data saved!")
            return item_data

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
            self.emulator.out.print_this("File Not Found.")
            return
        for line in old_lines[1:]:
            if item not in line:
                newlines += line
                newlines += "\n"
        with open(self.items_file, 'w') as file:
            file.write("Items:\n")
        with open(self.items_file, 'a') as file:
            file.write(newlines)
