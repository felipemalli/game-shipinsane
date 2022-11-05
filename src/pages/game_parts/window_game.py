import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

from PPlay.sprite import Sprite
from PPlay.window import Window

WIDTH, HEIGHT = 1920, 1080
window = Window(WIDTH, HEIGHT)

sea = Sprite("../assets/mar.png", 1)
island = Sprite("../assets/island2.png", 1)

island.x = WIDTH / 2 - island.width / 2
island.y = HEIGHT / 2 - island.height / 2
