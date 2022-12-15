import os
import sys

from game_parts.window_game import HEIGHT, WIDTH

sys.path.insert(0, os.path.abspath("../../"))
from PPlay.mouse import Mouse
from PPlay.sound import Sound
from PPlay.sprite import Sprite
from PPlay.window import Window

import shipinsane

window = Window(WIDTH, HEIGHT)

mixer.music.load("../assets/Pirate 1.ogg")
mixer.music.play(-1)
sound_enter = mixer.Sound("../assets/sound_enter.ogg")

opening_image = Sprite("../assets/menu_image.jpg")


play_button = Sprite("../assets/play_button.png")
play_button.set_position(WIDTH / 12, 200)
play_button_glow = Sprite("../assets/Play_button_glow.png")
play_button_glow.set_position(WIDTH / 12, 200)
exit_button = Sprite("../assets/exit_button.png")
exit_button.set_position(WIDTH / 12, 600)
exit_button_glow = Sprite("../assets/exit_button_glow.png")
exit_button_glow.set_position(WIDTH / 12, 600)

mouse = Mouse()

reload = True

while(True):

    window.set_background_color((0,0,0))
    opening_image.draw()

    play_button.draw()
    exit_button.draw()
    
    if mouse.is_over_object(play_button):
        play_button_glow.draw()
        if mouse.is_button_pressed(1):
            sound_enter.play()
            while reload:
                reload = shipinsane.init()
            reload = True
        
    if mouse.is_over_object(exit_button):
        exit_button_glow.draw()
        if mouse.is_button_pressed(1):
            break
    
    window.update()
