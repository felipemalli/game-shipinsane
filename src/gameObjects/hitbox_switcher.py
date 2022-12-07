import pygame


class Hitbox_switcher:
    TOGGLE_COOLDOWN = 5

    def __init__(self, game_object_list):
        self.game_object_list = game_object_list
        self.toggle_cooldown = self.TOGGLE_COOLDOWN

    def toggle_hitbox(self):
        for game_object in self.game_object_list:
            game_object.toggle_hitbox()

    def draw(self, delta_time):
        if self.toggle_cooldown > 0:
            self.toggle_cooldown -= 10 * delta_time

        if self.toggle_cooldown <= 0 and pygame.key.get_pressed()[pygame.K_F1]:
            self.toggle_hitbox()
            self.toggle_cooldown = self.TOGGLE_COOLDOWN

