import pygame
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window
from .player import Player
from PPlay.sprite import Sprite

class Life_Bar:
    def __init__(self, center_x, center_y, actual, max, size, thickness):
        
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
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.center_x, self.center_y, (self.actual / self.max) * self.size, self.thickness))
        pygame.draw.rect(self.ext_surface, self.ext_color, pygame.Rect(self.center_x, self.center_y, self.size, self.thickness), 2)
    