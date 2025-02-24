import pygame
from blocks import Block
from constans import FRAME_DELAY_RUN, GRAVITY_SPEED, JUMP_COUNTER_DEFAULT, JUMP_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED
from images import JUMP_HERO, JUMP_SKINNY_HERO, RUN_HERO_1, RUN_HERO_2, RUN_SKINNY_HERO_1, RUN_SKINNY_HERO_2, STANDING_HERO, STANDING_SKINNY_HERO
from sprite import Sprite

class Hero(Sprite):
    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)
        self.gravity_speed = GRAVITY_SPEED
        self.gravity_active = True
        self.speed = SPEED

        self.is_skinny = False
        self.is_running = False

        self.jump_speed = JUMP_SPEED
        self.jump_active = False
        self.jump_counter_default = JUMP_COUNTER_DEFAULT
        self.jump_counter_current = self.jump_counter_default

        self.running_frames = [
            self._load_image(RUN_HERO_1),
            self._load_image(RUN_HERO_2)
        ]
        self.skinny_running_frames = [
            self._load_image(RUN_SKINNY_HERO_1),
            self._load_image(RUN_SKINNY_HERO_2)
        ]
        self.standing_frame = self._load_image(STANDING_HERO)
        self.skinny_standing_frame = self._load_image(STANDING_SKINNY_HERO)
        self.jumping_frame = self._load_image(JUMP_HERO)
        self.skinny_jumping_frame = self._load_image(JUMP_SKINNY_HERO)
        self.current_frame = 0
        self.image = self.standing_frame
        self.last_frame_update = pygame.time.get_ticks()
        self.frame_delay = FRAME_DELAY_RUN

        self.running_frames_left = [
            pygame.transform.flip(self.running_frames[0], True, False),
            pygame.transform.flip(self.running_frames[1], True, False)
        ]
        self.skinny_running_frames_left = [
            pygame.transform.flip(self.skinny_running_frames[0], True, False),
            pygame.transform.flip(self.skinny_running_frames[1], True, False)
        ]

    def _gravity(self):
        '''
        Handles the gravity effect by checking if the hero is on the floor.
        If not, it applies gravity to the hero's vertical position.
        '''
        if not self._is_on_floor() and not self.jump_active:
            self.y += self.gravity_speed
            self.gravity_active = True
        else:
            self.gravity_active = False

    def _move(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_LEFT]:
            self._move_left()
        elif keyboard[pygame.K_RIGHT]:
            self._move_right()
        else:
            self._stop_running()
        if keyboard[pygame.K_UP]:
            self._start_jump()

    def _is_on_floor(self):
        if self.bottom_y >= SCREEN_HEIGHT or any([block.collide_hero_up(main_hero) for block in Block.block_list]):
            return True

    def _start_jump(self):
        if self._is_on_floor() and not self.jump_active:
            self.jump_active = True
            if not self.is_skinny:
                self.image = self.jumping_frame
            else:
                self.image = self.skinny_jumping_frame
        elif not self._is_on_floor():
            if not self.is_skinny:
                self.image = self.jumping_frame
            else:
                self.image = self.skinny_jumping_frame

    def _jump_process(self):
        if self.jump_active:
            if self.jump_counter_current != 0:
                self.jump_counter_current -= 1
                self.y -= self.jump_speed
            else:
                self.jump_counter_current = self.jump_counter_default
                self.jump_active = False

    def _move_right(self):
        if self.right_x < SCREEN_WIDTH and not any([block.collide_hero_left(main_hero) for block in Block.block_list]):
            self.x += self.speed
            self.is_running = True
            self._update_sprite()

    def _move_left(self):
        if self.x > 0 and not any([block.collide_hero_right(main_hero) for block in Block.block_list]):
            self.x -= self.speed
            self.is_running = True
            self._update_sprite()

    def _stop_running(self):
        self.is_running = False
        if self._is_on_floor():
            if not self.is_skinny:
                self.image = self.standing_frame
            else:
                self.image = self.skinny_standing_frame

    def process(self):
        super().process()
        self._jump_process()

    def _update_sprite(self):
        if self.is_running:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_frame_update > self.frame_delay:
                if not self.is_skinny:
                    self.current_frame = (self.current_frame + 1) % len(self.running_frames)
                else:
                    self.current_frame = (self.current_frame + 1) % len(self.skinny_running_frames)
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    if not self.is_skinny:
                        self.image = self.running_frames_left[self.current_frame]
                    else:
                        self.image = self.skinny_running_frames_left[self.current_frame]
                else:
                    if not self.is_skinny:
                        self.image = self.running_frames[self.current_frame]
                    else:
                        self.image = self.skinny_running_frames[self.current_frame]
                self.last_frame_update = current_time


main_hero = Hero(50,50, 40,50, 'images/heroes/fat_hero.png')
