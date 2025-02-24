import pygame

from blocks import Block
from hero import main_hero
from constans import BACGROUND_COLOR, DISPLAY, FPS

screen = pygame.display.set_mode(DISPLAY)

def start_game():
    game_run = True
    clock = pygame.time.Clock()

    while game_run:
        screen.fill(BACGROUND_COLOR)
        main_hero.process()
        Block.all_block_process()

        screen.blit(main_hero.image, (main_hero.x, main_hero.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

        pygame.display.flip()
        clock.tick(FPS)

start_game()
