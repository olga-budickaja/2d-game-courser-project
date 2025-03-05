import os

import pygame

from constans import FILE_DIR
from images import BG
from sprite import Sprite, screen


class Background(Sprite):
    offset_x = 0
    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)

        self.x_static = self.x
        self.y_static = self.y
        self.image = self._load_image(self.image_name)

    def _load_image(self, image_name=None):
        if image_name is None:
            image_name = self.image_name

        image_path = os.path.join(FILE_DIR, image_name)
        transformed_image = pygame.image.load(image_path).convert()
        return transformed_image

    def _draw(self):
        screen.blit(self.image, (self.x, self.y))

    def _move(self):
        self.x = self.x_static - self.offset_x

main_bg = Background(0, 0, 4800, 600, BG)
