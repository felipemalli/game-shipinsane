from PPlay.sprite import Sprite


def sprite_direction(relative_path, png_name, direction):
  sprite_path = relative_path + png_name + '_' + direction + '.png'

  return Sprite(sprite_path)
