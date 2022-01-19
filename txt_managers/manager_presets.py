from classes_and_functions import func_get_input as g
from classes_and_functions.class_output import Output


class PresetManager:
    """A class to manage saved_presets.txt."""
    def __init__(self):
        self.presets_file = 'txt_files/saved_presets.txt'

    def preset(self, emulator):
        try:
            with open(self.presets_file, 'r') as File:
                read_data = File.readlines()
        except FileNotFoundError:
            with open(self.presets_file, 'w') as File:
                File.write("Presets:\n")
            Output("There are no presets.")
            return None
        read_data = read_data[1:]  # Remove first line, which is "Presets:"
        preset = g.get("What preset do you want? ", emulator).upper()

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
                    position = g.get(
                        f"What is the position of {item}? ", emulator)
                    item_data.append((item, int(position)))
                except ValueError:
                    Output(
                        f"You entered an invalid value. {item} was not added.")
            return item_data
        else:
            Output("That is not a valid preset.")
            return
