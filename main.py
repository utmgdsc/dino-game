import random
import time

import pygame as pg
from pygame import KEYDOWN
from pygame import constants

from Obstacle import Obstacle
from Player import Player
from constants import *

game_active = True


def game_over():
    # TODO
    global game_active
    game_active = False
    print('You lost!')


def main():
    # Initialize pygame
    pg.init()
    screen = pg.display.set_mode((600, 480))
    pg.display.set_caption("GDSC Dino")
    clock = pg.time.Clock()
    pg.mouse.set_visible(True)
    start = int(time.time_ns())
    font = pg.font.SysFont("Comic Sans", 16)

    player = Player(screen)
    obstacles = []
    next_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)
    time_to_unduck = None
    global game_active
    while game_active:
        dt = clock.tick(fps) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_active = False
                return
            if event.type == KEYDOWN:
                if event.key == constants.K_SPACE:
                    player.jump()
                elif event.key == constants.K_DOWN:
                    player.duck()
                    time_to_unduck = DUCK_TIME

        if time_to_unduck:
            time_to_unduck -= dt
            if time_to_unduck <= 0:
                player.unduck()
                time_to_unduck = None

        next_spawn -= dt
        if next_spawn <= 0:
            obstacles.append(Obstacle(screen))
            next_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)
        screen.fill(BG_RGB)
        score = (int(time.time_ns()) - start) // 50000000
        text = font.render(str(score), True, (0, 0, 0))
        screen.blit(text, (500, 25))
        player.show(screen)
        player.update_coords(dt)
        for obstacle in obstacles:
            if obstacle.rect.right <= 0:
                obstacles.remove(obstacle)
            obstacle.update_coords(dt)
            obstacle.show(screen)

        if player.rect.collidelist(
                [obstacle.rect for obstacle in obstacles]) != -1:
            game_over()

        pg.display.update()


if __name__ == "__main__":
    main()
    pg.quit()
