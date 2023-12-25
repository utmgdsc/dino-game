import random
import time

import pygame as pg
from pygame import KEYDOWN
from pygame import constants

from Obstacle import Obstacle
from Player import Player
from constants import *

game_active = True


def game_over(surface: pg.Surface, score: int) -> bool:
    surface.fill(BG_RGB)
    font = pg.font.SysFont("Comic Sans", 32)
    button1 = font.render("Quit", True, (0, 0, 0))
    button2 = font.render("Retry", True, (0, 0, 0))
    lab1 = font.render("You Lost!", True, (0, 0, 0))
    lab2 = font.render("Score: " + str(score), True, (0, 0, 0))
    button1_rect = button1.get_rect()
    button2_rect = button2.get_rect()
    lab1_rect = lab1.get_rect()
    lab2_rect = lab2.get_rect()
    button1_rect.center = (surface.get_width()/2, surface.get_height()/2 - 25)
    button2_rect.center = (surface.get_width()/2, surface.get_height()/2 + 50)
    lab1_rect.center = (surface.get_width()/2, surface.get_height()/2 - 175)
    lab2_rect.center = (surface.get_width()/2, surface.get_height()/2 - 100)
    surface.blit(button1, button1_rect)
    surface.blit(button2, button2_rect)
    surface.blit(lab1, lab1_rect)
    surface.blit(lab2, lab2_rect)

    run = True
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(pg.mouse.get_pos()):
                    return False
                elif button2_rect.collidepoint(pg.mouse.get_pos()):
                    return True
        pg.display.update()


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
            obstacles.clear()
            player.jumping = False
            player.rect.update(X_OFFSET, screen.get_height() - PLAYER_HEIGHT,
                               PLAYER_WIDTH, PLAYER_HEIGHT)
            if game_over(screen, score):
                start = int(time.time_ns())
            else:
                game_active = False
            next_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)

        pg.display.update()


if __name__ == "__main__":
    main()
    pg.quit()
