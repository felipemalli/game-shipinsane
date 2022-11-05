import pygame
from PPlay.sprite import Sprite

from .cannon_ball import Cannon_ball


class Cannon:
    def __init__(self, initial_angle, sprite, x, y):
        self.cannon_ball_list = []

        self.sprite = sprite
        self.sprite.x = x
        self.sprite.y = y

        self.image = self.sprite.image
        self.rect = self.sprite.image.get_rect()
        self.rect.center=(self.sprite.x - (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))

        self.initial_angle = initial_angle
        self.angle = 0

    def get_relative_angle(self):
        return self.angle

    def get_absolute_angle(self):
        return self.initial_angle + self.angle

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
        shot_speed = 0.5
        cannon_ball = Cannon_ball(shot_speed, self)
        self.cannon_ball_list.append(cannon_ball)

    def remove_cannon_ball(self, cannon_ball):
        self.cannon_ball_list.remove(cannon_ball)

    def render_shots(self):
        for cannon_ball in self.cannon_ball_list:
            cannon_ball.draw()
            cannon_ball.move_with_angle()

        # if pygame.sprite.collide_mask(cannon_ball.cannon_ball_spt, self.island):
        #     print('colidiu')
        # else:
        #     print('nao')
