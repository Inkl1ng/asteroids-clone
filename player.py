import pygame
import math
from main import SCREEN_WIDTH
from main import SCREEN_HEIGHT


class Player(object):
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.angle = 180
        self.radius = radius
        self.velocity = 10
        self.rotation_rate = 5

    def update_verticies(self):
        head_radians = math.radians(self.angle)
        left_radians = math.radians(self.angle + 120)
        right_radians = math.radians(self.angle - 120)

        self.verticies = [
            [self.x - round(math.cos(head_radians) * self.radius * 1.5), self.y - round(math.sin(head_radians) * self.radius * 1.5)],
            [self.x - round(math.cos(left_radians) * self.radius), self.y - round(math.sin(left_radians) * self.radius)],
            [self.x - round(math.cos(right_radians) * self.radius), self.y - round(math.sin(right_radians) * self.radius)]
        ]

    def draw(self):
        self.update_verticies()
        self.move()
        self.shoot()
        self.rotate()
        self.update_projectiles()

        for projectile in self.projectiles:
            projectile.draw()
        pygame.draw.polygon(self.surface, self.color, self.verticies)

    def move(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.x > 0 and self.x < SCREEN_WIDTH:
            self.x -= self.velocity * math.cos(math.radians(self.angle)) 
            self.y -= self.velocity * math.sin(math.radians(self.angle))
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and self.y > 0 and self.x < SCREEN_HEIGHT:
            self.x += self.velocity * math.cos(math.radians(self.angle))
            self.y += self.velocity * math.sin(math.radians(self.angle))

    def rotate(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_rate
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_rate