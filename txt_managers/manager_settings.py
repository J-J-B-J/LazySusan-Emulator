import sys


default_settings = \
    "Screen Width:                 1300\n"\
    "Screen Height:                800\n"\
    "Screen Background R:          220\n"\
    "Screen Background G:          220\n"\
    "Screen Background B:          220\n"\
    "Screen Caption:               Lazy Susan\n"\
    "Screen Icon Path:             images/Logo.png\n"\
    "Lazy Susan Colour R:          200\n"\
    "Lazy Susan Colour G:          200\n"\
    "Lazy Susan Colour B:          150\n"\
    "Text Colour R:                0\n"\
    "Text Colour G:                0\n"\
    "Text Colour B:                0\n"\



class SettingsManager:
    """A class to manage saved_settings.txt."""

    def __init__(self):
        self.settings_file = 'txt_files/saved_settings.txt'

        self.read_file()

    def read_file(self):
        try:
            with open(self.settings_file, 'r') as File:
                settings = File.readlines()
        except FileNotFoundError:
            with open(self.settings_file, 'w') as File:
                File.write(default_settings)
            with open(self.settings_file, 'r') as File:
                settings = File.readlines()
            sys.exit()
        new_settings = []
        for line in settings:
            new_line = line[30:].rstrip("\n")
            new_settings.append(new_line)
        return new_settings

    def get_screen(self):
        settings = self.read_file()
        try:
            screen_dimensions = (int(settings[0]), int(settings[1]))
        except ValueError:
            screen_dimensions = (1300, 800)
        return screen_dimensions

    def get_screen_colour(self):
        settings = self.read_file()
        screen_colour = (int(settings[2]), int(settings[3]), int(settings[4]))
        return screen_colour

    def get_screen_caption(self):
        settings = self.read_file()
        screen_caption = settings[5]
        return screen_caption

    def get_screen_icon(self):
        settings = self.read_file()
        screen_icon = settings[6]
        return screen_icon

    def get_susan_colour(self):
        settings = self.read_file()
        screen_colour = (int(settings[7]), int(settings[8]), int(settings[9]))
        return screen_colour

    def get_text_colour(self):
        settings = self.read_file()
        screen_colour = (int(settings[10]), int(settings[11]),
                         int(settings[12]))
        return screen_colour
