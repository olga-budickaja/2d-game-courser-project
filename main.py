import pygame

from backgrounds import main_bg, game_over
from blocks import Block
from buttons import draw_buttons
from coin import Coin
from fonts import FONT_46
from hero import main_hero
from constans import BACGROUND_COLOR, COLOR_COIN, COUNTER_COIN, DISPLAY, FPS, POSITION_COIN, SCREEN_WIDTH

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(DISPLAY)

def draw_coin_counter():
    """Function to display hearts instead of numbers"""
    hearts = "♥" * main_hero.counter_coin
    text = FONT_46.render(hearts, True, COLOR_COIN)
    screen.blit(text, POSITION_COIN)

def start_game():
    global main_hero
    game_run = True

    clock = pygame.time.Clock()

    while game_run:
        screen.fill(BACGROUND_COLOR)
        main_bg.process()
        main_hero.process()
        Block.all_block_process()
        Coin.all_coin_process()
        screen.blit(main_hero.image, (main_hero.x, main_hero.y))

        draw_coin_counter()

        if main_hero.counter_coin < 1:
            game_over.process()
            button_restart, button_exit = draw_buttons(screen)

        if main_hero.x >= SCREEN_WIDTH:
            game_over.process()
            button_restart, button_exit = draw_buttons(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_restart.collidepoint(mouse_x, mouse_y):
                    game_run = True
                    main_hero.counter_coin = COUNTER_COIN
                    game_run = True
                    break
                elif button_exit.collidepoint(mouse_x, mouse_y):
                    game_run = False

        pygame.display.flip()
        clock.tick(FPS)

start_game()
