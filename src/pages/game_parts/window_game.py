import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

from PPlay.sprite import Sprite
from PPlay.window import Window

WIDTH, HEIGHT = 1920, 1080
window = Window(WIDTH, HEIGHT)

island = Sprite("../assets/images/island_view.png", 1)
island.x = WIDTH / 2 - island.width / 2
island.y = HEIGHT / 2 - island.height / 2

island_hitbox = Sprite("../assets/images/island_hitbox.png", 1)
island_hitbox.x = WIDTH / 2 - island_hitbox.width / 2
island_hitbox.y = HEIGHT / 2 - island_hitbox.height / 2

