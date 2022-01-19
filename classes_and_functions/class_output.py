from classes_and_functions.class_text import Text


class Output:
    """A class to essentially print program output to the pygame window."""
    def __init__(self, emulator):
        self.emulator = emulator
        self.output = ""
        self.image = Text(self.output, self.emulator, 20, 20)
        self.stop_display_time = 0

    def print_this(self, text, row=1):
        self.output = text
        for _ in range(0, 50 - len(self.output)):
            self.output += " "
        self.image = Text(self.output, self.emulator, 20, row * 20)
        self.image.blit()

    def blit_me(self):
        self.image.blit()
