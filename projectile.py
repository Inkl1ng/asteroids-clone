import pygame
import math


class Projectile(object):
    def __init__(self, surface, x: float, y: float, shot_velocity: float, angle: int):
        self.surface = surface
        self.COLOR = (255, 255, 255)
        self.x = x
        self.y = y
        self.shot_velocity = shot_velocity
        self.angle = angle
        self.VELOCITY = 20
        self.RADIUS = 5

    def draw(self):
        radians = math.radians(self.angle)  
        self.x -= self.VELOCITY * math.cos(radians)
        self.y -= self.VELOCITY * math.sin(radians)

        pygame.draw.circle(self.surface, self.COLOR, (self.x, self.y), self.RADIUS)