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


        self.all_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        self.possible_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        self.average_change_direction_speed = 100
        self.change_direction_initial_timer = 20
        self.change_direction_timer = self.change_direction_initial_timer

        self.change_random_speed = 5
        self.random_speed_NS = 0
        self.random_speed_EW = 0

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

    def get_hitbox(self):
        return self.hitbox

    #   ----------- Initial position with middle included ------------
    def set_position_out_of_screen(self):
        if self.direction == 'S': # coming from above
            self.sprite.y = - self.sprite.height
            self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
            return
        if self.direction == 'N': # coming from below
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

    # def random_speed_NS_possibility(self):
    #     if (close_to_north() and (self.direction == 'E' or self.direction == 'W')):
    #         return [3]
    #     if (close_to_south() and (self.direction == 'E' or self.direction == 'W')):
    #         return [-3]
    #     return [-3, 3]
    
    # def random_speed_EW_possibility(self):
    #     if (close_to_east() and (self.direction == 'N' or self.direction == 'S')):
    #         return [-3]
    #     if (close_to_west() and (self.direction == 'N' or self.direction == 'S')):
    #         return [3]
    #     return [-3, 3]

    def random_side_speed(self, delta_time):
        self.change_random_speed += (2* delta_time)
        if self.change_random_speed >= (10 + random.randint(-3, 3)):
            self.random_speed_NS = random.choice([3, -3]) * delta_time
            self.random_speed_EW = random.choice([3, -3]) * delta_time
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
        # if pygame.sprite.collide_mask(self.sprite, self.island):
        if Sprite_utils.collide_mask_rect(self.hitbox, self.island):
            return True
        return False

    # def is_close_to_above(self):
    #     print()
        # if self.hitbox.y < 50:
        # if self.direction == 'N':
        #     self.direction = random.choice('NE', 'NW')

    def remove_directions(self, letters):
        for letter in letters:
            self.possible_directions.remove(letter)

    def change_direction(self):
        directions = get_around_string_list(self.possible_directions, self.direction)
        self.direction = random.choice(directions)
    
    def is_close_to_below(self):
        if self.hitbox.y > HEIGHT - 200 and self.direction == 'S':
            self.change_direction()
            return self.remove_directions('S')
        # print(self.hitbox.y)
        if self.hitbox.y > HEIGHT - 150 and (self.direction == 'SW' or self.direction == 'SE'):
            self.remove_directions(['SE', 'S', 'SW'])
            return self.change_direction()
        self.possible_directions = self.all_directions


    # def about_to_leave_map(self):
    #     self.all_directions


    #     if self.sprite.x +=

    def move(self, delta_time):
        if not self.collide_with_island():
            # if self.about_to_leave_map():
            self.is_close_to_below()
                

            # if self.change_direction_timer > 0:
            #     self.change_direction_timer -= self.change_direction_speed * delta_time
            # else:
            #     random_timer = self.generate_random_num_around(self.)
            self.move_to_a_direction(self.direction, delta_time)
