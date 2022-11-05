import os
import sys

import pygame
from PPlay.sprite import Sprite
from PPlay.window import Window

from game_parts.cannon_controls import cannon_controls
from game_parts.player_movement import player_movement

sys.path.insert(0, os.path.abspath("../")) # src/
from gameObjects.cannon import Cannon
from gameObjects.cannon_ball import Cannon_ball
from utils.sprite_direction import sprite_direction


def init():
    WIDTH, HEIGHT = 1920, 1080
    window = Window(WIDTH, HEIGHT)
    window.set_title("ShipInsane")
    window.set_background_color([0, 0, 0])

    island = Sprite("../assets/island2.png", 1)
    sea = Sprite("../assets/mar.png", 1)
    enemy_pirate_1 = Sprite("../assets/enemy1.png", 1)
    enemy_pirate_2 = Sprite("../assets/enemy2.png", 1)
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
    # player = Sprite("../assets/player_NE.png", 1)

    # cannon1.x = island.x + island.width / 2 - 15
    # cannon1.y = island.y + 10

    # cannon2.x = island.x + island.width / 2 + 130
    # cannon2.y = island.y + island.height / 2 - 70

    # cannon3.x = island.x + island.width / 2 - 50
    # cannon3.y = island.y + island.height - 50  

    # cannon4.x = island.x
    # cannon4.y = island.y + island.height / 2

    # ----------------- Player  ----------------

    player = sprite_direction('../assets/', 'player', 'S', island.x + island.width / 2 - 35, island.y + island.height / 2 - 25)

    # ----------- Cannons of island  -----------

    cannon_N = Cannon(0, Sprite("../assets/cannon_N.png"), island.x + island.width / 2 - 15, island.y + 20)
    cannon_N_img, cannon_N_rect = cannon_N.get_img_rect()

    cannon_S = Cannon(180, Sprite("../assets/cannon_S.png"), island.x + island.width / 2 - 50, island.y + island.height - 50)
    cannon_S_img, cannon_S_rect = cannon_S.get_img_rect()

    cannon_W = Cannon(90, Sprite("../assets/cannon_W.png"), island.x + 45, island.y + island.height / 2)
    cannon_W_img, cannon_W_rect = cannon_W.get_img_rect()

    cannon_NE = Cannon(300, Sprite("../assets/cannon_NE.png"), island.x + 130 + island.width / 2, island.y + island.height / 2 - 70)
    cannon_NE_img, cannon_NE_rect = cannon_NE.get_img_rect()

    # ------------------------------------------

    cannon_shot_timer = 0
    
    circle_color, circle_size, circle_thickness = (160, 160, 160), 12, 1
    circle_N_x = cannon_N_rect.x + (cannon_N.get_sprite().width / 2)
    circle_N_y = cannon_N_rect.y + cannon_N.get_sprite().height
    circle_S_x = cannon_S_rect.x + (cannon_S.get_sprite().width / 2)
    circle_S_y = cannon_S_rect.y - cannon_S.get_sprite().height / 12
    circle_W_x = cannon_W_rect.x + (cannon_W.get_sprite().width) + 4
    circle_W_y = cannon_W_rect.y + cannon_W.get_sprite().height / 2 + 5
    circle_NE_x = cannon_NE_rect.x + (cannon_NE.get_sprite().width / 4) - 2
    circle_NE_y = cannon_NE_rect.y + cannon_NE.get_sprite().height - 4

    while(True):
        if cannon_shot_timer >= 0: cannon_shot_timer -= window.delta_time()

        # ----------- Initial Renderizations ------------

        sea.draw()
        island.draw()
        circle_N = pygame.draw.circle(window.get_screen(), circle_color, [circle_N_x, circle_N_y], circle_size, circle_thickness)
        circle_S = pygame.draw.circle(window.get_screen(), circle_color, [circle_S_x, circle_S_y], circle_size, circle_thickness)
        circle_W = pygame.draw.circle(window.get_screen(), circle_color, [circle_W_x, circle_W_y], circle_size, circle_thickness)
        circle_NE = pygame.draw.circle(window.get_screen(), circle_color, [circle_NE_x, circle_NE_y], circle_size, circle_thickness)

        # ------------- Player interactions -------------

        player = player_movement(player, island)

        if player.collided(circle_N):
            cannon_shot_timer, cannon_N_img, cannon_N_rect = cannon_controls(cannon_N, cannon_N_img, cannon_N_rect, cannon_shot_timer, "RIGHT", "LEFT")
        if player.collided(circle_S):
            cannon_shot_timer, cannon_S_img, cannon_S_rect = cannon_controls(cannon_S, cannon_S_img, cannon_S_rect, cannon_shot_timer, "LEFT", "RIGHT")
        if player.collided(circle_W):
            cannon_shot_timer, cannon_W_img, cannon_W_rect = cannon_controls(cannon_W, cannon_W_img, cannon_W_rect, cannon_shot_timer, "UP", "DOWN")
        if player.collided(circle_NE):
            cannon_shot_timer, cannon_NE_img, cannon_NE_rect = cannon_controls(cannon_NE, cannon_NE_img, cannon_NE_rect, cannon_shot_timer, "DOWN", "UP")
        
        # --------------- Renderizations ----------------
       
        cannon_N.render_shots()
        window.get_screen().blit(cannon_N_img, cannon_N_rect)
        cannon_W.render_shots()
        window.get_screen().blit(cannon_W_img, cannon_W_rect)
        cannon_NE.render_shots()
        window.get_screen().blit(cannon_NE_img, cannon_NE_rect)
        player.draw()
        window.get_screen().blit(cannon_S_img, cannon_S_rect)
        cannon_S.render_shots()

        enemy_pirate_1.draw()
        enemy_pirate_2.draw()
        enemy_ship_1.draw()
        enemy_ship_2.draw()

        #  ----------------------------------------------

        window.update()
