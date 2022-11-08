import os
import sys

import pygame
from PPlay.sprite import Sprite

from game_parts.window_game import HEIGHT, WIDTH, island, sea, window

sys.path.insert(0, os.path.abspath("../")) # src/
from gameObjects.cannon import Cannon
from gameObjects.contact_circle import Contact_circle
from gameObjects.fleet_of_ships import Fleet_of_ships
from gameObjects.player import Player
from gameObjects.ship import Ship


def init():
    # enemy_pirate_1 = Sprite("../assets/enemy1.png")
    # enemy_pirate_2 = Sprite("../assets/enemy2.png")

    # enemy_pirate_1.x = island.x + island.width / 2 
    # enemy_pirate_1.y = island.y + 50
    # enemy_pirate_2.x = island.x + island.width / 2 - 70
    # enemy_pirate_2.y = island.y + 80

    # ----------------- Player  ----------------

    player = Player(island)

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

    # ------------ Cannon ball chest -----------

    chest = Sprite("../assets/chest.png")
    chest.x = island.x + island.x / 2 + island.x / 6
    chest.y = island.y + island.y / 2

    # -------------- Fleet_of_ships ------------

    fleet_of_ships = Fleet_of_ships(island)

    # ------------------------------------------

    delta_time = 0

    while(True):
        delta_time = window.delta_time()

        if cannon_shot_timer >= 0: cannon_shot_timer -= delta_time

        # ----------- Static Renderizations ------------

        player.movement(delta_time)
        sea.draw()
        island.draw()

        window.draw_text('Cannon ammo: ' + str(player.get_cannon_ammo()), WIDTH / 4 + 100, HEIGHT - 40, 30)
        window.draw_text('Life: ' + str(100), WIDTH / 2 + 150, HEIGHT - 40, 30)

        # -------------- Enemy generation ---------------

        fleet_of_ships.generate_enemy_ships(delta_time)

        # ------------- Player interactions -------------

        if player.get_sprite().collided(circle_N.draw()):
            cannon_shot_timer, cannon_N_img, cannon_N_rect = cannon_N.control(player, cannon_shot_timer, "RIGHT", "LEFT")
        if player.get_sprite().collided(circle_S.draw()):
            cannon_shot_timer, cannon_S_img, cannon_S_rect = cannon_S.control(player, cannon_shot_timer, "LEFT", "RIGHT")
        if player.get_sprite().collided(circle_W.draw()):
            cannon_shot_timer, cannon_W_img, cannon_W_rect = cannon_W.control(player, cannon_shot_timer, "UP", "DOWN")
        if player.get_sprite().collided(circle_NE.draw()):
            cannon_shot_timer, cannon_NE_img, cannon_NE_rect = cannon_NE.control(player, cannon_shot_timer, "DOWN", "UP")
        
        if player.get_sprite().collided(chest):
            player.reload_ammo()

        # ---------- Dinamic Renderizations -------------
       
        cannon_N.render_shots(delta_time)
        window.get_screen().blit(cannon_N_img, cannon_N_rect)
        cannon_W.render_shots(delta_time)
        window.get_screen().blit(cannon_W_img, cannon_W_rect)
        cannon_NE.render_shots(delta_time)
        window.get_screen().blit(cannon_NE_img, cannon_NE_rect)
        player.get_sprite().draw()
        window.get_screen().blit(cannon_S_img, cannon_S_rect)
        cannon_S.render_shots(delta_time)
        chest.draw()
        fleet_of_ships.render_ships(delta_time)

        # enemy_pirate_1.draw()
        # enemy_pirate_2.draw()

        #  ----------------------------------------------

        window.update()
