import pygame
from PPlay.keyboard import Keyboard

keyboard = Keyboard()

from PPlay.sprite import Sprite
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window
from utils.sprite_utils import Sprite_utils
from utils.text_utils import Text_utils

from .lifebar import I_Life_bar, Life_bar


class Player(I_Life_bar):
    def __init__(self, island):
        self.island = island
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.show_hitbox = False
        self.sprite = Sprite_utils.sprite_direction('../assets/images/', 'player', 'S', island.x + island.width / 2 - 35, island.y + island.height / 2 - 25)
        self.cannon_max_ammo = 10
        self.cannon_ammo = self.cannon_max_ammo
        self.speed = 100
        self.max_life = 100
        self.life = 100
        self.key_W = 'free'
        self.key_A = 'free'
        self.key_S = 'free'
        self.key_D = 'free'
        self.life_bar = Life_bar(self, self.max_life, self.life, WIDTH/4 , HEIGHT - 50, 1000, 30, Sprite("../assets/images/heart_50x50.png"))
        self.sound_reload = pygame.mixer.Sound("../assets/sounds/Reload.wav")
        self.sound_hit = self.generate_sound_hit()

    def get_island(self):
        return self.island
    def get_sprite(self):
        return self.sprite
    def set_sprite(self, sprite):
        self.sprite = sprite
    def get_cannon_ammo(self):
        return self.cannon_ammo
    def set_cannon_ammo(self, cannon_ammo):
        self.cannon_ammo = cannon_ammo
    def get_speed(self):
        return self.speed
    def set_sprite_x(self, x):
        self.sprite.x = x
    def set_sprite_y(self, y):
        self.sprite.y = y
    def get_hitbox(self):
        return self.hitbox
    def get_life(self):
        return self.life

    def generate_sound_hit(self):
        sound = pygame.mixer.Sound("../assets/sounds/hit_player.wav")
        pygame.mixer.Sound.set_volume(sound, 0.5)
        return sound

    def take_damage(self, damage):
        self.sound_hit.play()
        self.life -= damage

    def toggle_hitbox(self):
        self.show_hitbox = not self.show_hitbox

    def draw(self):
        self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 20, self.sprite.width, self.sprite.height - 20)
        if self.show_hitbox: pygame.draw.rect(window.get_screen(), (255,0,0), self.hitbox, 2)
        self.sprite.draw()
        self.life_bar.draw()

    def reduce_cannon_ammo(self):
        if self.get_cannon_ammo() > 0:
            self.cannon_ammo -= 1

    def player_direction(self):
        if keyboard.key_pressed("W") and keyboard.key_pressed("D"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'NE', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("S") and keyboard.key_pressed("D"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'SE', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("S") and keyboard.key_pressed("A"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'SW', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("W") and keyboard.key_pressed("A"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'NW', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("W"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'N', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("A"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'W', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("S"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'S', self.get_sprite().x, self.get_sprite().y))
        elif keyboard.key_pressed("D"):
            self.set_sprite(Sprite_utils.sprite_direction('../assets/images/', 'player', 'E', self.get_sprite().x, self.get_sprite().y))

    def is_inside_island(self):
        if pygame.sprite.collide_mask(self.get_sprite(), self.get_island()):
            return True

    def block_if_outside_island(self, sprite, key):
        key_attribute = 'key_' + key
        if not pygame.sprite.collide_mask(sprite.get_sprite(), self.get_island()):
            setattr(self, key_attribute, 'blocked')
        else:
            setattr(self, key_attribute, 'free')

    def test_next_position(self, mirror_sprite, key_to_block, actual_x, plus_x, actual_y, plus_y):
        mirror_sprite.get_sprite().x = actual_x + plus_x
        mirror_sprite.get_sprite().y = actual_y + plus_y
        mirror_sprite.get_sprite().draw()
        self.block_if_outside_island(mirror_sprite, key_to_block)

    def check_if_outside_island(self):
        actual_x = self.get_sprite().x
        actual_y = self.get_sprite().y
        mirror_sprite = Player(self.get_island())

        self.test_next_position(mirror_sprite, 'D', actual_x, 25, actual_y, 0)
        if self.key_D == 'free':
            self.test_next_position(mirror_sprite, 'D', actual_x, 25, actual_y, 36) 
        self.test_next_position(mirror_sprite, 'A', actual_x, -25, actual_y, 0)
        if self.key_A == 'free':
            self.test_next_position(mirror_sprite, 'A', actual_x, -25, actual_y, 36)
        self.test_next_position(mirror_sprite, 'W', actual_x, 0, actual_y, -5)
        self.test_next_position(mirror_sprite, 'S', actual_x, 0, actual_y, 38)
        
    def movement(self, delta_time):
        if keyboard.key_pressed("W") and self.key_W == 'free':
            self.get_sprite().y -= self.get_speed() * delta_time
            self.check_if_outside_island()
        if keyboard.key_pressed("A") and self.key_A == 'free':
            self.get_sprite().x -= self.get_speed() * delta_time
            self.check_if_outside_island()
        if keyboard.key_pressed("S") and self.key_S == 'free':
            self.get_sprite().y += self.get_speed() * delta_time
            self.check_if_outside_island()
        if keyboard.key_pressed("D") and self.key_D == 'free':
            self.get_sprite().x += self.get_speed() * delta_time
            self.check_if_outside_island()
        
        self.player_direction()

    def reload_ammo(self):
        Text_utils.draw_text("Press R to reload", 30, WIDTH/2, HEIGHT-200)

        if keyboard.key_pressed("R"):
            if self.cannon_ammo < self.cannon_max_ammo:
                self.sound_reload.play()

            self.set_cannon_ammo(self.cannon_max_ammo)
