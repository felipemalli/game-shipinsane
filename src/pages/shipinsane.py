import os
import sys

from PPlay.sprite import Sprite

from game_parts.endless_mode import Endless_mode
from game_parts.window_game import HEIGHT, WIDTH, island, island_hitbox, window

sys.path.insert(0, os.path.abspath("../")) # src/
from gameObjects.cannon import Cannon
from gameObjects.contact_circle import Contact_circle
from gameObjects.fleet_of_ships import Fleet_of_ships
from gameObjects.hitbox_switcher import Hitbox_switcher
from gameObjects.player import Player
from gameObjects.smoke_effect import Smoke, SmokeParticle
from PPlay.keyboard import Keyboard
from pygame import mixer
from utils.animation import Animation
from utils.text_utils import Text_utils

keyboard = Keyboard()


def init():

    sea_sprites = [Sprite("../assets/images/sea0.png"),Sprite("../assets/images/sea1.png"),Sprite("../assets/images/sea2.png"),Sprite("../assets/images/sea3.png"),Sprite("../assets/images/sea4.png")]
    sea_animation = Animation(sea_sprites, 0)
    sound_lose = mixer.Sound("../assets/sounds/sf-you-lose.mp3")
    play_sound = True
    smoke = Smoke()

    # sea_sprite = Sprite("../assets/images/sea0.png")
    # image = sea_sprite.image.convert_alpha()
    # image.set_alpha(100)
    # window.get_screen().blit(sea_sprite.image, (0,0))

    # -------------------- Player  -------------------

    player = Player(island_hitbox)

    # ----------- Cannons of island  -----------

    cannon_N = Cannon(0, Sprite("../assets/images/cannon_N.png"), island.x + island.width / 2 - 15, island.y + 20)
    cannon_S = Cannon(180, Sprite("../assets/images/cannon_S.png"), island.x + island.width / 2 - 50, island.y + island.height - 50)
    cannon_W = Cannon(90, Sprite("../assets/images/cannon_W.png"), island.x + 45, island.y + island.height / 2)
    cannon_NE = Cannon(300, Sprite("../assets/images/cannon_NE.png"), island.x + 130 + island.width / 2, island.y + island.height / 2 - 70)

    # --------- Contact area of cannons ---------

    CIRCLE_COLOR, CIRCLE_SIZE, CIRCLE_THICKNESS = (160, 160, 160), 12, 1
    circle_N_x, circle_N_y = cannon_N.get_rect().x + (cannon_N.get_sprite().width / 2), cannon_N.get_rect().y + cannon_N.get_sprite().height
    circle_N = Contact_circle(circle_N_x, circle_N_y, CIRCLE_SIZE, CIRCLE_THICKNESS, CIRCLE_COLOR)
    circle_S_x, circle_S_y = cannon_S.get_rect().x + (cannon_S.get_sprite().width / 2), cannon_S.get_rect().y - cannon_S.get_sprite().height / 12
    circle_S = Contact_circle(circle_S_x, circle_S_y, CIRCLE_SIZE, CIRCLE_THICKNESS, CIRCLE_COLOR)
    circle_W_x, circle_W_y = cannon_W.get_rect().x + (cannon_W.get_sprite().width) + 4, cannon_W.get_rect().y + cannon_W.get_sprite().height / 2 + 5
    circle_W = Contact_circle(circle_W_x, circle_W_y, CIRCLE_SIZE, CIRCLE_THICKNESS, CIRCLE_COLOR)
    circle_NE_x, circle_NE_y = cannon_NE.get_rect().x + (cannon_NE.get_sprite().width / 4) - 2, cannon_NE.get_rect().y + cannon_NE.get_sprite().height - 4 
    circle_NE = Contact_circle(circle_NE_x, circle_NE_y, CIRCLE_SIZE, CIRCLE_THICKNESS, CIRCLE_COLOR)

    # ------------ Cannon ball chest -----------

    chest = Sprite("../assets/images/chest.png")
    chest.x = island.x + island.x / 2 + island.x / 6
    chest.y = island.y + island.y / 2

    # -------------- Game modes  ------------

    endless_mode = Endless_mode(island)
    endless_mode.add_player(player)

    # ---------------- Hitbox Switcher ---------------

    hitbox_switcher = Hitbox_switcher([player, endless_mode.fleet_of_ships])

    # ------------------------------------------

    delta_time = 0
    
    while(True):
        if player.life > 0:
            player.movement(delta_time)

        if window.delta_time() < 0.1:
            delta_time = window.delta_time()

        sea_animation.infinite_scroll(200, delta_time)
        
        # ----------- Static renderizations ------------

        island_hitbox.draw()
        island.draw()
        hitbox_switcher.draw(delta_time)
        window.draw_text('Cannon ammo: ' + str(player.get_cannon_ammo()), WIDTH / 2 - 110, HEIGHT - 100, 30)

        # ------------- Player interactions -------------

        if player.get_hitbox().colliderect(circle_N.draw()): cannon_N.control(player, "RIGHT", "LEFT")
        if player.get_hitbox().colliderect(circle_S.draw()): cannon_S.control(player, "LEFT", "RIGHT")
        if player.get_hitbox().colliderect(circle_W.draw()): cannon_W.control(player, "UP", "DOWN")
        if player.get_hitbox().colliderect(circle_NE.draw()): cannon_NE.control(player, "DOWN", "UP")
        if player.get_hitbox().colliderect(chest): player.reload_ammo()

        # ------- Dynamic and order renderizations -------
    
        cannon_N.render_shots(delta_time)
        cannon_N.render()
        cannon_W.render_shots(delta_time)
        cannon_W.render()
        cannon_NE.render_shots(delta_time)
        cannon_NE.render()
        endless_mode.render(delta_time)
        player.draw()
        cannon_S.render()
        cannon_S.render_shots(delta_time)
        chest.draw()
        endless_mode.screen_configurations(delta_time)


        smoke.update()
        smoke.draw()

    #  ---------------- In progress ----------------

        if player.life <= 0:
            if play_sound:
                mixer.music.stop()
                sound_lose.play()
            play_sound = False
            Text_utils.draw_text("Você perdeu!", 100, WIDTH/2, HEIGHT/2)
            Text_utils.draw_text("Digite R para recomeçar.", 35, WIDTH/2, HEIGHT/2 + 120)

            if keyboard.key_pressed("R"):
                Fleet_of_ships.enemy_ships = []
                mixer.music.play(-1)
                return True

        if keyboard.key_pressed("ESC"):
            if player.life <= 0:
                mixer.music.play(-1)
            Fleet_of_ships.enemy_ships = []
            return False

        #  ----------------------------------------------

        window.update()
