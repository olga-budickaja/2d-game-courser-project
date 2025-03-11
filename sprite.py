import os

import pygame
from constans import DISPLAY, FILE_DIR, HEIGHT_HERO, OFFSET_X, OFFSET_Y, WIDTH_HERO

screen = pygame.display.set_mode(DISPLAY)

class Sprite(pygame.Rect):
    def __init__(self, x: int, y: int, width: int, height: int, image_name: str):
        super().__init__(x, y, width, height)
        self.is_active = True
        self.image_name = image_name
        self.image = None
        self._load_image()

    @property
    def bottom_y(self):
        return self.y + self.height

    @property
    def right_x(self):
        return self.x + self.width

    def _load_image(self, image_name=None):
        if image_name is None:
            image_name = self.image_name

        image_path = os.path.join(FILE_DIR, image_name)
        image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(image, (self.width, self.height))
        return transformed_image


    def _draw(self):
        screen.blit(self.image, (self.x, self.y))

    def _move(self):
        pass

    def _gravity(self):
        pass

    def process(self):
        if self.is_active:
            self._draw()
            self._move()
            self._gravity()

    @classmethod
    def reset_game(cls, hero, blocks):
        for block in blocks:
            block.offset_idx = 1
            block.offset_count = 1
            block.x, block.y = (OFFSET_X, -OFFSET_Y)
            block.x_static, block.y_static = (OFFSET_X, -OFFSET_Y)
            block.is_active = True

        hero.x, hero.y = WIDTH_HERO, HEIGHT_HERO
        hero.is_active = True
