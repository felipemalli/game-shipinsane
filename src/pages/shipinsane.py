import math
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
    WIDTH, HEIGHT = 1920, 1080
    window = Window(WIDTH, HEIGHT)
    window.set_title("ShipInsane")
    window.set_background_color([0, 0, 0])

    island = Sprite("../assets/island2.png", 1)
    sea = Sprite("../assets/mar.png", 1)
    enemy_pirate_1 = Sprite("../assets/enemy1.png", 1)
    enemy_pirate_2 = Sprite("../assets/enemy2.png", 1)
    player = Sprite("../assets/player.png", 1)
    enemy_ship_1 = Sprite("../assets/enemy_ship1.png")
    enemy_ship_2 = Sprite("../assets/enemy_ship2.png")

    keyboard = Window.get_keyboard()

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


    # Cannons of island below ---------------------

    cannon_north = Cannon(0, Sprite("../assets/cannon_north.png"), island.x + island.width / 2 - 15, island.y + 20)
    cannon_north_img, cannon_north_rect = cannon_north.get_img_rect()

    cannon_south = Cannon(180, Sprite("../assets/cannon_south.png"), island.x + island.width / 2 - 50, island.y + island.height - 50)
    cannon_south_img, cannon_south_rect = cannon_south.get_img_rect()

    cannon_west = Cannon(90, Sprite("../assets/cannon_west.png"), island.x, island.y + island.height / 2)
    cannon_west_img, cannon_west_rect = cannon_west.get_img_rect()

    cannon_north_east = Cannon(300, Sprite("../assets/cannon_north_east.png"), island.x + island.width / 2 + 130, island.y + island.height / 2 - 70)
    cannon_north_east_img, cannon_north_east_rect = cannon_north_east.get_img_rect()

    # ---------------------------------------------

    cooldown_time = 0.5
    shot_cooldown = cooldown_time

    while(True):
        sea.draw()
        island.draw()

        if keyboard.key_pressed("A"):
            cannon_north_img, cannon_north_rect = cannon_north.move_anticlockwise()
            cannon_south_img, cannon_south_rect = cannon_south.move_anticlockwise()
            cannon_west_img, cannon_west_rect = cannon_west.move_anticlockwise()
            cannon_north_east_img, cannon_north_east_rect = cannon_north_east.move_anticlockwise()

        if keyboard.key_pressed("D"):
            cannon_north_img, cannon_north_rect = cannon_north.move_clockwise()
            cannon_south_img, cannon_south_rect = cannon_south.move_clockwise()
            cannon_west_img, cannon_west_rect = cannon_west.move_clockwise()
            cannon_north_east_img, cannon_north_east_rect = cannon_north_east.move_clockwise()

        if keyboard.key_pressed("SPACE") and shot_cooldown < 0:
            shot_cooldown = cooldown_time
            cannon_north.shot()
            cannon_south.shot()
            cannon_west.shot()
            cannon_north_east.shot()        

        cannon_north.render_shots()
        window.get_screen().blit(cannon_north_img, cannon_north_rect)

        window.get_screen().blit(cannon_south_img, cannon_south_rect)
        cannon_south.render_shots()    

        cannon_west.render_shots()
        window.get_screen().blit(cannon_west_img, cannon_west_rect)

        cannon_north_east.render_shots()
        window.get_screen().blit(cannon_north_east_img, cannon_north_east_rect)

        if shot_cooldown > 0:
            shot_cooldown -= window.delta_time()

        # enemy_pirate_1.draw()
        # enemy_pirate_2.draw()
        # enemy_ship_1.draw()
        # enemy_ship_2.draw()
        # player.draw()
        window.update()
        window.set_background_color([0, 0, 0,])
