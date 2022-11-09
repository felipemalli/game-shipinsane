import os
import random
import sys

import pygame

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window
from src.utils.sprite_utilities import Sprite_utils


class Ship:
    def __init__(self, island, life, speed):
        self.island = island
        self.life = life
        self.speed = speed
        
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.direction = random.choice(['N', 'S', 'E', 'W'])
        self.sprite = Sprite_utils.sprite_direction('../assets/', 'enemy_ship', self.direction)
        self.set_position_out_of_screen()

        self.average_change_direction_speed = 100
        self.change_direction_initial_timer = 20
        self.change_direction_timer = self.change_direction_initial_timer

    def draw(self):
        if self.direction == "E" or self.direction == "W":
            self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 50, self.sprite.width - 30, self.sprite.height - 50)
            self.hitbox.collidedictall
            pygame.draw.rect(window.get_screen(), (255,0,0), self.hitbox, 2)
        elif self.direction == "N":
            self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 10, self.sprite.width, self.sprite.height - 10)
            pygame.draw.rect(window.get_screen(), (255,0,0), self.hitbox, 2)
        elif self.direction == "S":
            self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 35, self.sprite.width, self.sprite.height - 35)
            pygame.draw.rect(window.get_screen(), (255,0,0), self.hitbox, 2)
        self.sprite.draw()

    def get_hitbox(self):
        return self.hitbox

    #   ----------- Initial position with middle included ------------
    def set_position_out_of_screen(self):
        if self.direction == 'S': # coming from up
            self.sprite.y = - self.sprite.height
            self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
            return
        if self.direction == 'N': # coming from down
            self.sprite.y = HEIGHT
            self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
            return
        if self.direction == 'E': # coming from left
            self.sprite.y = random.randint(0, HEIGHT - self.sprite.height)
            self.sprite.x = - self.sprite.width
            return
        if self.direction == 'W': # coming from right
            self.sprite.y = random.randint(0, HEIGHT - self.sprite.height)
            self.sprite.x = WIDTH
            return

    # def set_position_out_of_screen(self):
    #     side = random.choice('left or up', 'right or down')
    #     if self.direction == 'S': # coming from up
    #         self.sprite.y = - self.sprite.height
    #         if 'left' in side: self.sprite.x = random.randint(0, self.island.x - self.sprite.x)
    #         elif 'right' in side: self.sprite.x = random.randint(self.island.x + self.island.width + self.sprite.x, WIDTH - self.sprite.width)
    #         return
    #     if self.direction == 'N': # coming from down
    #         self.sprite.y = HEIGHT
    #         self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
    #         return
    #     if self.direction == 'E': # coming from left
    #         self.sprite.y = random.randint(0, HEIGHT - self.sprite.height)
    #         self.sprite.x = - self.sprite.width
    #         return
    #     if self.direction == 'W': # coming from right
    #         self.sprite.y = random.randint(0, HEIGHT - self.sprite.height)
    #         self.sprite.x = WIDTH
    #         return

    def move_to_a_direction(self, direction, delta_time):
        if 'N' in direction:
            self.sprite.y -= self.speed * delta_time
        if 'S' in direction:
            self.sprite.y += self.speed * delta_time
        if 'E' in direction:
            self.sprite.x += self.speed * delta_time
        if 'W' in direction:
            self.sprite.x -= self.speed * delta_time

    # def collide_mask_rect(self, left, right):
    #     xoffset = right.rect[0] - left.x
    #     yoffset = right.rect[1] - left.y
    #     try:
    #         leftmask = left.mask
    #     except AttributeError:
    #         leftmask = pygame.mask.Mask(left.size, True)
    #     try:
    #         rightmask = right.mask
    #     except AttributeError:
    #         rightmask = pygame.mask.from_surface(right.image)
    #     return leftmask.overlap(rightmask, (xoffset, yoffset))

    def collide_with_island(self):
        # if pygame.sprite.collide_mask(self.sprite, self.island):
        if Sprite_utils.collide_mask_rect(self.hitbox, self.island):
            return True
        return False

    # def about_to_leave_map(self):
    #     if self.sprite.x +=

    def move(self, delta_time):
        if not self.collide_with_island():
            # if self.about_to_leave_map():
                

            # if self.change_direction_timer > 0:
            #     self.change_direction_timer -= self.change_direction_speed * delta_time
            # else:
            #     random_timer = self.generate_random_num_around(self.)
            self.move_to_a_direction(self.direction, delta_time)
