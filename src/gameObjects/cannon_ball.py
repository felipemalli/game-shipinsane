from PPlay.sprite import Sprite


class Cannon_ball:
    def __init__(self, speed, cannon_object):
        self.cannon_object = cannon_object
        self.speed = speed                  # speed with delta_time included!
        self.cannon_ball = Sprite("cannon_ball.png")
        self.cannon_ball.x = cannon_object.x + (cannon_object.width / 2) - (self.cannon_ball.width / 2)
        self.cannon_ball.y = cannon_object.y - self.cannon_ball.height

    def draw(self):
        self.cannon_ball.draw()

    def get_x_position(self):
        return self.cannon_ball.x

    def get_y_position(self):
        return self.cannon_ball.y
    
    def set_y_position(self, y_position):
        self.cannon_ball.y = y_position

    def up_y_position(self, y_increment_position):
        self.cannon_ball.y -= y_increment_position

    def get_is_on_screen(self):
        return self.is_on_screen

    def move_up(self):
        if self.cannon_ball.y >= 0:
            y_increment = self.speed
            self.up_y_position(y_increment)
        else:
            self.cannon_object.remove_cannon_ball(self)
