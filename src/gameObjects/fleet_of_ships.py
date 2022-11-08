import random


class Fleet_of_ships:
    def __init__(self, max_count, average_spawn_speed):
        self.enemy_ships = []
        self.max_count = max_count
        self.average_spawn_speed = average_spawn_speed

        self.spawn_speed = self.average_spawn_speed
        self.next_ship_initial_timer = 100
        self.next_ship_timer = self.next_ship_initial_timer
    
    def generate_enemy_ships(self, delta_time):
        if len(self.enemy_ships) < self.max_count and self.next_ship_timer > 0:
            self.next_ship_timer -= self.random_spawn_speed * delta_time
        
        if self.next_ship_timer <= 0:
            self.spawn_speed = self.generate_random_num_around(self.enemy_ship_spawn_speed, 1/3)
            self.next_ship_timer = self.next_ship_initial_timer
            self.create_enemy_ship()
  
    def generate_random_num_around(self, num, proximity):
        min_num = num / proximity
        max_num = num * proximity
        return random.randint(min_num, max_num)

    def create_enemy_ship(self):
        enemy_ship = Ship(self)
        self.enemy_ships.append(enemy_ship)
