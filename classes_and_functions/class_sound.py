import pygame


class Sound:
    def __init__(self, sound):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        self.sound = sound
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()
