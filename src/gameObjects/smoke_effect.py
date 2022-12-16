import pygame
import random
from src.pages.game_parts.window_game import HEIGHT, WIDTH, window



def scale(img: pygame.Surface, factor):
    w, h = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, (int(w), int(h)))


IMAGE = pygame.image.load('../assets/images/smoke.png').convert_alpha()


class SmokeParticle:
    def __init__(self, x=WIDTH // 2, y=HEIGHT // 2):
        self.x = x
        self.y = y
        self.scale_k = 0.1
        self.img = scale(IMAGE, self.scale_k)
        self.alpha = 255
        self.alpha_rate = 3
        self.alive = True
        self.vx = 0
        self.vy = 4 + random.randint(7, 10) / 10
        self.k = 0.01 * random.random() * random.choice([-1, 1])

    def update(self):
        self.x += self.vx
        self.vx += self.k
        self.y -= self.vy
        self.vy *= 0.99
        self.scale_k += 0.005
        self.alpha -= self.alpha_rate
        if self.alpha < 0:
            self.alpha = 0
            self.alive = False
        self.alpha_rate -= 0.1
        if self.alpha_rate < 1.5:
            self.alpha_rate = 1.5
        self.img = scale(IMAGE, self.scale_k)
        self.img.set_alpha(self.alpha)

    def draw(self):
        window.get_screen().blit(self.img, self.img.get_rect(center=(self.x, self.y)))


class Smoke:
    def __init__(self, x=WIDTH // 2, y=HEIGHT // 2 + 150):
        self.x = x
        self.y = y
        self.particles = []
        self.frames = 0

    def update(self):
        self.particles = [i for i in self.particles if i.alive]
        self.frames += 1
        if self.frames % 2 == 0:
            self.frames = 0
            self.particles.append(SmokeParticle(self.x, self.y))
        for i in self.particles:
            i.update()

    def draw(self):
        for i in self.particles:
            i.draw()

    

