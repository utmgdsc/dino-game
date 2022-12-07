import pygame.mixer


class Sound:
    sounds: dict

    def __init__(self):
        self.sounds = {}
        self.sounds['jump'] = pygame.mixer.Sound('assets/jump_sound.wav')
        # more sounds to be added

    def play(self, sound: str):
        self.sounds[sound].play()
