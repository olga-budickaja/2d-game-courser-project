import os

import pygame
from constans import DISPLAY, FILE_DIR

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
