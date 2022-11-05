import os
import sys

from PPlay.sprite import Sprite
from PPlay.window import Window

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

    player = sprite_direction('../assets/', 'player', 'NE', island.x + island.width / 2 - 35, island.y + island.height / 2 - 25)

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

    cooldown_time = 0.5
    shot_cooldown = cooldown_time

    while(True):
        sea.draw()
        island.draw()

        player = player_movement(player, island)
        
        if keyboard.key_pressed("LEFT"):
            cannon_N_img, cannon_N_rect = cannon_N.move_anticlockwise()
            cannon_S_img, cannon_S_rect = cannon_S.move_anticlockwise()
            cannon_W_img, cannon_W_rect = cannon_W.move_anticlockwise()
            cannon_NE_img, cannon_NE_rect = cannon_NE.move_anticlockwise()

        if keyboard.key_pressed("RIGHT"):
            cannon_N_img, cannon_N_rect = cannon_N.move_clockwise()
            cannon_S_img, cannon_S_rect = cannon_S.move_clockwise()
            cannon_W_img, cannon_W_rect = cannon_W.move_clockwise()
            cannon_NE_img, cannon_NE_rect = cannon_NE.move_clockwise()

        if keyboard.key_pressed("SPACE") and shot_cooldown < 0:
            shot_cooldown = cooldown_time
            cannon_N.shot()
            cannon_S.shot()
            cannon_W.shot()
            cannon_NE.shot()        

        cannon_N.render_shots()
        window.get_screen().blit(cannon_N_img, cannon_N_rect)

        window.get_screen().blit(cannon_S_img, cannon_S_rect)
        cannon_S.render_shots()    

        cannon_W.render_shots()
        window.get_screen().blit(cannon_W_img, cannon_W_rect)

        cannon_NE.render_shots()
        window.get_screen().blit(cannon_NE_img, cannon_NE_rect)

        if shot_cooldown > 0:
            shot_cooldown -= window.delta_time()

        # enemy_pirate_1.draw()
        # enemy_pirate_2.draw()
        # enemy_ship_1.draw()
        # enemy_ship_2.draw()
        player.draw()
        window.update()
        window.set_background_color([0, 0, 0,])
