import random

from .ship import Ship


class Fleet_of_ships:
    def __init__(self, island, max_count = 10, average_spawn_speed = 400, enemy_ship_life = 100, enemy_ship_speed = 25):
        self.island = island
        self.enemy_ships = []
        self.max_count = max_count
        self.enemy_ship_life = enemy_ship_life
        self.enemy_ship_speed = enemy_ship_speed
        self.average_spawn_speed = average_spawn_speed

        self.spawn_speed = self.average_spawn_speed
        self.next_ship_initial_timer = 1000
        self.next_ship_timer = self.next_ship_initial_timer
    
    def generate_enemy_ships(self, delta_time):
        if len(self.enemy_ships) < self.max_count and self.next_ship_timer > 0:
            self.next_ship_timer -= self.spawn_speed * delta_time
        
        if self.next_ship_timer <= 0:
            self.spawn_speed = self.generate_random_num_around(self.average_spawn_speed, 30)
            self.next_ship_timer = self.next_ship_initial_timer
            self.create_enemy_ship()

    def create_enemy_ship(self):
        enemy_ship = Ship(self.island, self.enemy_ship_life, self.enemy_ship_speed)
        self.enemy_ships.append(enemy_ship)

    def render_ships(self, delta_time):
        print(self.enemy_ships)
        for enemy_ship in self.enemy_ships:
            enemy_ship.draw()
            enemy_ship.move(delta_time)

    def generate_random_num_around(self, num, proximity):
        min_num = num - proximity
        max_num = num + proximity
        return random.randint(min_num, max_num)