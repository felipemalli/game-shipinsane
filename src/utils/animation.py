from src.pages.game_parts.window_game import window


class Animation:
    def __init__(self, sprites, initial_timer = 100):
        self.sprites = sprites
        self.actual_sprite = sprites[0]
        self.actual_sprite_i = 0
        self.is_scroll_on = False
        self.max_timer = 100
        self.timer = initial_timer

        self.reverse = True
        self.reverse_loop = False

    def reset_scroll(self, initial_index):
        self.actual_sprite = self.sprites[initial_index]
        self.actual_sprite_i = initial_index

    def active_scroll(self, initial_index = 0):
        if initial_index == 1: initial_index = len(self.sprites) - 1
        self.reset_scroll(initial_index)
        self.is_scroll_on = True

    def get_next_sprite(self, circular = False):
        self.actual_sprite_i += 1
        if self.actual_sprite_i >= len(self.sprites):
            self.actual_sprite_i = 0
            if not circular: return None
        return self.sprites[self.actual_sprite_i]

    def get_previous_sprite(self, circular = False):
        self.actual_sprite_i -= 1
        if self.actual_sprite_i < 0:
            self.actual_sprite_i = len(self.sprites) - 1
            if not circular: return None
        return self.sprites[self.actual_sprite_i]

    def render_order_scroll(self, speed, delta_time):
        if self.is_scroll_on and self.actual_sprite:
            self.timer -= (delta_time * speed)
            self.actual_sprite.draw()

            if self.timer <= 0:
                self.actual_sprite = self.get_next_sprite()
                self.timer = self.max_timer
                if not self.actual_sprite: 
                    self.is_scroll_on = False
                    self.reverse_loop = True
                    self.reverse = True

    def render_inverse_scroll(self, speed, delta_time):
        if self.is_scroll_on and self.actual_sprite:
            self.timer -= (delta_time * speed)
            self.actual_sprite.draw()

            if self.timer <= 0:
                self.actual_sprite = self.get_previous_sprite()
                self.timer = self.max_timer
                if not self.actual_sprite: 
                    self.is_scroll_on = False
                    self.reverse_loop = False
                    self.reverse = False
                    self.reset_scroll(len(self.sprites) - 1)

    def render_back_and_forth(self, speed, delta_time):
        if not self.reverse_loop:
            self.render_order_scroll(speed, delta_time)
        if self.reverse_loop:
            if self.reverse:
                self.active_scroll(len(self.sprites) - 2)
                self.reverse = False
            self.render_inverse_scroll(speed, delta_time)

    def infinite_scroll(self, speed, delta_time):
        self.timer -= (delta_time * speed)
        self.actual_sprite.draw()

        if self.timer <= 0:
            self.actual_sprite = self.get_next_sprite(True)
            self.timer = self.max_timer
    