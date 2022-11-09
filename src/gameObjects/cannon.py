import os
import sys

import pygame
from PPlay.keyboard import Keyboard

from .cannon_ball import Cannon_ball
from .fleet_of_ships import Fleet_of_ships

keyboard = Keyboard()

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.utils.sprite_utilities import Sprite_utils


class Cannon:
    def __init__(self, initial_angle, sprite, x, y):
        self.cannon_ball_list = []
        self.shot_cooldown = 1
        self.shot_speed = 150

        self.sprite = sprite
        self.sprite.x = x
        self.sprite.y = y

        self.image = self.sprite.image
        self.rect = self.sprite.image.get_rect()
        self.rect.center=(self.sprite.x - (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))

        self.initial_angle = initial_angle
        self.angle = 0

    def get_sprite(self):
        return self.sprite
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
        self.sprite.x = rot_rect.x
        self.sprite.y = rot_rect.y
        return rot_image, rot_rect

    def move_clockwise(self):
        if self.angle > -50:
            self.angle -= 0.35
        return self.rot_center()

    def move_anticlockwise(self):
        if self.angle < 50:
            self.angle += 0.35
        return self.rot_center()

    def shot(self):
        cannon_ball = Cannon_ball(self.shot_speed, self)
        self.cannon_ball_list.append(cannon_ball)

    def remove_cannon_ball(self, cannon_ball):
        self.cannon_ball_list.remove(cannon_ball)

    def render_shots(self, delta_time):
        for cannon_ball in self.cannon_ball_list:
            cannon_ball.draw()
            cannon_ball.move_with_angle(delta_time)

            ship = Sprite_utils.sprite_collide_obj_list(cannon_ball.sprite, Fleet_of_ships.enemy_ships)
            if ship:
                self.remove_cannon_ball(cannon_ball)
                ship.reduce_life()

    def control(self, player_object, shot_timer, clockwise_key, anticlockwise_key):
        rot_image, rot_rect = self.rot_center()

        if keyboard.key_pressed(clockwise_key):
            rot_image, rot_rect = self.move_clockwise()

        if keyboard.key_pressed(anticlockwise_key):
            rot_image, rot_rect = self.move_anticlockwise()

        if keyboard.key_pressed("SPACE") and shot_timer < 0 and player_object.get_cannon_ammo() > 0:
            player_object.reduce_cannon_ammo()
            self.shot()
            return self.shot_cooldown, rot_image, rot_rect
        
        return shot_timer, rot_image, rot_rect
