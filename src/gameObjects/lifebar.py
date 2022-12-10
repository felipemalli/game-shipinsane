from abc import ABC, abstractmethod

import pygame
from src.pages.game_parts.window_game import window


class I_Life_bar(ABC):
    @abstractmethod
    def get_life(self):
        raise NotImplementedError

class Life_bar:
    def __init__(self, entity_object, max_life, actual_life, x, y, size, thickness, heart_sprite = False):
        self.entity_object = entity_object
        self.max_life = max_life
        self.actual_life = actual_life
        self.x = x
        self.y = y
        self.size = size
        self.thickness = thickness
        self.color = (255, 0, 0)
        self.ext_color = (0, 0, 0)
        self.heart = self.create_heart(heart_sprite)

    def create_heart(self, heart_sprite):
        if heart_sprite: 
            heart = heart_sprite
            heart.x = self.x - (heart.width / 2)
            heart.y = self.y - (self.thickness / 3)
            return heart
        return False

    def update_life(self):
        self.actual_life = self.entity_object.get_life()

    def draw(self):
        self.update_life()
        pygame.draw.rect(window.get_screen(), self.color, pygame.Rect(self.x, self.y, (self.actual_life / self.max_life) * self.size, self.thickness))
        pygame.draw.rect(window.get_screen(), self.ext_color, pygame.Rect(self.x, self.y, self.size, self.thickness), 2)
        if self.heart: self.heart.draw()
