from PPlay.keyboard import Keyboard

keyboard = Keyboard()

def cannon_controls(cannon, cannon_img, cannon_rect, shot_timer, clockwise_key, anticlockwise_key):
  if keyboard.key_pressed(clockwise_key):
    cannon_img, cannon_rect = cannon.move_clockwise()

  if keyboard.key_pressed(anticlockwise_key):
    cannon_img, cannon_rect = cannon.move_anticlockwise()

  if keyboard.key_pressed("SPACE") and shot_timer < 0:
    cannon.shot()
    shot_cooldown = 1
    return shot_cooldown, cannon_img, cannon_rect
  
  return shot_timer, cannon_img, cannon_rect
