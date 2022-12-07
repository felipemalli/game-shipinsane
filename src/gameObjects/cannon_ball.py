import math
import os
import sys

from PPlay.sprite import Sprite

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import HEIGHT, WIDTH


class Cannon_ball:
    def __init__(self, x, y, speed, cannon_object):
        self.cannon_object = cannon_object
        self.cannon_shot_angle = cannon_object.get_absolute_angle()

        self.sprite = Sprite("../assets/cannon_ball.png")
        self.sprite.x = x - (self.sprite.width / 2)
        self.sprite.y = y - (self.sprite.height / 2)
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
        angle = self.cannon_shot_angle
        radAngle = math.radians(90 - angle)
        self.sprite.x -= self.speed * math.cos(radAngle) * delta_time
        self.sprite.y -= self.speed * math.sin(radAngle) * delta_time
