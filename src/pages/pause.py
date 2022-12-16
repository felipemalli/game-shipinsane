import os
import sys

from game_parts.window_game import HEIGHT, WIDTH

sys.path.insert(0, os.path.abspath("../../"))
from PPlay.mouse import Mouse
from PPlay.sprite import Sprite
from PPlay.window import Window

window = Window(WIDTH, HEIGHT)

play_button = Sprite("../assets/images/play_button.png")
play_button.set_position(WIDTH / 2 - (play_button.width / 2), HEIGHT / 2 - (play_button.height / 2))
play_button_glow = Sprite("../assets/images/Play_button_glow.png")
play_button_glow.set_position(WIDTH / 2 - (play_button_glow.width / 2), HEIGHT / 2 - (play_button_glow.height / 2))

mouse = Mouse()

reload = True

def init():
  while(True):
      play_button.draw()
          
      if mouse.is_over_object(play_button):
          play_button_glow.draw()
          if mouse.is_button_pressed(1):
              return
      
      window.update()
