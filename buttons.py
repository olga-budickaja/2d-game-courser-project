import pygame

from constans import DISPLAY
from fonts import FONT_28


def draw_buttons(screen):
    button_restart = pygame.Rect(DISPLAY[0] // 4, DISPLAY[1] // 2 + 50, 200, 50)
    button_exit = pygame.Rect(DISPLAY[0] // 2, DISPLAY[1] // 2 + 50, 200, 50)

    pygame.draw.rect(screen, (255, 0, 0), button_restart)
    pygame.draw.rect(screen, (0, 255, 0), button_exit)

    restart_text = FONT_28.render("NEW START", True, (255, 255, 255))
    exit_text = FONT_28.render("EXIT", True, (255, 255, 255))

    screen.blit(restart_text, (button_restart.x + 20, button_restart.y + 10))
    screen.blit(exit_text, (button_exit.x + 70, button_exit.y + 10))

    return button_restart, button_exit
