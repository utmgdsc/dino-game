import random

import pygame as pg

COLORS = [(0, 255, 0), (255, 0, 0)]
MIN_WIDTH = 50
MAX_WIDTH = 100
MIN_HEIGHT = 50
MAX_HEIGHT = 100
MIN_SPEED = 400
MAX_SPEED = 400


class Obstacle:

    def __init__(self, surface: pg.Surface):
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.height = random.randint(MIN_HEIGHT, MAX_HEIGHT)
        self.rect = pg.rect.Rect(surface.get_width(), surface.get_height() - self.height, self.width,
                                 self.height)
        self.jumping = False
        self.velocity = 0
        self.color = random.choice(COLORS)
        self.speed = random.randint(MIN_SPEED, MAX_SPEED)

    def Show(self, surface: pg.Surface):
        pg.draw.rect(surface, self.color, self.rect)

    def UpdateCoords(self, dt):
        self.rect.move_ip(-self.speed * dt, 0)
