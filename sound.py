import pygame.mixer


class Sound:
    sounds: dict
    no_music: bool

    def __init__(self):
        self.sounds = {}
        self.no_music = False
        try:
            self.sounds['jump'] = pygame.mixer.Sound('assets/jump_sound.wav')

            background_music = pygame.mixer.Sound('assets/background_music.mp3')
            background_music.set_volume(0.4)
            self.sounds['background_music'] = background_music

            game_over_sound = pygame.mixer.Sound('assets/game_over_sound.wav')
            game_over_sound.set_volume(0.4)
            self.sounds['game_over'] = game_over_sound
        except FileNotFoundError:
            self.no_music = True

    def play(self, sound: str):
        if sound == "background_music":
            self.sounds[sound].play(-1)
        else:
            self.sounds[sound].play()

    def stop(self, sound: str):
        self.sounds[sound].stop()
