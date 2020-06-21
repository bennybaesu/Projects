import media
import pygame


class Rocket:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = media.rocket_sprite()
        self.hitbox = (self.x + 70, self.y + 18, 53, 130)
        self.explosion_sprite = media.explosion_image()

    def update(self):
        self.hitbox = (self.x + 70, self.y + 18, 53, 130)


    def reset(self, x, y):
        self.x = x
        self.y = y


