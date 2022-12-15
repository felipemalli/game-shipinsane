
import random

import pygame
from PPlay.sprite import Sprite
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window
from src.utils.ship_moviment import get_around_string_list_by_range
from utils.animation import Animation
from utils.sprite_utils import Sprite_utils

from .cannon_ball import Cannon_ball, I_Cannon_ball
from .lifebar import Life_bar


class Ship(I_Cannon_ball):
    CLOSE_TO_SCREEN = 150
    TOO_CLOSE_TO_SCREEN = 50
    TIME_TO_FIRST_SHOT = 4

    def __init__(self, island, life, speed, damage = 20, shot_speed = 400, shot_cooldown = 10, shot_inaccuracy = 300, shot_quantity = 2):
        self.island = island
        self.life = life
        self.speed = speed
        self.damage = damage
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.show_hitbox = False
        self.is_moving = True
        self.is_shooting = True

        self.sound = pygame.mixer.Sound("../assets/explosion1.ogg")
        self.direction = random.choice(['N', 'S', 'E', 'W'])
        self.sprite = Sprite_utils.sprite_direction('../assets/', 'enemy_ship', self.direction)
        self.is_initial_position_defined = self.set_position_out_of_screen()

        self.all_directions = ["N", "NW", "W", "SW", "S", "SE", "E", "NE"]
        self.direction_dict = { direction: True for direction in self.all_directions }

        # self.average_change_direction_speed = 100
        # self.change_direction_initial_timer = 20
        # self.change_direction_timer = self.change_direction_initial_timer

        self.life_bar = Life_bar(self, self.life, self.life, self.sprite.x - self.sprite.width / 2, self.sprite.y - 13, 50, 10)

        """ Random speed for perpendicular direction """
        self.random_speed_variation = 5
        self.change_random_speed = 5
        self.random_speed_NS = 0
        self.random_speed_EW = 0

        # self.quadrant = ''
    
        self.cannon_ball_list = []
        self.shot_speed = shot_speed
        self.shot_cooldown = shot_cooldown
        self.shot_cooldown_timer = self.TIME_TO_FIRST_SHOT
        self.shot_inaccuracy = shot_inaccuracy
        self.shot_quantity = shot_quantity
        self.rect = self.sprite.image.get_rect()

        # self.shot_animation = Animation([Sprite("../assets/enemy1.png"),Sprite("../assets/enemy2.png"),Sprite("../assets/exit_button.png"),Sprite("../assets/play_button.png"),Sprite("../assets/chest.png")])

    def get_life(self):
        return self.life

    def set_show_hitbox(self, boolean):
        self.show_hitbox = boolean

    def take_damage(self, damage):
        self.sound.play()
        self.life -= damage

    def check_death(self, enemy_ships):
        if self.life <= 0:
            self.is_shooting = False
            self.is_moving = False

            if not len(self.cannon_ball_list):
                enemy_ships.remove(self)

    def draw(self):
        if self.is_initial_position_defined:
            if self.direction in ['E', 'W']:
                self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 50, self.sprite.width, self.sprite.height - 50)
                self.hitbox.collidedictall
            elif self.direction in ['NE', 'N', 'NW']:
                self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 10, self.sprite.width, self.sprite.height - 10)
            elif self.direction in ['SE', 'S', 'SW']:
                self.hitbox = pygame.Rect(self.sprite.x, self.sprite.y + 35, self.sprite.width, self.sprite.height - 35)
            if self.show_hitbox: pygame.draw.rect(window.get_screen(), (255,0,0), self.hitbox, 2)
            self.sprite.draw()
            self.life_bar.x = self.sprite.x + self.sprite.width - (self.sprite.width / 2) - (self.life_bar.size / 2)
            self.life_bar.y = self.sprite.y - 13
            self.life_bar.draw()

    # """Initial position with middle included"""
    # def set_position_out_of_screen(self):
    #     if self.direction == 'S': # coming from N
    #         self.sprite.y = - self.sprite.height
    #         self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
    #         return
    #     if self.direction == 'N': # coming from S
    #         self.sprite.y = HEIGHT
    #         self.sprite.x = random.randint(0, WIDTH - self.sprite.width)
    #         return
    #     if self.direction == 'E': # coming from W
    #         self.sprite.y = random.randint(0, HEIGHT - self.sprite.height)
    #         self.sprite.x = - self.sprite.width
    #         return
    #     if self.direction == 'W': # coming from E
    #         self.sprite.y = random.randint(0, HEIGHT - self.sprite.height)
    #         self.sprite.x = WIDTH
    #         return

    """Initial position with middle not included"""
    def set_position_out_of_screen(self):
        side = random.choice(['left or up', 'right or down'])
        space_ship_island = 50
        if self.direction == 'S': # coming from N
            self.sprite.y = - self.sprite.height
            if 'left' in side: self.sprite.x = random.randint(0, self.island.x - self.sprite.width - space_ship_island)
            elif 'right' in side: self.sprite.x = random.randint(self.island.x + self.island.width + space_ship_island, WIDTH - self.sprite.width)
            return True
        if self.direction == 'N': # coming from S
            self.sprite.y = HEIGHT
            if 'left' in side: self.sprite.x = random.randint(0, self.island.x - self.sprite.width - space_ship_island)
            elif 'right' in side: self.sprite.x = random.randint(self.island.x + self.island.width + space_ship_island, WIDTH - self.sprite.width)
            return True
        if self.direction == 'E': # coming from W
            self.sprite.x = - self.sprite.width
            if 'up' in side: self.sprite.y = random.randint(0, self.island.y - self.sprite.height - space_ship_island)
            elif 'down' in side: self.sprite.y = random.randint(self.island.y + self.island.height + space_ship_island, HEIGHT - self.sprite.height)
            return True
        if self.direction == 'W': # coming from E
            self.sprite.x = WIDTH
            if 'up' in side: self.sprite.y = random.randint(0, self.island.y - self.sprite.height - space_ship_island)
            elif 'down' in side: self.sprite.y = random.randint(self.island.y + self.island.height + space_ship_island, HEIGHT - self.sprite.height)
            return True

    def is_close_to_S(self):
        if self.hitbox.y + self.hitbox.height > HEIGHT - self.CLOSE_TO_SCREEN:
            return True

    def is_too_close_to_S(self):
        if self.hitbox.y + self.hitbox.height > HEIGHT - self.TOO_CLOSE_TO_SCREEN:
            return True

    def is_close_to_N(self):
        if self.hitbox.y < self.CLOSE_TO_SCREEN:
            return True

    def is_too_close_to_N(self):
        if self.hitbox.y < self.TOO_CLOSE_TO_SCREEN:  
            return True

    def is_close_to_E(self):
        if self.hitbox.x + self.hitbox.width > WIDTH - self.CLOSE_TO_SCREEN:
            return True

    def is_too_close_to_E(self):
        if self.hitbox.x + self.hitbox.width > WIDTH - self.TOO_CLOSE_TO_SCREEN:  
            return True

    def is_close_to_W(self):
        if self.hitbox.x < self.CLOSE_TO_SCREEN:
            return True

    def is_too_close_to_W(self):
        if self.hitbox.x < self.TOO_CLOSE_TO_SCREEN:  
            return True

    def random_speed_NS_possibility(self):
        if self.is_too_close_to_N() and self.direction in ['E', 'W']:
            return [self.random_speed_variation]
        if self.is_too_close_to_S() and self.direction in ['E', 'W']:
            return [-self.random_speed_variation]
        return [-self.random_speed_variation, self.random_speed_variation]
    
    def random_speed_EW_possibility(self):
        if self.is_too_close_to_E() and self.direction in ['N', 'S']:
            return [-self.random_speed_variation]
        if self.is_too_close_to_W() and self.direction in ['N', 'S']:
            return [self.random_speed_variation]
        return [-self.random_speed_variation, self.random_speed_variation]

    def random_side_speed(self, delta_time):
        self.change_random_speed += (2* delta_time)
        if self.change_random_speed >= (10 + random.randint(-3, 3)):
            self.random_speed_NS = random.choice(self.random_speed_NS_possibility()) * delta_time
            self.random_speed_EW = random.choice(self.random_speed_EW_possibility()) * delta_time
            self.change_random_speed = 0

    def move_to_a_direction(self, direction, delta_time):
        self.random_side_speed(delta_time)
        if 'N' in direction:
            self.sprite.y -= self.speed * delta_time
            self.sprite.x += self.random_speed_EW
        if 'S' in direction:
            self.sprite.y += self.speed * delta_time
            self.sprite.x += self.random_speed_EW
        if 'E' in direction:
            self.sprite.x += self.speed * delta_time
            self.sprite.y += self.random_speed_NS
        if 'W' in direction:
            self.sprite.x -= self.speed * delta_time
            self.sprite.y += self.random_speed_NS

    """Changes direction to the next or previous"""
    def change_direction(self):
        if len(self.direction) == 1: possible_directions = [direc for direc in self.all_directions if ((self.direction in direc) and (self.direction != direc))]
        else: possible_directions = [direc for direc in self.all_directions if ((self.direction[0] == direc) or (self.direction[1] == direc))]
        possible_valid_directions = [direc for direc in possible_directions if self.direction_dict[direc]]

        if not possible_valid_directions: # if ship is coming diagonally in a corner
            for main_direction in ["N", "S", "E", "W" ]:
                if main_direction in self.direction:
                    possible_valid_directions.append(main_direction)

        self.direction = random.choice(possible_valid_directions)
        self.sprite = Sprite_utils.sprite_direction('../assets/', 'enemy_ship', self.direction, self.sprite.x, self.sprite.y)

    def set_directions(self, directions, boolean):
        for direction in directions:
            self.direction_dict[direction] = boolean

    def prevents_going_through(self, direction):
        prev_diagonal_direction, next__diagonal_direction, next_direction, prev_direction = get_around_string_list_by_range(self.all_directions, direction, 2)

        is_close = getattr(self, "is_close_to_" + direction)
        is_too_close = getattr(self, "is_too_close_to_" + direction)

        if is_close() and self.direction in [prev_diagonal_direction, direction, next__diagonal_direction]:
            self.set_directions([direction], False) # if close, direction is blocked
            if self.direction == direction:
                self.change_direction() # to random diagonal direction
            if is_too_close(): # when in diagonal direction and too close, change to clean direction (actual is already blocked because of up line)
                self.change_direction()
        elif self.direction_dict[direction] == False: # if not close and direction blocked, free all
            self.set_directions([prev_diagonal_direction, direction, next__diagonal_direction], True)

        if is_close():
            diagonal_to_block = None
            if self.direction in [prev_direction, next_direction]: # if it is close and coming in parallel, the diagonal to this side needs to be blocked
                if self.direction in prev_diagonal_direction: diagonal_to_block = prev_diagonal_direction
                if self.direction in next__diagonal_direction: diagonal_to_block = next__diagonal_direction
                if diagonal_to_block: self.set_directions([diagonal_to_block], False)
            elif diagonal_to_block:
                self.set_directions([prev_diagonal_direction, next__diagonal_direction], True)

    def collide_with_island(self):
        if Sprite_utils.collide_mask_rect(self.hitbox, self.island):
            return True
        return False

    def move(self, delta_time):
        if not self.collide_with_island():
            self.prevents_going_through('N')
            self.prevents_going_through('E')
            self.prevents_going_through('S')
            self.prevents_going_through('W')
            
            """Ship to random direction | In progress..."""
            #
            # if self.change_direction_timer > 0:
            #     self.change_direction_timer -= self.change_direction_speed * delta_time
            # else:
            #     random_timer = self.generate_random_num_around(self.)

            self.move_to_a_direction(self.direction, delta_time)

    def shot(self, delta_time):
        if self.is_shooting:
            # self.shot_animation.render_back_and_forth(400, delta_time)
            if self.shot_cooldown_timer <= 0:
                # self.shot_animation.active_scroll()
                for _ in range(self.shot_quantity):
                    cannon_ball = Cannon_ball(self.sprite.x, self.sprite.y, self.shot_speed, self)
                    self.cannon_ball_list.append(cannon_ball)
                self.shot_cooldown_timer = self.shot_cooldown
            if self.shot_cooldown > 0:
                self.shot_cooldown_timer -= delta_time
    
    def remove_cannon_ball(self, cannon_ball):
        self.cannon_ball_list.remove(cannon_ball)

    def render_shots(self, delta_time, targets):
        for cannon_ball in self.cannon_ball_list:
            cannon_ball.draw()
            random_close_x = random.randrange((WIDTH / 2) - self.shot_inaccuracy, (WIDTH / 2) + self.shot_inaccuracy)
            random_close_y = random.randrange((HEIGHT / 2) - self.shot_inaccuracy, (HEIGHT / 2) + self.shot_inaccuracy)
            cannon_ball.move_with_position_direction(self.hitbox.x, self.hitbox.y, random_close_x, random_close_y, delta_time)
        
        for cannon_ball in self.cannon_ball_list:
            for target in targets:
                if cannon_ball.sprite.rect.colliderect(target.hitbox):
                    self.remove_cannon_ball(cannon_ball)
                    target.take_damage(self.damage)

    # def update_quadrant(self):
    #     if self.hitbox.y + (self.hitbox.height / 2) < HEIGHT / 2:
    #         if self.hitbox.x + (self.hitbox.width / 2) > WIDTH / 2:
    #             self.quadrant = 'NE'
    #         else:
    #             self.quadrant = 'NW'
    #     else:
    #         if self.hitbox.x + (self.hitbox.width / 2) > WIDTH / 2:
    #             self.quadrant = 'SE'
    #         else:
    #             self.quadrant = 'SW'
