import pygame
import math
import calc


class Player(object):
    def __init__(self, surface: pygame.Surface, color: tuple[int, int, int], x: int, y: int, radius: int):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.RADIUS = radius

        self.angle = 180
        self.ROTATION_RATE = 180 / 60 # 180 degrees per second
        self.velocity = 15
        self.x_velocity = 0
        self.y_velocity = 0
        self.MAX_VELOCITY = 15
        self.TIME_TO_ACCELERATE = 1
        # 60 is there because framerate is 60 fps
        # multiply by time to accelerate
        # ship will accelerate up to MAX_VELOCITY in 60 * TIME_TO_ACCELERATE seconds
        self.ACCELERATION_RATE = self.MAX_VELOCITY / (60 * self.TIME_TO_ACCELERATE)
        self.DECCELERATION_RATE = 0.95

    # all the necessary methods for the player to function in one method to call in main
    def draw(self):
        verticies = self.calc_verticies()
        self.reset_angles()
        self.move()
        self.out_of_bounds()
        pygame.draw.polygon(self.surface, self.color, verticies, 1)

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
            self.x_velocity *= 0.98
            self.y_velocity *= 0.98

        self.velocity = calc.pythagorean(self.x_velocity, self.y_velocity)
        if self.velocity > self.MAX_VELOCITY:
            ratio = self.MAX_VELOCITY / self.velocity
            self.x_velocity *= abs(ratio)
            self.y_velocity *= abs(ratio)
        # if keys[pygame.K_w]:
        #     self.x_velocity -= self.ACCELERATION_RATE * math.cos(radians)
        #     self.y_velocity -= self.ACCELERATION_RATE * math.sin(radians)

        self.x += self.x_velocity
        self.x = round(self.x)
        self.y += self.y_velocity
        self.y = round(self.y)
        
    # moves player onto other side of the screen if they go off screen
    def out_of_bounds(self):
        if self.x < 0:
            self.x = self.surface.get_width()
        elif self.x > self.surface.get_width():
            self.x = 0
        
        if self.y < 0:
            self.y = self.surface.get_height()
        elif self.y > self.surface.get_height():
            self.y = 0

    def rotate(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= self.ROTATION_RATE
        if keys[pygame.K_RIGHT]:
            self.angle += self.ROTATION_RATE

    def reset_angles(self):
        if self.angle == 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360 + self.angle
