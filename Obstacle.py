import random

import pygame as pg
from constants import *


class Obstacle:

    def __init__(self, surface: pg.Surface):
        # randomly choose an obstacle
        obstacle_type = random.randint(1, 4)

        # land objects
        if obstacle_type != 4:
            # trees
            if obstacle_type == 1:
                self.width = TREES_WIDTH
                self.height = TREES_HEIGHT
                self.img = pg.image.load('assets/trees.png').convert_alpha()
            # rock
            elif obstacle_type == 2:
                self.width = ROCK_WIDTH
                self.height = ROCK_HEIGHT
                self.img = pg.image.load('assets/rock.png').convert_alpha()
            # grass
            else:
                self.width = GRASS_WIDTH
                self.height = GRASS_HEIGHT
                self.img = pg.image.load('assets/grass.png').convert_alpha()

            top_location = surface.get_height() - self.height
        # flying bird
        else:
            self.width = BIRD_WIDTH
            self.height = BIRD_HEIGHT
            self.img = pg.image.load('assets/bird.png').convert_alpha()
            top_location = surface.get_height() - \
                           random.randint(self.height, self.height*7)

        self.rect = pg.rect.Rect(surface.get_width(), top_location, self.width,
                                 self.height)
        self.jumping = False
        self.velocity = 0
        self.color = random.choice(COLORS)
        self.speed = random.randint(MIN_SPEED, MAX_SPEED)

    def show(self, surface: pg.Surface):
        surface.blit(self.img, self.rect)

    def update_coords(self, dt):
        self.rect.move_ip(-self.speed * dt, 0)
