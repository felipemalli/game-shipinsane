from abc import ABC, abstractmethod


class Cannon_ball_format(ABC):

    @abstractmethod
    def remove_cannon_ball(self, cannon_ball):
        raise NotImplementedError
