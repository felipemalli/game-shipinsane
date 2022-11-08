import os
import random
import sys

from PPlay.sprite import Sprite

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import HEIGHT, WIDTH
from src.utils.sprite_direction import sprite_direction


class Ship:
    def __init__(self, island, life, speed):
        self.island = island
        self.life = life
        self.speed = speed
        
        self.direction = random.choice(['N', 'S', 'E', 'W'])
        self.sprite = sprite_direction('../assets/', 'enemy_ship', self.direction)
        self.set_position_out_of_screen()

        self.average_change_direction_speed = 100
        self.change_direction_initial_timer = 20
        self.change_direction_timer = self.change_direction_initial_timer

    def draw(self):
        self.sprite.draw()

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

    def move_to_a_direction(self, direction, delta_time):
        if 'N' in direction:
            self.sprite.y -= self.speed * delta_time
        if 'S' in direction:
            self.sprite.y += self.speed * delta_time
        if 'E' in direction:
            self.sprite.x += self.speed * delta_time
        if 'W' in direction:
            self.sprite.x -= self.speed * delta_time

    def collide_with_island(self):
        if self.sprite.collided(self.island):
            print('Barco colidiu com a ilha!')
            return True
        return False

    def move(self, delta_time):
        # if not self.collide_with_island():
        #     if self.change_direction_timer > 0:
        #         self.change_direction_timer -= self.change_direction_speed * delta_time
        #     else:
                # random_timer = self.generate_random_num_around(self.)
                self.collide_with_island()
                self.move_to_a_direction(self.direction, delta_time)
