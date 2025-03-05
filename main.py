import pygame

from backgrounds import main_bg
from blocks import Block
from hero import Hero, main_hero
from constans import BACGROUND_COLOR, DISPLAY, FPS, HEIGHT_HERO, WIDTH_HERO

screen = pygame.display.set_mode(DISPLAY)

def start_game():
    global main_hero
    game_run = True

    clock = pygame.time.Clock()

    while game_run:
        screen.fill(BACGROUND_COLOR)
        main_bg.process()
        main_hero.process()
        Block.all_block_process()

        screen.blit(main_hero.image, (main_hero.x, main_hero.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

        pygame.display.flip()
        clock.tick(FPS)

start_game()
