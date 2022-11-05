import math

from PPlay.sprite import Sprite


class Cannon_ball:
    def __init__(self, speed, cannon_object):
        self.cannon_object = cannon_object
        self.cannon_rect = cannon_object.get_rect()
        self.cannon_absolute_angle = cannon_object.get_absolute_angle()
        self.cannon_relative_angle = cannon_object.get_relative_angle()

        self.cannon_ball_spt = Sprite("../assets/cannon_ball.png")
        self.cannon_ball_spt.x = self.cannon_rect.centerx - (self.cannon_ball_spt.width / 2) - (6 * (math.cos(math.radians(90 - self.cannon_relative_angle))) + (10 * (math.cos(math.radians(90 - self.cannon_absolute_angle)))) - 1)
        self.cannon_ball_spt.y = self.cannon_rect.centery - (self.cannon_ball_spt.width / 2) - (6 * (math.sin(math.radians(90 - self.cannon_relative_angle))) + (10 * (math.sin(math.radians(90 - self.cannon_absolute_angle)))) - 1)
        self.speed = speed                  # speed with delta_time included!

    def draw(self):
        self.cannon_ball_spt.draw()

    def is_out_of_screen(self):
        WIDTH, HEIGHT = 1920, 1080
        if self.cannon_ball_spt.y + self.cannon_ball_spt.height < 0 or self.cannon_ball_spt.y > HEIGHT:
            return True
        if self.cannon_ball_spt.x < 0 or self.cannon_ball_spt.x > WIDTH:
            return True
        return False

    def move_with_angle(self):
        if self.is_out_of_screen(): self.cannon_object.remove_cannon_ball(self)
        angle = self.cannon_absolute_angle
        radAngle = math.radians(90 - angle)
        self.cannon_ball_spt.x -= self.speed * math.cos(radAngle)
        self.cannon_ball_spt.y -= self.speed * math.sin(radAngle)
