import pygame as pg

PLAYER_JUMP_FORCE = 10
PLAYER_JUMP_COEFFICIENT = 50
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
X_OFFSET = 50
PLAYER_COLOR = (0, 0, 255)
GRAVITY = -10


class Player:

    def __init__(self, surface: pg.Surface):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.initial_pos = X_OFFSET, surface.get_height() - self.height
        self.rect = pg.rect.Rect(X_OFFSET, surface.get_height() - self.height, self.width,
                                 self.height)
        self.jumping = False
        self.velocity = 0

    def Show(self, surface: pg.Surface):
        pg.draw.rect(surface, PLAYER_COLOR, self.rect)

    def Jump(self):
        if self.jumping:
            return
        self.jumping = True
        self.velocity = PLAYER_JUMP_FORCE

    def UpdateCoords(self, dt):
        if self.jumping:
            self.rect.move_ip(0,-dt * self.velocity*PLAYER_JUMP_COEFFICIENT)
            self.velocity = self.velocity + dt * GRAVITY
            if self.rect.y > self.initial_pos[1]:
                self.rect.update(self.initial_pos[0], self.initial_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT)
                self.jumping = False
