import math
import os
import sys

from PPlay.sprite import Sprite

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import HEIGHT, WIDTH


class Cannon_ball:
    def __init__(self, speed, cannon_object):
        self.cannon_object = cannon_object
        self.cannon_rect = cannon_object.get_rect()
        self.cannon_absolute_angle = cannon_object.get_absolute_angle()
        self.cannon_relative_angle = cannon_object.get_relative_angle()

        self.sprite = Sprite("../assets/cannon_ball.png")
        self.sprite.x = self.cannon_rect.centerx - (self.sprite.width / 2) - (6 * (math.cos(math.radians(90 - self.cannon_relative_angle))) + (10 * (math.cos(math.radians(90 - self.cannon_absolute_angle)))) - 1)
        self.sprite.y = self.cannon_rect.centery - (self.sprite.width / 2) - (6 * (math.sin(math.radians(90 - self.cannon_relative_angle))) + (10 * (math.sin(math.radians(90 - self.cannon_absolute_angle)))) - 1)
        self.speed = speed

    def draw(self):
        self.sprite.draw()

    def is_out_of_screen(self):
        if self.sprite.y + self.sprite.height < 0 or self.sprite.y > HEIGHT:
            return True
        if self.sprite.x < 0 or self.sprite.x > WIDTH:
            return True
        return False

    def move_with_angle(self, delta_time):
        if self.is_out_of_screen(): self.cannon_object.remove_cannon_ball(self)
        angle = self.cannon_absolute_angle
        radAngle = math.radians(90 - angle)
        self.sprite.x -= self.speed * math.cos(radAngle) * delta_time
        self.sprite.y -= self.speed * math.sin(radAngle) * delta_time
