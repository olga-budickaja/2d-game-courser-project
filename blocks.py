import time
from constans import BLOCK_HEIGHT, BLOCK_WIDTH, HEIGHT_HERO, OFFSET_X, OFFSET_Y, SCREEN_START, WIDTH_HERO
from images import BLOCK, RIVER_BLOCK
from map import GAME_MAP
from sprite import Sprite
from sprite import screen

def map_generator(game_map):
    x = 0
    y = 0
    for row in game_map:
        for item in row:
            if item == "1":
                yield Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK)
            if item == "2":
                yield Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, RIVER_BLOCK)
            x += BLOCK_WIDTH
        y += BLOCK_HEIGHT
        x = 0


class Block(Sprite):
    offset_x= OFFSET_X
    offset_y= OFFSET_Y
    offset_idx = 1
    height_block = HEIGHT_HERO
    restart_game = False

    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)

        self.x_static = self.x
        self.y_static = self.y
        self.image = self._load_image(image_name)

    block_list = []

    @classmethod
    def init(cls):
        cls.offset_idx = 1
        cls.offset_count = 1
        cls.block_list = [block for block in map_generator(GAME_MAP)]
        for idx, block_item in enumerate(cls.block_list):
            cls.offset_idx += idx

        cls.offset_count = cls.offset_y + cls.height_block * cls.offset_idx

    def collide_hero_up(self, hero):
        if self.colliderect(hero):
            if self.image_name == BLOCK:
                if self.y + self.offset_count >= hero.bottom_y - self.height - 5:
                    return True
            else:
                self.offset_idx = 1
                self.offset_count = 1
                self.x, self.y = (OFFSET_X, -OFFSET_Y)
                self.x_static, self.y_static = (OFFSET_X, -OFFSET_Y)
                Block.init()
                hero.x, hero.y = WIDTH_HERO, HEIGHT_HERO
                print(f"self.x: {self.x}, self.y: -{self.y}")
                print(f"self.x_static: {self.x_static}, self.y_static: -{self.y_static}")
                print(f"cls.offset_idx : {self.offset_idx }, cls.offset_count: -{self.offset_count}")
                return False



    def collide_hero_left(self, hero):
        if self.colliderect(hero):
            if self.x <= hero.right_x and hero.x < self.x and not self.y + self.height >= hero.bottom_y + 5:
                return True

    def collide_hero_right(self, hero):
        if self.colliderect(hero):
            if self.right_x >= hero.x and hero.right_x > self.right_x and not self.y + self.height >= hero.bottom_y + 5:
                return True

    def _draw(self):
        screen.blit(self.image, (self.x, self.y))

    def _move(self):
        self.x = self.x_static - self.offset_x
        self.y = self.y_static - self.offset_y

    @classmethod
    def all_block_process(cls):
        for block in cls.block_list:
            block.process()

Block.init()
