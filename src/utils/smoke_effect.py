import random

import pygame
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window


def scale(img: pygame.Surface, factor):
    w, h = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, (int(w), int(h)))



class SmokeParticle:
    def __init__(self, x=WIDTH // 2, y=HEIGHT // 2, initial_height = 4, min_random_height = 7, max_random_height = 10, scale_k = 0.1, x_variaton = 1, image_path = '../assets/images/smoke.png'):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y
        self.initial_height = initial_height
        self.min_random_height = min_random_height
        self.max_random_height = max_random_height
        self.scale_k = scale_k
        self.img = scale(self.image, self.scale_k)
        self.alpha = 255
        self.alpha_rate = 3
        self.alive = True
        self.vx = random.randint(-self.min_random_height, self.max_random_height) / 10
        self.vy = self.initial_height + random.randint(self.min_random_height, self.max_random_height) / 10
        self.k = 0.01 * random.random() * random.choice([-1, 1]) * x_variaton

    def update(self, delta_time = 1):
        if delta_time != 1: delta_time *= 100
        self.x += self.vx
        self.vx += self.k
        self.y -= self.vy
        self.vy *= 0.99
        self.scale_k += 0.005
        self.alpha -= self.alpha_rate
        if self.alpha < 0:
            self.alpha = 0
            self.alive = False
        self.alpha_rate -= 0.1 * delta_time
        if self.alpha_rate < 1.5:
            self.alpha_rate = 1.5
        self.img = scale(self.image, self.scale_k)
        self.img.set_alpha(self.alpha)

    def draw(self):
        window.get_screen().blit(self.img, self.img.get_rect(center=(self.x, self.y)))


class Smoke:
    def __init__(self, x=WIDTH // 2, y=HEIGHT // 2 + 150, speed = 150, initial_height = 4, min_random_height = 7, max_random_height = 10, scale = 0.1):
        self.x = x
        self.y = y
        self.particles = []
        self.frames = 0
        self.speed = speed
        self.initial_height = initial_height
        self.min_random_height = min_random_height
        self.max_random_height = max_random_height
        self.scale = scale
        self.speed_timer = 5
        self.generate_more = True

    def update(self, delta_time):
        self.particles = [i for i in self.particles if i.alive]
        self.frames += delta_time
        if self.frames >= 0 and self.generate_more:
            self.frames = -0.1
            self.particles.append(SmokeParticle(self.x, self.y, self.initial_height, self.min_random_height, self.max_random_height, self.scale))
        
        self.speed_timer -= delta_time * self.speed
        if self.speed_timer <= 0:
            self.speed_timer = 5
            for i in self.particles:
                i.update()

    def draw(self):
        for i in self.particles:
            i.draw()

    

