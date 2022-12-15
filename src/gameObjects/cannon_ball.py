import math
from abc import ABC, abstractmethod

from PPlay.sprite import Sprite
from src.pages.game_parts.window_game import HEIGHT, WIDTH


class I_Cannon_ball(ABC):
    @abstractmethod
    def remove_cannon_ball(self, cannon_ball):
        raise NotImplementedError

class Cannon_ball:
    def __init__(self, x, y, speed, cannon_object, angle = None):
        self.cannon_object = cannon_object
        self.angle = angle

        self.sprite = Sprite("../assets/images/cannon_ball.png")
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
        radAngle = math.radians(90 - self.angle)
        self.sprite.x -= self.speed * math.cos(radAngle) * delta_time
        self.sprite.y -= self.speed * math.sin(radAngle) * delta_time

    def move_with_position_direction(self, x_start, y_start, x_destination, y_destination, delta_time):
        if not self.angle:
            dx = x_start - x_destination
            dy = y_start - y_destination
            if dy == 0: dy = 0.01
            angle = math.atan(float(dx)/float(dy)) * 180/math.pi
            if dy < 0: angle += 180
            self.angle = angle

        self.move_with_angle(delta_time)
