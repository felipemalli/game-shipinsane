import math

import pygame
from PPlay.keyboard import Keyboard
from pygame import mixer, sprite

from .cannon_ball import Cannon_ball, I_Cannon_ball
from .fleet_of_ships import Fleet_of_ships

keyboard = Keyboard()

from src.pages.game_parts.window_game import window
from utils.smoke_effect import SmokeParticle
from utils.sprite_utils import Sprite_utils

from gameObjects.explosion import Explosion


class Cannon(I_Cannon_ball):
    def __init__(self, initial_angle, sprite_c, x, y):
        self.cannon_ball_list = []
        self.shot_cooldown = 0
        self.shot_speed = 150
        self.damage = 20
        self.sound_explosion = self.render_sound_explosion()

        self.sprite = sprite_c
        self.sprite.x = x
        self.sprite.y = y

        self.initial_angle = initial_angle
        self.angle = 0

        self.image = self.sprite.image
        self.rect = self.sprite.image.get_rect()
        self.rect.center = (self.sprite.x - (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))
        self.rot_image = self.image
        self.rot_rect = self.rect

        self.is_shooting = False
        self.smoke = SmokeParticle(self.initial_cannon_ball_x(), self.initial_cannon_ball_y(), 0, 0, 0, 0.1, 0, '../assets/exp5.png')
        self.explosion_group = sprite.Group()

    def get_sprite(self):
        return self.sprite
    def get_relative_angle(self):
        return self.angle
    def get_absolute_angle(self):
        return self.initial_angle + self.angle
    def get_rect(self):
        return self.rect

    def render_sound_explosion(self):
        sound = pygame.mixer.Sound("../assets/sounds/Explosion 4.ogg")
        pygame.mixer.Sound.set_volume(sound, 0.5)
        return sound

    def render_smoke(self):
        self.smoke.update()
        self.smoke.draw()

    """Ensure that cannon ball will come out in the perfect position"""
    def initial_cannon_ball_x(self):
        return self.rect.centerx - (6 * (math.cos(math.radians(90 - self.get_relative_angle()))) + (10 * (math.cos(math.radians(90 - self.get_absolute_angle())))) - 1)
    def initial_cannon_ball_y(self):
        return self.rect.centery - (6 * (math.sin(math.radians(90 - self.get_relative_angle()))) + (10 * (math.sin(math.radians(90 - self.get_absolute_angle())))) - 1)

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
        cannon_ball = Cannon_ball(self.initial_cannon_ball_x(), self.initial_cannon_ball_y(), self.shot_speed, self, self.get_absolute_angle())
        self.cannon_ball_list.append(cannon_ball)

    def remove_cannon_ball(self, cannon_ball):
        self.cannon_ball_list.remove(cannon_ball)

    def render_shots(self, delta_time):
        for cannon_ball in self.cannon_ball_list:
            cannon_ball.draw()
            cannon_ball.move_with_angle(delta_time)

            enemy_ship = Sprite_utils.sprite_collide_obj_list(cannon_ball.sprite, Fleet_of_ships.enemy_ships)
            if enemy_ship:
                explosion = Explosion(cannon_ball.sprite.x, cannon_ball.sprite.y)
                self.explosion_group.add(explosion)
                self.remove_cannon_ball(cannon_ball)
                enemy_ship.take_damage(self.damage)
        
        if self.shot_cooldown > 0:
            self.shot_cooldown -= delta_time

        self.explosion_group.draw(window.get_screen())
        self.explosion_group.update()
        if self.is_shooting and self.smoke.alive: self.render_smoke()

    def render(self):
        window.get_screen().blit(self.rot_image, self.rot_rect)

    def control(self, player_object, clockwise_key, anticlockwise_key):
        rot_image, rot_rect = self.rot_center()

        if keyboard.key_pressed(clockwise_key):
            rot_image, rot_rect = self.move_clockwise()

        if keyboard.key_pressed(anticlockwise_key):
            rot_image, rot_rect = self.move_anticlockwise()

        if keyboard.key_pressed("SPACE") and self.shot_cooldown <= 0 and player_object.get_cannon_ammo() > 0:
            self.is_shooting = True
            self.smoke = SmokeParticle(self.initial_cannon_ball_x(), self.initial_cannon_ball_y(), 0, 1, 2, 0.1, 0, '../assets/exp5.png')
            self.sound_explosion.play()
            player_object.reduce_cannon_ammo()
            self.shot()
            self.shot_cooldown = 1
        
        self.rot_image = rot_image
        self.rot_rect = rot_rect
