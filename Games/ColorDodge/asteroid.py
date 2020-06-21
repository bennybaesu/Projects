import pygame
import media
import random


def random_color():
    x = random.randrange(0, 5)
    return x


class Asteroid:
    sprite: object

    def __init__(self, i, w):
        self.color = random_color()
        self.width = w
        self.radius = 48
        self.x = random.randrange(0, w - 400)
        self.y = -i
        self.sprite = media.asteroid_sprite(self.color)
        self.center = [self.x + 72, self.y + 74]
        self.hit = False

    def attributes(self):
        return self

    def new_game(self, i, w):
        self.color = random_color()
        self.width = w
        self.radius = 48
        self.x = random.randrange(0, w - 400)
        self.y = -i
        self.sprite = media.asteroid_sprite(self.color)
        self.center = [self.x + 72, self.y + 74]
        self.hit = False

    def update(self):
        self.center = [self.x + 72, self.y + 74]

    def fall(self, speed):
        self.y += speed
        if self.y >= 750:
            self.reset()

    def reset(self):
        self.color = random_color()
        self.sprite = media.asteroid_sprite(self.color)
        self.x = random.randrange(0, self.width - 500)
        self.y = -500
        self.hit = False
