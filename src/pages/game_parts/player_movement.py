import os
import sys

import pygame
from PPlay.keyboard import Keyboard

keyboard = Keyboard()

sys.path.insert(0, os.path.abspath("../"))
from utils.sprite_direction import sprite_direction


def player_direction(player):
    if keyboard.key_pressed("W") and keyboard.key_pressed("D"):
        return sprite_direction('../assets/', 'player', 'NE', player.x, player.y)
    if keyboard.key_pressed("S") and keyboard.key_pressed("D"):
        return sprite_direction('../assets/', 'player', 'SE', player.x, player.y)
    if keyboard.key_pressed("S") and keyboard.key_pressed("A"):
        return sprite_direction('../assets/', 'player', 'SW', player.x, player.y)
    if keyboard.key_pressed("W") and keyboard.key_pressed("A"):
        return sprite_direction('../assets/', 'player', 'NW', player.x, player.y)
    if keyboard.key_pressed("W"):
        return sprite_direction('../assets/', 'player', 'N', player.x, player.y)
    if keyboard.key_pressed("A"):
        return sprite_direction('../assets/', 'player', 'W', player.x, player.y)
    if keyboard.key_pressed("S"):
        return sprite_direction('../assets/', 'player', 'S', player.x, player.y)
    if keyboard.key_pressed("D"):
        return sprite_direction('../assets/', 'player', 'E', player.x, player.y)

    return player

def player_movement(player, island):
    player = player_direction(player)

    if keyboard.key_pressed("W"):
        player.y -= 0.5
    if keyboard.key_pressed("A"):
        player.x -= 0.5
    if keyboard.key_pressed("S"):           
        player.y += 0.5
    if keyboard.key_pressed("D"):           
        player.x += 0.5

    return player


    if pygame.sprite.collide_mask(cannon_ball.cannon_ball_spt, self.island):
        print('colidiu')
    else:
        print('nao')
