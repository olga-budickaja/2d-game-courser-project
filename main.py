import pygame

from backgrounds import main_bg
from blocks import Block
from coin import Coin
from hero import main_hero
from constans import BACGROUND_COLOR, DISPLAY, FPS

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
        Coin.all_coin_process()

        screen.blit(main_hero.image, (main_hero.x, main_hero.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

        pygame.display.flip()
        clock.tick(FPS)

start_game()

from typing import List, Dict

def count_repeated_strings(list1: List[str], list2: List[str]) -> Dict[int, List[str]]:
    """
    Returns a dictionary where the key is the number of occurrences, the value is a list of strings.


    :param last1: List of strings
    :param last2: List of strings

    :return: Dict[int, List[str]]: Словник {кількість повторень: [рядок, ...]}.
    :raises ValueError: if the lenght of list < 0 or the lenght of list > 1000
    """
    combined_list = list1 + list2
    count_dict: Dict[str, int] = {}

    for string in combined_list:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1

    result: Dict[int, List[str]] = {}
    for string, count in count_dict.items():
        if count > 1:
            if count not in result:
                result[count] = []
            result[count].append(string)

    return result
