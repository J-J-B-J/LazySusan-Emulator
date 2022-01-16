raw_input = ""
test = False


def get(prompt):
    """Replaces the input function, to allow for input from a test file."""
    if not test:  # If this is the main program, just run the normal input
        # function
        return_value = str(input(prompt))
    else:  # If in testing mode, return the input from the test program
        return_value = str(raw_input)
    return_value = return_value.title()
    if "Cancel" in return_value:
        return None
    return return_value
