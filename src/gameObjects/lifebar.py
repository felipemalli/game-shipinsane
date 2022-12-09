import pygame
from PPlay.sprite import Sprite
from src.pages.game_parts.window_game import HEIGHT, WIDTH

from .player import Player


class Life_Bar:
    def __init__(self, entity_object, center_x, center_y, actual, max, size, thickness):
        self.entity_object = entity_object
        self.center_x = center_x                     #posicao x da barra
        self.center_y = center_y                    #posicao y da barra
        self.actual = actual                         #valor atual da vida
        self.max = max                              #maximo valor de vida
        self.size = size                            #comprimento da barra de vida
        self.thickness = thickness                      #espessura da barra de vida
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))   
        self.ext_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.color = (255, 0, 0)
        self.ext_color = (0, 0, 0)

    def update_life(self):
        self.actual = self.entity_object.get_life()
    
    def draw(self):
        self.update_life()
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.center_x, self.center_y, (self.actual / self.max) * self.size, self.thickness))
        pygame.draw.rect(self.ext_surface, self.ext_color, pygame.Rect(self.center_x, self.center_y, self.size, self.thickness), 2)
    