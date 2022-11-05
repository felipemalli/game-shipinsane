import os
import sys

from pages.game_parts.window_game import HEIGHT, WIDTH

sys.path.insert(0, os.path.abspath("../../"))
from PPlay.mouse import Mouse
from PPlay.sprite import Sprite
from PPlay.window import Window

import shipinsane

window = Window(WIDTH, HEIGHT)

play_button = Sprite("../assets/play_button.png")
play_button.set_position(WIDTH / 12, 100)
exit_button = Sprite("../assets/exit_button.png")
exit_button.set_position(WIDTH / 12, 400)

mouse = Mouse()

while(True): 
    play_button.draw()
    exit_button.draw()
    
    if mouse.is_over_object(play_button) and mouse.is_button_pressed(1):
        shipinsane.init()
        
    if mouse.is_over_object(exit_button) and mouse.is_button_pressed(1):
        break
    
    window.update()
