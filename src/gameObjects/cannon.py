import pygame
from PPlay.sprite import Sprite


class Cannon:
    def __init__(self, sprite, x, y):
        self.cannon_list = []

        self.cannon_spt = sprite
        self.cannon_spt.x = x
        self.cannon_spt.y = y

        self.image = self.cannon_spt.image
        self.rect = self.cannon_spt.image.get_rect()
        self.rect.center=(self.cannon_spt.x - (self.cannon_spt.width / 2), self.cannon_spt.y + (self.cannon_spt.height / 2))

        self.angle = 0

    def get_img_rect(self):
        return self.image, self.rect

    def rot_center(self):
        rot_image = pygame.transform.rotate(self.image, self.angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        return rot_image,rot_rect

    def move_angle_anticlockwise(self):
        if self.angle < 60:
            self.angle += 1
        return self.rot_center()

    def move_angle_clockwise(self):
        if self.angle > -60:
            self.angle -= 1
        return self.rot_center()

    def get_is_on_screen(self):
        return self.is_on_screen

    def move_clockwise(self):
        self.angle -= 1
