from PPlay.sprite import Sprite


def sprite_direction(relative_path, png_name, direction, x , y):
  sprite_path = relative_path + png_name + '_' + direction + '.png'
  sprite = Sprite(sprite_path)
  sprite.x = x
  sprite.y = y

  return sprite
