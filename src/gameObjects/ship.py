import os
import random
import sys

import pygame

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window
from src.utils.ship_moviment import get_around_string_list
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

        self.all_directions = ["N", "NW", "W", "SW", "S", "SE", "E", "NE"]
        self.direction_dict = { direction: True for direction in self.all_directions }

        self.average_change_direction_speed = 100
        self.change_direction_initial_timer = 20
        self.change_direction_timer = self.change_direction_initial_timer

        self.random_speed_variation = 10
        self.change_random_speed = 5
        self.random_speed_NS = 0
        self.random_speed_EW = 0

        self.close_value = 150
        self.too_close_value = 50

    def reduce_life(self):
        self.life -= 1

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

    # """Initial position with middle included"""
    # def set_position_out_of_screen(self):
    #     if self.direction == 'S': # coming from above
    #         self.sprite.y = - self.sprite.height
    #         self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
    #         return
    #     if self.direction == 'N': # coming from below
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

    #Initial position with middle not included
    def set_position_out_of_screen(self):
        side = random.choice(['left or up', 'right or down'])
        space_ship_island = 50
        if self.direction == 'S': # coming from up
            self.sprite.y = - self.sprite.height
            if 'left' in side: self.sprite.x = random.randint(0, self.island.x - self.sprite.width - space_ship_island)
            elif 'right' in side: self.sprite.x = random.randint(self.island.x + self.island.width + space_ship_island, WIDTH - self.sprite.width)
            return
        if self.direction == 'N': # coming from down
            self.sprite.y = HEIGHT
            if 'left' in side: self.sprite.x = random.randint(0, self.island.x - self.sprite.width - space_ship_island)
            elif 'right' in side: self.sprite.x = random.randint(self.island.x + self.island.width + space_ship_island, WIDTH - self.sprite.width)
            return
        if self.direction == 'E': # coming from left
            self.sprite.x = - self.sprite.width
            if 'up' in side: self.sprite.y = random.randint(0, self.island.y - self.sprite.height - space_ship_island)
            elif 'down' in side: self.sprite.y = random.randint(self.island.y + self.island.height + space_ship_island, HEIGHT - self.sprite.height)
            return
        if self.direction == 'W': # coming from right
            self.sprite.x = WIDTH
            if 'up' in side: self.sprite.y = random.randint(0, self.island.y - self.sprite.height - space_ship_island)
            elif 'down' in side: self.sprite.y = random.randint(self.island.y + self.island.height + space_ship_island, HEIGHT - self.sprite.height)
            return

    def is_close_to_S(self):
        if self.hitbox.y + self.hitbox.height > HEIGHT - self.close_value:
            return True

    def is_too_close_to_S(self):
        if self.hitbox.y + self.hitbox.height > HEIGHT - self.too_close_value:
            return True

    def is_close_to_N(self):
        if self.hitbox.y < self.close_value:
            return True

    def is_too_close_to_N(self):
        if self.hitbox.y < self.too_close_value:  
            return True

    def is_close_to_E(self):
        if self.hitbox.x + self.hitbox.width > WIDTH - self.close_value:
            return True

    def is_too_close_to_E(self):
        if self.hitbox.x + self.hitbox.width > WIDTH - self.too_close_value:  
            return True

    def is_close_to_W(self):
        if self.hitbox.x < self.close_value:
            return True

    def is_too_close_to_W(self):
        if self.hitbox.x < self.too_close_value:  
            return True

    def random_speed_NS_possibility(self):
        if (self.is_too_close_to_N() and (self.direction == 'E' or self.direction == 'W')):
            return [self.random_speed_variation]
        if (self.is_too_close_to_S() and (self.direction == 'E' or self.direction == 'W')):
            return [-self.random_speed_variation]
        return [-self.random_speed_variation, self.random_speed_variation]
    
    def random_speed_EW_possibility(self):
        if (self.is_too_close_to_E() and (self.direction == 'N' or self.direction == 'S')):
            return [-self.random_speed_variation]
        if (self.is_too_close_to_W() and (self.direction == 'N' or self.direction == 'S')):
            return [self.random_speed_variation]
        return [-self.random_speed_variation, self.random_speed_variation]

    def random_side_speed(self, delta_time):
        self.change_random_speed += (2* delta_time)
        if self.change_random_speed >= (10 + random.randint(-3, 3)):
            self.random_speed_NS = random.choice(self.random_speed_NS_possibility()) * delta_time
            self.random_speed_EW = random.choice(self.random_speed_EW_possibility()) * delta_time
            self.change_random_speed = 0

    def move_to_a_direction(self, direction, delta_time):
        self.random_side_speed(delta_time)
        if 'N' in direction:
            self.sprite.y -= self.speed * delta_time
            self.sprite.x += self.random_speed_EW
        if 'S' in direction:
            self.sprite.y += self.speed * delta_time
            self.sprite.x += self.random_speed_EW
        if 'E' in direction:
            self.sprite.x += self.speed * delta_time
            self.sprite.y += self.random_speed_NS
        if 'W' in direction:
            self.sprite.x -= self.speed * delta_time
            self.sprite.y += self.random_speed_NS

    def collide_with_island(self):
        if Sprite_utils.collide_mask_rect(self.hitbox, self.island):
            return True
        return False

    def remove_directions(self, letters):
        for letter in letters:
            self.possible_directions.remove(letter)

    """Changes direction to the next or previous."""
    def change_direction(self):
        if len(self.direction) == 1: possible_directions = [direc for direc in self.all_directions if ((self.direction in direc) and (self.direction != direc))]
        else: possible_directions = [direc for direc in self.all_directions if ((self.direction[0] == direc) or (self.direction[1] == direc))]
        self.direction = random.choice(possible_directions)

    def move(self, delta_time):
        if not self.collide_with_island():

            # if self.change_direction_timer > 0:
            #     self.change_direction_timer -= self.change_direction_speed * delta_time
            # else:
            #     random_timer = self.generate_random_num_around(self.)
            self.move_to_a_direction(self.direction, delta_time)
