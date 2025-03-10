from constans import COIN_SPEED, HEIGHT_COIN, WIDTH_COIN
from images import COIN
from sprite import Sprite


class Coin(Sprite):
    coins_list = []
    count_coin = 0
    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)
        self.image = self._load_image(image_name)

    def _move(self):
        self.y -= COIN_SPEED

    @classmethod
    def create_by_block(cls, block):
        obj = cls(block.x, block.y, WIDTH_COIN, HEIGHT_COIN, COIN)
        cls.coins_list.append(obj)
        cls.count_coin += 1
        return obj, cls.count_coin

    @classmethod
    def all_coin_process(cls):
        for coin in cls.coins_list:
            coin.process()
