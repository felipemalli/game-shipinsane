import math
import os
import sys

import pygame

from .window_game import WIDTH, window

sys.path.insert(0, os.path.abspath("../"))
from gameObjects.fleet_of_ships import Fleet_of_ships
from gameObjects.pontuation import Pontuation
from utils.text_utils import Text_utils


class Endless_mode:
    TOGGLE_CONFIG_COOLDOWN = 5

    def __init__(self, island):
        self.initial_max_count = 2
        self.initial_average_spawn_speed = 200
        self.life = 20
        self.speed = 40
        self.damage = 10
        self.shot_speed = 300
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
        window.draw_text("- max life: " + str(self.player.max_life), 40, 40, 15, (46,46,46), "Arial", True)
        window.draw_text("- speed: " + str(self.player.speed), 40, 60, 15, (46,46,46), "Arial", True)
        window.draw_text("- max ammo: " + str(self.player.cannon_max_ammo), 40, 80, 15, (46,46,46), "Arial", True)
        window.draw_text("Enemy ship:", 20, 100, 15, (46,46,46), "Arial", True)
        window.draw_text("- life: " + str(self.life), 40, 120, 15, (46,46,46), "Arial", True)
        window.draw_text("- speed: " + str(self.speed), 40, 140, 15, (46,46,46), "Arial", True)
        window.draw_text("- damage: " + str(self.damage), 40, 160, 15, (46,46,46), "Arial", True)
        window.draw_text("- max count on screen: " + str(self.fleet_of_ships.max_count), 40, 180, 15, (46,46,46), "Arial", True)
        window.draw_text("- spawn speed: " + str(self.fleet_of_ships.average_spawn_speed), 40, 200, 15, (46,46,46), "Arial", True)
        window.draw_text("- shot speed: " + str(self.shot_speed), 40, 220, 15, (46,46,46), "Arial", True)
        window.draw_text("- shot cooldown: " + str(self.shot_cooldown), 40, 240, 15, (46,46,46), "Arial", True)
        window.draw_text("- shot inaccuracy: " + str(self.shot_inaccuracy), 40, 260, 15, (46,46,46), "Arial", True)
        window.draw_text("- cannon ball per shot: " + str(self.shot_quantity), 40, 280, 15, (46,46,46), "Arial", True)

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

    def render_timer(self, delta_time):
        if self.player.life > 0:
            self.minutes = math.floor(self.timer_in_minutes)
            self.seconds += delta_time
        if self.seconds >= 60: self.seconds -= 60
        Text_utils.draw_text(str(self.minutes).zfill(2) + " : " + str(math.floor(self.seconds)).zfill(2), 30, WIDTH / 2, 60)
        Pontuation.update_time_by_seconds(self.timer_in_seconds)

    def render(self, delta_time):
        self.render_timer(delta_time)
        self.delta_time = delta_time
        self.fleet_of_ships.generate_enemy_ships(delta_time, 
            [
                self.life, self.speed, self.damage, self.shot_speed, 
                self.shot_cooldown, self.shot_inaccuracy, self.shot_quantity
            ]
        )
        self.fleet_of_ships.render_ships(delta_time, self.player)
        if self.player.life > 0: 
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

    def boss_parameters(self):
        return [
            self.life * 2,
            self.speed,
            self.damage,
            self.shot_speed,
            self.shot_cooldown / 1.25,
            self.shot_inaccuracy,
            self.shot_quantity * 2,
        ]  
    
    def timer_balancing(self):
        if self.minutes != 0 and (self.minutes % 2 == 0 or self.minutes == 1) and self.seconds < 1:
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(0, 10):
            self.fleet_of_ships.average_spawn_speed += 50

        if self.timer_reaches(0, 20):
            self.fleet_of_ships.max_count += 1
            self.fleet_of_ships.average_spawn_speed += 50
            self.shot_cooldown -= 0.5
            self.shot_speed += 50

        if self.timer_reaches(0, 30):
            self.shot_cooldown -= 0.5
            self.damage += 5

        if self.timer_reaches(0, 40):
            self.shot_cooldown -= 0.5
        
        if self.timer_reaches(1, 30):
            self.fleet_of_ships.average_spawn_speed += 50
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(2, 0):
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(3, 0):
            self.fleet_of_ships.max_count += 1
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(3, 30):
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(4, 30):
            self.shot_speed += 50

        if self.timer_reaches(5, 0):
            self.shot_quantity += 1
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(6, 0):
            self.fleet_of_ships.max_count += 1

        if self.timer_reaches(7, 0):
            self.fleet_of_ships.average_spawn_speed += 50
    
        if self.timer_reaches(9, 0):
            self.damage += 5
            self.fleet_of_ships.max_count += 1

        if self.timer_reaches(9, 30):
            self.life += 20

        if self.timer_reaches(10, 0):
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(11, 0):
            self.shot_inaccuracy -= 50

        if self.timer_reaches(13, 0):
            self.shot_inaccuracy -= 50
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(15, 0):
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.shot_cooldown -= 0.5

        if self.timer_reaches(17, 0):
            self.shot_inaccuracy -= 50

        if self.timer_reaches(20, 0):
            self.shot_speed += 50
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(22, 30):
            self.shot_inaccuracy -= 50

        if self.timer_reaches(25, 0):
            self.fleet_of_ships.max_count += 1
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(27, 30):
            self.shot_inaccuracy -= 50

        if self.timer_reaches(30, 0):
            self.shot_speed += 50
            self.shot_inaccuracy -= 50
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())

        if self.timer_reaches(60, 0):
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
            self.fleet_of_ships.create_enemy_ship('enemy_ship_boss', self.boss_parameters())
