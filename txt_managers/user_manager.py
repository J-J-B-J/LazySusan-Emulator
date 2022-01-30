from classes_and_functions import get_input as g


class UserManager:
    """A class to manage users.txt."""

    def __init__(self):
        self.users_file = 'txt_files/users.txt'

    def read_users_file(self):
        try:
            with open(self.users_file, 'r') as file:  # Try to read the file
                read_data = file.readlines()
        except FileNotFoundError:  # If the file doesn't exist
            with open(self.users_file, 'w') as file:  # Create the file
                file.write("Users:\n")
                # Write this line at the start
            with open(self.users_file, 'r') as file:
                read_data = file.readlines()
        return read_data

    def get_users(self):
        read_data = self.read_users_file()
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
        read_data = self.read_users_file()
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
            with open(self.users_file, 'w') as file:
                file.write(new_read_data)
            print("User Deleted!")

    def get_modifier(self):  # This function returns the modifier for the
        # specified user
        user = g.get("User? ")
        if user is None:
            return None
        users = self.get_users()
        try:
            return int(users[user])  # Return the modifier once the user has
            # given a valid answer
        except KeyError:
            print("That is not a valid user.")
