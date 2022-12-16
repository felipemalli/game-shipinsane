import math

from src.pages.game_parts.window_game import WIDTH
from utils.text_utils import Text_utils


class Pontuation:
    PONTUATION = 0
    TIME_SECONDS = 0

    @classmethod
    def add_pontuation(self, pontuation):
        self.PONTUATION += (pontuation + (pontuation * (self.TIME_SECONDS / 150)))

    @classmethod
    def draw(self):
        Text_utils.draw_text(('Pontuation: ' + str(math.floor(self.PONTUATION))), 30, WIDTH / 2, 20)

    @classmethod
    def update_time_by_seconds(self, time_seconds):
        self.TIME_SECONDS = time_seconds
