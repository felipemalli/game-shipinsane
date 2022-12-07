import pygame
from src.pages.game_parts.window_game import window


class Contact_circle:
    def __init__(self, x, y, size, thickness, color):
        self.x = x
        self.y = y
        self.size = size
        self.thickness = thickness
        self.color = color
        self.sprite = None

    def draw(self):
        self.sprite = pygame.draw.circle(window.get_screen(), self.color, [self.x, self.y], self.size, self.thickness)
        return self.sprite

