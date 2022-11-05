import os
import sys

import pygame
from PPlay.sprite import Sprite

from game_parts.cannon_controls import cannon_controls
from game_parts.player_movement import player_movement
from pages.game_parts.window_game import island, sea, window

sys.path.insert(0, os.path.abspath("../")) # src/
from gameObjects.cannon import Cannon
from gameObjects.contact_circle import Contact_circle
from utils.sprite_direction import sprite_direction


def init():
    enemy_pirate_1 = Sprite("../assets/enemy1.png", 1)
    enemy_pirate_2 = Sprite("../assets/enemy2.png", 1)
    enemy_ship_1 = Sprite("../assets/enemy_ship1.png")
    enemy_ship_2 = Sprite("../assets/enemy_ship2.png")

    # enemy_ship_1.x = 5 * WIDTH / 6
    # enemy_ship_1.y = island.x / 2 - 40
    # enemy_ship_2.x = island.x / 2 - 40
    # enemy_ship_2.y = 5 * HEIGHT / 7 
    # enemy_pirate_1.x = island.x + island.width / 2 
    # enemy_pirate_1.y = island.y + 50
    # enemy_pirate_2.x = island.x + island.width / 2 - 70
    # enemy_pirate_2.y = island.y + 80

    # ----------------- Player  ----------------

    player = sprite_direction('../assets/', 'player', 'S', island.x + island.width / 2 - 35, island.y + island.height / 2 - 25)

    # ----------- Cannons of island  -----------

    cannon_shot_timer = 0

    cannon_N = Cannon(0, Sprite("../assets/cannon_N.png"), island.x + island.width / 2 - 15, island.y + 20)
    cannon_N_img, cannon_N_rect = cannon_N.get_img_rect()

    cannon_S = Cannon(180, Sprite("../assets/cannon_S.png"), island.x + island.width / 2 - 50, island.y + island.height - 50)
    cannon_S_img, cannon_S_rect = cannon_S.get_img_rect()

    cannon_W = Cannon(90, Sprite("../assets/cannon_W.png"), island.x + 45, island.y + island.height / 2)
    cannon_W_img, cannon_W_rect = cannon_W.get_img_rect()

    cannon_NE = Cannon(300, Sprite("../assets/cannon_NE.png"), island.x + 130 + island.width / 2, island.y + island.height / 2 - 70)
    cannon_NE_img, cannon_NE_rect = cannon_NE.get_img_rect()

    # --------- Contact area of cannons ---------

    circle_color, circle_size, circle_thickness = (160, 160, 160), 12, 1

    circle_N_x, circle_N_y = cannon_N_rect.x + (cannon_N.get_sprite().width / 2), cannon_N_rect.y + cannon_N.get_sprite().height
    circle_N = Contact_circle(circle_N_x, circle_N_y, circle_size, circle_thickness, circle_color)

    circle_S_x, circle_S_y = cannon_S_rect.x + (cannon_S.get_sprite().width / 2), cannon_S_rect.y - cannon_S.get_sprite().height / 12
    circle_S = Contact_circle(circle_S_x, circle_S_y, circle_size, circle_thickness, circle_color)

    circle_W_x, circle_W_y = cannon_W_rect.x + (cannon_W.get_sprite().width) + 4, cannon_W_rect.y + cannon_W.get_sprite().height / 2 + 5
    circle_W = Contact_circle(circle_W_x, circle_W_y, circle_size, circle_thickness, circle_color)

    circle_NE_x, circle_NE_y = cannon_NE_rect.x + (cannon_NE.get_sprite().width / 4) - 2, cannon_NE_rect.y + cannon_NE.get_sprite().height - 4 
    circle_NE = Contact_circle(circle_NE_x, circle_NE_y, circle_size, circle_thickness, circle_color)

    # ------------------------------------------

    while(True):
        if cannon_shot_timer >= 0: cannon_shot_timer -= window.delta_time()

        # ----------- Static Renderizations ------------

        sea.draw()
        island.draw()

        # ------------- Player interactions -------------

        player = player_movement(player, island)

        if player.collided(circle_N.draw()):
            cannon_shot_timer, cannon_N_img, cannon_N_rect = cannon_controls(cannon_N, cannon_N_img, cannon_N_rect, cannon_shot_timer, "RIGHT", "LEFT")
        if player.collided(circle_S.draw()):
            cannon_shot_timer, cannon_S_img, cannon_S_rect = cannon_controls(cannon_S, cannon_S_img, cannon_S_rect, cannon_shot_timer, "LEFT", "RIGHT")
        if player.collided(circle_W.draw()):
            cannon_shot_timer, cannon_W_img, cannon_W_rect = cannon_controls(cannon_W, cannon_W_img, cannon_W_rect, cannon_shot_timer, "UP", "DOWN")
        if player.collided(circle_NE.draw()):
            cannon_shot_timer, cannon_NE_img, cannon_NE_rect = cannon_controls(cannon_NE, cannon_NE_img, cannon_NE_rect, cannon_shot_timer, "DOWN", "UP")
        
        # ---------- Dinamic Renderizations -------------
       
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
