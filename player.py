import pygame
import math
import calc
from projectile import Projectile


class Player(object):
    def __init__(self, surface, color: tuple[int, int, int], x: int, y: int, radius: int):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.verticies = []
        self.RADIUS = radius

        self.angle = 180
        self.ROTATION_RATE = 180 / 60 # 180 degrees per second
        self.velocity = 15
        self.x_velocity = 0
        self.y_velocity = 0
        self.MAX_VELOCITY = 10
        self.TIME_TO_ACCELERATE = 1
        # 60 is there because framerate is 60 fps
        # multiply by time to accelerate
        # ship will accelerate up to MAX_VELOCITY in 60 * TIME_TO_ACCELERATE seconds
        self.ACCELERATION_RATE = self.MAX_VELOCITY / (60 * self.TIME_TO_ACCELERATE)
        self.DECCELERATION_RATE = 0.90

        self.projectiles = []
        # SHOT_TIMER / 1000 = time between shots in SECOND
        # ex. 500 / 1000 = 0.5 seconds
        self.SHOT_TIMER =  250
        self.last_shot = 0

        self.rect = None
        self.alive = True

    # all the necessary methods for the player to function in one method to call in main
    def draw(self):
        self.verticies = self.calc_verticies()
        if self.alive:
            self.reset_angles()
            self.move()
            self.shoot()
            calc.off_screen(self)
            self.rect = pygame.draw.polygon(self.surface, self.color, self.verticies, 1)
        else:
            pygame.draw.polygon(self.surface, (255,0,0), self.verticies)

    # each vertex of the triangle is calculated as a point on a circle at a certain angle
    def calc_verticies(self) -> list[list[int, int], list[int, int], list[int, int]]:
        head_radians = math.radians(self.angle)
        left_radians = math.radians(self.angle + 120)
        right_radians = math.radians(self.angle - 120)

        verticies = [
            [self.x - round(math.cos(head_radians) * self.RADIUS * 1.5),
             self.y - round(math.sin(head_radians) * self.RADIUS * 1.5)],
            [self.x - round(math.cos(left_radians) * self.RADIUS),
             self.y - round(math.sin(left_radians) * self.RADIUS)],
            [self.x - round(math.cos(right_radians) * self.RADIUS),
             self.y - round(math.sin(right_radians) * self.RADIUS)]
        ]
        return verticies

    def move(self):
        keys = pygame.key.get_pressed()

        # self.velocity = calc.pythagorean(self.x_velocity, self.y_velocity)
        self.rotate()
        radians = math.radians(self.angle)

        if keys[pygame.K_q]:
            self.x_velocity = 0
            self.y_velocity = 0
        if keys[pygame.K_w]:
            self.x_velocity -= self.ACCELERATION_RATE * math.cos(radians)
            self.y_velocity -= self.ACCELERATION_RATE * math.sin(radians)
        else:
            # i have no how this works
            # i just put in a random number and it works
            # every frame the ship's velocity is reduced by 98%
            # idk how this adds up over time but it works :)
            self.x_velocity *= 0.98
            self.y_velocity *= 0.98

        self.velocity = calc.pythagorean(self.x_velocity, self.y_velocity)
        if self.velocity > self.MAX_VELOCITY:
            ratio = self.MAX_VELOCITY / self.velocity
            self.x_velocity *= abs(ratio)
            self.y_velocity *= abs(ratio)

        self.x += self.x_velocity
        # self.x = round(self.x)
        self.y += self.y_velocity
        # self.y = round(self.y)

    def rotate(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= self.ROTATION_RATE
        if keys[pygame.K_RIGHT]:
            self.angle += self.ROTATION_RATE

    def shoot(self):
        keys = pygame.key.get_pressed()
        head_vertex = 0
        head_x = self.verticies[head_vertex][0]
        head_y = self.verticies[head_vertex][1]
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and current_time > self.last_shot:
            # updates when the last shot was taken
            self.last_shot = current_time + self.SHOT_TIMER
            self.projectiles.append(Projectile(self.surface, head_x, head_y, self.velocity, self.angle))

    def draw_projectiles(self):
        for projectile in self.projectiles:
            # checks if the projectile are off screen and delete them if they are
            if projectile.x < 0 or projectile.x > projectile.surface.get_width():
                self.projectiles.pop(self.projectiles.index(projectile))
            elif projectile.y < 0 or projectile.y > projectile.surface.get_height():
                self.projectiles.pop(self.projectiles.index(projectile))
            else:
                projectile.draw()

    # keeps the angles between 0 and 359 for ease of tracking
    # for example -10 degrees gets converted to 350 degrees
    # 375 gets convereted to 15
    def reset_angles(self):
        if self.angle == 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360 + self.angle

    def destruct(self):
        self.alive = False