import os
import sys

from game_parts.window_game import HEIGHT, WIDTH

sys.path.insert(0, os.path.abspath("../../"))
from PPlay.mouse import Mouse
from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.sound import Sound

import shipinsane

window = Window(WIDTH, HEIGHT)

music = Sound("../assets/Pirate 1.ogg")
opening_image = Sprite("../assets/menu_image.jpg")

play_button = Sprite("../assets/play_button.png")
play_button.set_position(WIDTH / 12, 100)
exit_button = Sprite("../assets/exit_button.png")
exit_button.set_position(WIDTH / 12, 400)

mouse = Mouse()

reload = True

while(True): 
    music.play()

    window.set_background_color((0,0,0))
    opening_image.draw()

    play_button.draw()
    exit_button.draw()
    
    if mouse.is_over_object(play_button) and mouse.is_button_pressed(1):
        while reload:
            reload = shipinsane.init()
        reload = True
        
    if mouse.is_over_object(exit_button) and mouse.is_button_pressed(1):
        break
    
    window.update()
