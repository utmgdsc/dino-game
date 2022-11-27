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
        self.jumping = False
        self.velocity = 0
        self.sound = Sound()

    def show(self, surface: pg.Surface):
        pg.draw.rect(surface, PLAYER_COLOR, self.rect)

    def jump(self):
        if self.jumping:
            return
        self.jumping = True
        self.sound.play('jump')
        self.velocity = PLAYER_JUMP_FORCE

    def update_coords(self, dt):
        if self.jumping:
            self.rect.move_ip(0, -dt * self.velocity * PLAYER_JUMP_COEFFICIENT)
            self.velocity = self.velocity + dt * GRAVITY
            if self.rect.y > self.initial_pos[1]:
                self.rect.update(self.initial_pos[0], self.initial_pos[1],
                                 PLAYER_WIDTH, PLAYER_HEIGHT)
                self.jumping = False
