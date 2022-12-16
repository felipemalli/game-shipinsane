import random

from .ship import Ship


class Fleet_of_ships:
    enemy_ships = []

    def __init__(self, island, max_count = 2, average_spawn_speed = 100):
        self.island = island
        self.max_count = max_count
        self.average_spawn_speed = average_spawn_speed
        self.show_hitbox = False

        self.targets = []

        self.spawn_speed = self.average_spawn_speed
        self.next_ship_initial_timer = 1000
        self.next_ship_timer = 1

    def add_target(self, target):
        self.targets.append(target)

    def toggle_hitbox(self):
        self.show_hitbox = not self.show_hitbox

    def generate_enemy_ships(self, delta_time, parameters = None):
        # print(self.spawn_speed)
        if len(Fleet_of_ships.enemy_ships) < self.max_count and self.next_ship_timer > 0:
            self.next_ship_timer -= self.spawn_speed * delta_time
        if self.next_ship_timer <= 0:
            self.spawn_speed = self.generate_random_num_around(self.average_spawn_speed, 30)
            self.next_ship_timer = self.next_ship_initial_timer
            self.create_enemy_ship('enemy_ship', parameters)

    def create_enemy_ship(self, image_name = 'enemy_ship', parameters = None):
        if parameters: enemy_ship = Ship(self.island, image_name, *parameters)
        else: enemy_ship = Ship(self.island, image_name)
        Fleet_of_ships.enemy_ships.append(enemy_ship)

    def render_ships(self, delta_time, player):
        for enemy_ship in Fleet_of_ships.enemy_ships:
            enemy_ship.set_show_hitbox(self.show_hitbox)
            enemy_ship.draw()
            enemy_ship.render_shots(delta_time, self.targets)
            if enemy_ship.is_moving: enemy_ship.move(delta_time)
            if enemy_ship.is_shooting and player.life > 0: enemy_ship.shot(delta_time)

        for enemy_ship in Fleet_of_ships.enemy_ships:
            enemy_ship.check_death(self.enemy_ships, delta_time)

    def generate_random_num_around(self, num, proximity):
        min_num = num - proximity
        max_num = num + proximity
        return random.randint(min_num, max_num)
