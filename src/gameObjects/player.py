import os
import sys

import pygame
from PPlay.keyboard import Keyboard

keyboard = Keyboard()

sys.path.insert(0, os.path.abspath("../../")) # src/
from src.pages.game_parts.window_game import island
from src.utils.sprite_direction import sprite_direction


class Player:
    def __init__(self):
        self.sprite = sprite_direction('../assets/', 'player', 'S', island.x + island.width / 2 - 35, island.y + island.height / 2 - 25)
        self.cannon_ammo = 3
        self.life = 100

    def get_sprite(self):
        return self.sprite

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

    def movement(self):
        if keyboard.key_pressed("W"):
            self.sprite.y -= 0.5
        elif keyboard.key_pressed("A"):
            self.sprite.x -= 0.5
        elif keyboard.key_pressed("S"):           
            self.sprite.y += 0.5
        elif keyboard.key_pressed("D"):           
            self.sprite.x += 0.5

        self.player_direction()
