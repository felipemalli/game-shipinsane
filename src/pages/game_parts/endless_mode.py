import math
import os
import sys

import pygame

from .window_game import WIDTH, window

sys.path.insert(0, os.path.abspath("../"))
from gameObjects.fleet_of_ships import Fleet_of_ships
from utils.text_utils import Text_utils


class Endless_mode:
    TOGGLE_CONFIG_COOLDOWN = 5

    def __init__(self, island):
        self.initial_max_count = 2
        self.initial_average_spawn_speed = 200
        self.life = 20
        self.speed = 40
        self.damage = 20
        self.shot_speed = 400
        self.shot_cooldown = 5
        self.shot_inaccuracy = 300
        self.shot_quantity = 1
        self.fleet_of_ships = Fleet_of_ships(island, self.initial_max_count, self.initial_average_spawn_speed)

        self.balancing_timer = 2

        self.seconds = 0
        self.minutes = 0
        self.timer_in_seconds = 0
        self.timer_in_minutes = 0

        self.toggle_config_cooldown = self.TOGGLE_CONFIG_COOLDOWN
        self.show_config = False
        self.player = None

    def show_configs(self):
        window.draw_text("Player:", 20, 20, 15, (46,46,46), "Arial", True)
        window.draw_text("- max life: " + str(self.player.life), 40, 40, 15, (46,46,46), "Arial", True)
        window.draw_text("- speed: " + str(self.player.speed), 40, 60, 15, (46,46,46), "Arial", True)
        window.draw_text("- max ammo: " + str(self.player.cannon_max_ammo), 40, 80, 15, (46,46,46), "Arial", True)
        window.draw_text("Enemy ship:", 20, 100, 15, (46,46,46), "Arial", True)
        window.draw_text("- life: " + str(self.life), 40, 120, 15, (46,46,46), "Arial", True)
        window.draw_text("- speed: " + str(self.speed), 40, 140, 15, (46,46,46), "Arial", True)
        window.draw_text("- damage: " + str(self.damage), 40, 160, 15, (46,46,46), "Arial", True)
        window.draw_text("- shot cooldown: " + str(self.speed), 40, 180, 15, (46,46,46), "Arial", True)
        window.draw_text("- shot inaccuracy: " + str(self.damage), 40, 200, 15, (46,46,46), "Arial", True)
        window.draw_text("- cannon ball per shot: " + str(self.damage), 40, 220, 15, (46,46,46), "Arial", True)
        window.draw_text("- max count on screen: " + str(self.fleet_of_ships.max_count), 40, 240, 15, (46,46,46), "Arial", True)
        window.draw_text("- spawn speed: " + str(self.fleet_of_ships.average_spawn_speed), 40, 260, 15, (46,46,46), "Arial", True)

    def screen_configurations(self, delta_time):
        if self.toggle_config_cooldown > 0:
            self.toggle_config_cooldown -= 10 * delta_time
        if self.toggle_config_cooldown <= 0 and pygame.key.get_pressed()[pygame.K_F2]:
            self.show_config = not self.show_config
            self.toggle_config_cooldown = self.TOGGLE_CONFIG_COOLDOWN
        if self.show_config: self.show_configs()

    def add_player(self, target):
        self.player = target
        self.fleet_of_ships.add_target(target)

    def increase_timer(self, delta_time):
        self.timer_in_seconds += delta_time
        self.timer_in_minutes = self.timer_in_seconds / 60

    def render_timer(self):
        self.minutes = math.floor(self.timer_in_minutes)
        self.seconds = math.floor(self.timer_in_seconds)
        if self.seconds > 60: self.seconds -= 60
        Text_utils.draw_text(str(self.minutes).zfill(2) + " : " + str(self.seconds).zfill(2), 30, WIDTH / 2, 20)

    def render(self, delta_time):
        self.render_timer()
        self.delta_time = delta_time
        self.fleet_of_ships.generate_enemy_ships(delta_time, 
            [
                self.life, self.speed, self.damage, self.shot_speed, 
                self.shot_cooldown, self.shot_inaccuracy, self.shot_quantity
            ]
        )
        self.fleet_of_ships.render_ships(delta_time)
        self.increase_timer(delta_time)
        self.balancing_management(delta_time)

    def timer_reaches(self, minute, seconds):
        time = seconds + (minute * 60)
        if self.timer_in_seconds > time and self.timer_in_seconds < (time + 1):
            return True
        return False

    def balancing_management(self, delta_time):
        if self.balancing_timer > 0:
            self.balancing_timer -= delta_time
        if self.balancing_timer <= 0:
            self.balancing_timer = 2
            self.timer_balancing()
    
    def timer_balancing(self):
        if self.timer_reaches(0, 20):
            self.fleet_of_ships.max_count += 1
            self.fleet_of_ships.average_spawn_speed += 100
        if self.timer_reaches(0, 40):
            self.shot_speed += 20
        # if self.timer_reaches()
