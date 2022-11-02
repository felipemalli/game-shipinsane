import os
import sys

sys.path.insert(0, os.path.abspath("../../"))
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *

import shipinsane

WIDTH, HEIGHT = 1920, 1080

janela = Window(WIDTH,HEIGHT)
janela.set_title("ShipInsane Menu")

play_button = Sprite("../assets/play_button.png")
play_button.set_position(WIDTH / 12, 100)
exit_button = Sprite("../assets/exit_button.png")
exit_button.set_position(WIDTH / 12, 400)

mouse = Window.get_mouse()

while(True): 
    janela.set_background_color((0,0,0))
    
    play_button.draw()
    exit_button.draw()
    
    if mouse.is_over_object(play_button) and mouse.is_button_pressed(1):
        shipinsane.init()
        
    if mouse.is_over_object(exit_button) and mouse.is_button_pressed(1):
        break
    
    janela.update()
