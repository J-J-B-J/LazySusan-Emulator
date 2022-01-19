import sys

import pygame

import classes_and_functions.func_get_input as g
from classes_and_functions.class_table_object import TableObject
from classes_and_functions.class_lazy_susan import LazySusan
from classes_and_functions.class_output import Output
from classes_and_functions.class_sound import Sound

from txt_managers.manager_settings import SettingsManager as Sm
from txt_managers.manager_presets import PresetManager
from txt_managers.manager_users import UserManager
from txt_managers.manager_items import ItemManager


class Emulator:
    """A class to manage the pygame image emulator."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(Sm().get_screen())
        pygame.display.set_caption(Sm().get_screen_caption())
        pygame.display.set_icon(pygame.image.load(Sm().get_screen_icon()))
        self.out = Output(self)
        self.susan = LazySusan(self)
        self.susan.print_current_position()

    def run(self):
        item_data = ItemManager(self).recover_items()
        if item_data:
            for item in item_data:
                TableObject(item[0], self.susan, self, item[1])
        self.susan.list_items()

        while True:
            self.screen.fill(Sm().get_screen_colour())
            self.susan.blit()
            self.out.blit_me()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

            # Ask what the user wants to do
            action = str(g.get("Action: ", self))

            if action == "Goto":  # If the user wants to turn the table:
                self.susan.goto(self)

            elif action == "Toggle":  # If the user wants to change the
                # items on
                # the table
                self.susan.toggle(self)

            elif action == "Bulk Toggle":  # If the user wants to change many
                # items on the table
                self.out.print_this("Press Esc to end the bulk toggle.")
                self.susan.toggle(self, bulk=True)

            elif action == "Edit":  # Edit the position of an item
                self.susan.edit(self)

            # Turn the table manually
            elif action == "Turn":
                self.susan.turn(self)

            # Edit the users list
            elif action == "Users":
                UserManager(self).edit_users(self)

            # Clear the items list
            elif action == "Clear":
                ItemManager(self).clear_items()

            # Clear the items list
            elif action == "Preset":
                item_data = PresetManager().preset(self)
                if item_data:
                    for item in item_data:
                        TableObject(item[0], self.susan, self)
                self.susan.list_items()

            # Clear the items list
            elif action == "Edit Presets":
                ItemManager(self).clear_items()

            else:  # If the action provided isn't valid
                Sound('sounds/Error.mp3')
