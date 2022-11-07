import os
import sys

import pygame
from PPlay.keyboard import Keyboard
from PPlay.sprite import Sprite

keyboard = Keyboard()

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window
from src.utils.sprite_direction import sprite_direction


class Player:
    def __init__(self, island):
        self.island = island
        self.sprite = sprite_direction('../assets/', 'player', 'S', island.x + island.width / 2 - 35, island.y + island.height / 2 - 25)
        self.cannon_ammo = 3
        self.life = 100

        self.key_W = 'free'
        self.key_A = 'free'
        self.key_S = 'free'
        self.key_D = 'free'

    def set_sprite_x(self, x):
        self.sprite.x = x

    def set_sprite_y(self, y):
        self.sprite.y = y

    def reduce_cannon_ammo(self):
        if self.cannon_ammo > 0:
            self.cannon_ammo -= 1

    def set_cannon_ammo(self, cannon_ammo):
        self.cannon_ammo = cannon_ammo

    def get_cannon_ammo(self):
        return self.cannon_ammo

    def get_sprite(self):
        return self.sprite

    def get_x(self):
        return self.sprite.x

    def player_direction(self):
        if keyboard.key_pressed("W") and keyboard.key_pressed("D"):
            self.sprite = sprite_direction('../assets/', 'player', 'NE', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("S") and keyboard.key_pressed("D"):
            self.sprite = sprite_direction('../assets/', 'player', 'SE', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("S") and keyboard.key_pressed("A"):
            self.sprite = sprite_direction('../assets/', 'player', 'SW', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("W") and keyboard.key_pressed("A"):
            self.sprite = sprite_direction('../assets/', 'player', 'NW', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("W"):
            self.sprite = sprite_direction('../assets/', 'player', 'N', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("A"):
            self.sprite = sprite_direction('../assets/', 'player', 'W', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("S"):
            self.sprite = sprite_direction('../assets/', 'player', 'S', self.sprite.x, self.sprite.y)
        elif keyboard.key_pressed("D"):
            self.sprite = sprite_direction('../assets/', 'player', 'E', self.sprite.x, self.sprite.y)

    def is_inside_island(self):
        if pygame.sprite.collide_mask(self.sprite, self.island):
            return True

    def block_if_outside_island(self, fake_sprite, key):
        key_attribute = 'key_' + key
        if not pygame.sprite.collide_mask(fake_sprite.get_sprite(), self.island):
            setattr(self, key_attribute, 'blocked')
        else:
            setattr(self, key_attribute, 'free')

    def check_if_outside_island(self):
        fake_x = self.sprite.x
        fake_y = self.sprite.y
        fake_sprite = Player(self.island)

        fake_sprite.get_sprite().x = fake_x + 25
        fake_sprite.get_sprite().y = fake_y
        fake_sprite.get_sprite().draw()
        self.block_if_outside_island(fake_sprite, 'D')
    
        if self.key_D == 'free':
            fake_sprite.get_sprite().x = fake_x + 25
            fake_sprite.get_sprite().y = fake_y + 36
            fake_sprite.get_sprite().draw()
            self.block_if_outside_island(fake_sprite, 'D')

        fake_sprite.get_sprite().x = fake_x - 25
        fake_sprite.get_sprite().y = fake_y
        fake_sprite.get_sprite().draw()
        self.block_if_outside_island(fake_sprite, 'A')

        if self.key_A == 'free':
            fake_sprite.get_sprite().x = fake_x - 25
            fake_sprite.get_sprite().y = fake_y + 36
            fake_sprite.get_sprite().draw()
            self.block_if_outside_island(fake_sprite, 'A')

        fake_sprite.get_sprite().x = fake_x
        fake_sprite.get_sprite().y = fake_y - 5
        fake_sprite.get_sprite().draw()
        self.block_if_outside_island(fake_sprite, 'W')

        fake_sprite.get_sprite().x = fake_x
        fake_sprite.get_sprite().y = fake_y + 38
        fake_sprite.get_sprite().draw()
        self.block_if_outside_island(fake_sprite, 'S')
        
    def movement(self):
        if keyboard.key_pressed("W") and self.key_W == 'free':
            self.sprite.y -= 0.7
            self.check_if_outside_island()
        if keyboard.key_pressed("A") and self.key_A == 'free':
            self.sprite.x -= 0.7
            self.check_if_outside_island()
        if keyboard.key_pressed("S") and self.key_S == 'free':
            self.sprite.y += 0.7
            self.check_if_outside_island()
        if keyboard.key_pressed("D") and self.key_D == 'free':
            self.sprite.x += 0.7
            self.check_if_outside_island()
        
        self.player_direction()

    def reload_ammo(self):
        font = pygame.font.SysFont("Arial", 30, False, False)
        text = font.render("Press R to reload", False, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT - 100))
        window.get_screen().blit(text, text_rect)
        
        if keyboard.key_pressed("R"):
            self.set_cannon_ammo(3)
