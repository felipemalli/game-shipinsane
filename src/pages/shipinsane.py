import os
import sys

import pygame
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *

sys.path.insert(0, os.path.abspath("../"))
from gameObjects.cannon import Cannon
from gameObjects.cannon_ball import Cannon_ball


def init():
    WIDTH = 1920
    HEIGHT = 1080
    window = Window(WIDTH, HEIGHT)
    window.set_title("ShipInsane")
    window.set_background_color([0, 0, 0])

    #Carrega os sprites de cada objeto do jogo
    island = Sprite("../assets/island2.png", 1)
    sea = Sprite("../assets/mar.png", 1)
    enemy_pirate_1 = Sprite("../assets/enemy1.png", 1)
    enemy_pirate_2 = Sprite("../assets/enemy2.png", 1)
    player = Sprite("../assets/player.png", 1)
    enemy_ship_1 = Sprite("../assets/enemy_ship1.png")
    enemy_ship_2 = Sprite("../assets/enemy_ship2.png")
    # cannon1 = Sprite("../assets/cannon1.png")

    keyboard = Window.get_keyboard()

    #Configura as posiçoes dos elementos do jogo

    island.x = WIDTH / 2 - island.width / 2
    island.y = HEIGHT / 2 - island.height / 2

    # enemy_ship_1.x = 5 * WIDTH / 6
    # enemy_ship_1.y = island.x / 2 - 40
    # enemy_ship_2.x = island.x / 2 - 40
    # enemy_ship_2.y = 5 * HEIGHT / 7 
    # enemy_pirate_1.x = island.x + island.width / 2 
    # enemy_pirate_1.y = island.y + 50
    # enemy_pirate_2.x = island.x + island.width / 2 - 70
    # enemy_pirate_2.y = island.y + 80
    # player.x = island.x + island.width / 2 + 120
    # player.y = island.y + island.height / 2 - 60

    # cannon1.x = island.x + island.width / 2 - 15
    # cannon1.y = island.y + 10

    # cannon2.x = island.x + island.width / 2 + 130
    # cannon2.y = island.y + island.height / 2 - 70

    # cannon3.x = island.x + island.width / 2 - 50
    # cannon3.y = island.y + island.height - 50  

    # cannon4.x = island.x
    # cannon4.y = island.y + island.height / 2

    cannon_north_x = island.x + island.width / 2 - 15
    cannon_north_y = island.y + 10
    cannon_north_sprite = Sprite("../assets/cannon_north.png")
    cannon_north = Cannon(cannon_north_sprite, cannon_north_x, cannon_north_y)
    cannon_north_img, cannon_north_rect = cannon_north.get_img_rect()

    while(True):
        sea.draw()
        island.draw()

        if keyboard.key_pressed("A"):
            cannon_north_img, cannon_north_rect = cannon_north.move_angle_anticlockwise()

        if keyboard.key_pressed("D"):
            cannon_north_img, cannon_north_rect = cannon_north.move_angle_clockwise()

        window.get_screen().blit(cannon_north_img, cannon_north_rect)
    
        # enemy_pirate_1.draw()
        # enemy_pirate_2.draw()
        # enemy_ship_1.draw()
        # enemy_ship_2.draw()
        # player.draw()
        window.update()
        window.set_background_color([0, 0, 0,])
