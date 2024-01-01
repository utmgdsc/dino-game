import pygame as pg

from constants import *
from sound import Sound


class Player:

    def __init__(self, surface: pg.Surface):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.initial_pos = X_OFFSET, surface.get_height() - self.height
        self.rect = pg.rect.Rect(X_OFFSET, surface.get_height() - self.height,
                                 self.width,
                                 self.height)
        self.img = pg.image.load('assets/dino.png').convert_alpha()

        self.jumping = False
        self.ducking = False
        self.velocity = 0
        self.sound = Sound()

    def show(self, surface: pg.Surface):
        surface.blit(self.img, self.rect)

    def jump(self):
        if self.jumping:
            return
        self.jumping = True
        self.sound.play('jump')
        self.velocity = PLAYER_JUMP_FORCE

    def duck(self):
        if self.ducking:
            return
        self.ducking = True

    def unduck(self):
        if not self.ducking:
            return
        self.rect.update(self.initial_pos[0], self.initial_pos[1],
                                 PLAYER_WIDTH, PLAYER_HEIGHT)
        self.img = pg.image.load('assets/dino.png').convert_alpha()
        self.ducking = False

    def update_coords(self, dt):
        if self.jumping:
            if self.ducking:
                self.unduck()
            self.rect.move_ip(0, -dt * self.velocity * PLAYER_JUMP_COEFFICIENT)
            self.velocity = self.velocity + dt * GRAVITY
            if self.rect.y > self.initial_pos[1]:
                self.rect.update(self.initial_pos[0], self.initial_pos[1],
                                 PLAYER_WIDTH, PLAYER_HEIGHT)
                self.jumping = False

        if self.ducking:
            self.rect.update(self.initial_pos[0], self.initial_pos[1] +
                             self.height - DUCK_HEIGHT, DUCK_WIDTH, DUCK_HEIGHT)
            self.img = pg.image.load('assets/dino_duck.png').convert_alpha()
