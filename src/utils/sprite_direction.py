from PPlay.sprite import Sprite


def sprite_direction(relative_path, png_name, direction, x = None, y = None):
  sprite_path = relative_path + png_name + '_' + direction + '.png'
  sprite = Sprite(sprite_path)
  if x and y:
    sprite.x = x
    sprite.y = y

  return sprite
