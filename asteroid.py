import pygame
import random
import math
import calc


class Asteroid(object):
    """
    A class to represent the asteroids
    
    Attributes
    ----------
    surface : pygame.Surface
        the surface that the asteroid will be drawn on
    x : float
        x position of the asteroid
    y : float
        y position of the asteroid
    angle : int
        angle that the asteroid is moving at
    color : tuple[int, int, int]
        color of the outline of the asteroid
    """
    def __init__(self, surface, x, y) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.angle = random.randint(0, 360)
        self.color = (0, 255, 255)
        self.rect = None
        self.VELOCITY = 5

    def draw(self) -> None:
        radians = math.radians(self.angle)
        self.x -= self.VELOCITY * math.cos(radians)
        self.y -= self.VELOCITY * math.sin(radians)
        calc.off_screen(self)
        self.rect = pygame.draw.circle(self.surface, self.color,
                                       (self.x, self.y), 30)
