from abc import ABC, abstractmethod


class Cannon_ball_format(ABC):
    @abstractmethod
    def get_absolute_angle(self):
        raise NotImplementedError
    
    @abstractmethod
    def remove_cannon_ball(self, cannon_ball):
        raise NotImplementedError
