import pygame.font

from txt_managers.manager_settings import SettingsManager as Sm


class Text:
    """A class to display text on the pygame screen."""
    def __init__(self, text, emulator, x_pos, y_pos):
        # Uncomment the below line to manually debug:
        # print(text)
        self.emulator = emulator
        self.screen = emulator.screen
        self.screen_rect = self.screen.get_rect()
        self.text = text
        self.text_colour = Sm().get_text_colour()
        self.bg_colour = Sm().get_screen_colour()
        self.font = pygame.font.SysFont("sanserif", 30)
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = self.font.render(self.text, True, self.text_colour,
                                      self.bg_colour)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    def blit(self):
        self.emulator.screen.blit(self.image, self.rect)
