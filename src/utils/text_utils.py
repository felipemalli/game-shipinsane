import pygame
from src.pages.game_parts.window_game import window


class Text_utils:
    @classmethod
    def draw_text(self, text, font_size, center_x, center_y, font = "Arial"):
        font_sys = pygame.font.SysFont(font, font_size, False, False)
        text_render = font_sys.render(text, False, (0,0,0))
        text_rect = text_render.get_rect(center=(center_x, center_y))
        window.get_screen().blit(text_render, text_rect)
