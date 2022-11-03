import pygame
from PPlay.sprite import Sprite

from .cannon_ball import Cannon_ball


class Cannon:
    def __init__(self, sprite, x, y):
        self.cannon_ball_list = []

        self.cannon_spt = sprite
        self.cannon_spt.x = x
        self.cannon_spt.y = y

        self.image = self.cannon_spt.image
        self.rect = self.cannon_spt.image.get_rect()
        self.rect.center=(self.cannon_spt.x - (self.cannon_spt.width / 2), self.cannon_spt.y + (self.cannon_spt.height / 2))

        self.angle = 0

    def get_angle(self):
        return self.angle

    def get_rect(self):
        return self.rect

    def get_img_rect(self):
        return self.image, self.rect

    def rot_center(self):
        rot_image = pygame.transform.rotate(self.image, self.angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        return rot_image,rot_rect

    def move_clockwise(self):
        if self.angle > -60:
            self.angle -= 0.35
        return self.rot_center()

    def move_anticlockwise(self):
        if self.angle < 60:
            self.angle += 0.35
        return self.rot_center()

    def shot(self):
        shot_speed = 1
        cannon_ball = Cannon_ball(shot_speed, self)
        self.cannon_ball_list.append(cannon_ball)

    def remove_cannon_ball(self, cannon_ball):
        print(cannon_ball)
        self.cannon_ball_list.remove(cannon_ball)

    def render_shots(self):
        for cannon_ball in self.cannon_ball_list:
            cannon_ball.draw()
            cannon_ball.move_with_angle()
