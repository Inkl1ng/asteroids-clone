import pygame
import random
import math
import calc
from player import Player


class Asteroid(object):
    def __init__(self, surface, x, y) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.angle = random.randint(0, 360)
        self.VELOCITY = 5
        self.color = (0, 255, 255)
        self.rect = None

    def draw(self) -> None:
        radians = math.radians(self.angle)
        self.x -= self.VELOCITY * math.cos(radians)
        self.y -= self.VELOCITY * math.sin(radians)
        calc.off_screen(self)
        self.rect = pygame.draw.circle(self.surface, self.color, (self.x, self.y), 30)

    def collision(self, player: Player) -> None:
        if self.rect.colliderect(player):
            player.destruct()