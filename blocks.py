from images import BLOCK
from map import GAME_MAP
from sprite import Sprite

def map_generator(game_map):
    x = 0
    y = 0
    for row in game_map:
        for item in row:
            if item == "1":
                yield Block(x, y, 80, 40,'images/bg/block.png')
            x += 80
        y += 40
        x = 0


class Block(Sprite):
    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)
        self.image = self._load_image(BLOCK)

    block_list = []

    @classmethod
    def init(cls):
        cls.block_list = [block for block in map_generator(GAME_MAP)]

    def collide_hero_up(self, hero):
        if self.colliderect(hero):
            if self.y >= hero.bottom_y - 3:
                return True

    def collide_hero_left(self, hero):
        if self.colliderect(hero):
            if self.x <= hero.right_x and hero.x < self.x and not self.y >= hero.bottom_y - 3:
                return True

    def collide_hero_right(self, hero):
        if self.colliderect(hero):
            if self.right_x >= hero.x and hero.right_x > self.right_x and not self.y >= hero.bottom_y - 3:
                return True

    @classmethod
    def all_block_process(cls):
        for block in cls.block_list:
            block.process()

Block.init()
