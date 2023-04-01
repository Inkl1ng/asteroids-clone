import pygame
import math
import calc
import random


class Player:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.angle = 0
        self.x = 400 - 30
        self.y = 400 - 17
        self.x_velocity = 0
        self.y_velocity = 0
        self.moving = False
        self.MAX_VELOCITY = 10
        self.ACCELERATION_RATE = 10 / (60 * 2)
        self.DECCELERATION_RATE = 0.96
        self.ROTATION_RATE = 5

    # handles player movement and shooting
    # rotation is handled in main.py because the ship rotates by rotating its surface
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        radians = math.radians(self.angle)

        if keys[pygame.K_LEFT]:
            self.angle -= self.ROTATION_RATE
        if keys[pygame.K_RIGHT]:
            self.angle += self.ROTATION_RATE

        if keys[pygame.K_w]:
            self.moving = True
        else:
            self.moving = False

        if self.moving:
            self.x_velocity += self.ACCELERATION_RATE * math.cos(radians)
            self.y_velocity += self.ACCELERATION_RATE * math.sin(radians)
            resultant_velocity = calc.pythagorean(self.x_velocity, self.y_velocity)
            if resultant_velocity > self.MAX_VELOCITY:
                # keeps the velocity of the ship under MAX_VELOCITY by scaling down the velocity vectors
                # keeps the angle of the resultant velocity the same but just keeps them slower
                ratio = self.MAX_VELOCITY / resultant_velocity
                self.x_velocity *= abs(ratio)
                self.y_velocity *= abs(ratio)
        else:
            self.x_velocity *= self.DECCELERATION_RATE
            self.y_velocity *= self.DECCELERATION_RATE

        self.x += self.x_velocity
        self.y += self.y_velocity

        calc.off_screen(self)

    def draw(self) -> None: 
        head_radians = math.radians(self.angle)
        left_radians = math.radians(self.angle - 120)
        right_radians = math.radians(self.angle + 120)
        verticies = [
            [30 + (20 * math.cos(head_radians) * 1.5), 30 + (20 * math.sin(head_radians) * 1.5)],
            [30 + (20 * math.cos(left_radians)), 30 + (20 * math.sin(left_radians))],
            [30 + (20 * math.cos(right_radians)), 30 + (20 * math.sin(right_radians))]
        ]
        self.surface.fill((0,0,0))
        pygame.draw.polygon(self.surface, (255, 255, 255), verticies, 1)

if __name__ == '__main__':
    angle = 180
    head_radians = math.radians(angle)
    left_radians = math.radians(angle - 120)
    right_radians = math.radians(angle + 120)
    verticies = [
        [(-20 * math.cos(head_radians) * 1.5), -20 * math.sin(head_radians) * 1.5],
        [20 * math.cos(left_radians), 20 * math.sin(left_radians)],
        [20 * math.cos(right_radians), 20 * math.sin(right_radians)]
    ]
    for vertex in verticies:
        print(vertex)
