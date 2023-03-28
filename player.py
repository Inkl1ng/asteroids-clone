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
        self.ROTATION_RATE = 5
        self.velocity = 0
        self.velocity_angle_forward = 180
        self.velocity_angle_backward = calc.opposite_angle(self.velocity_angle_forward)
        self.x_velocity = 0
        self.y_velocity = 0
        self.MAX_VELOCITY = 20
        self.TIME_TO_ACCELERATE = 1
        self.moving = False
        # 60 is there because framerate is 60 fps
        # multiply by time to accelerate
        # ship will accelerate up to MAX_VELOCITY in 60 * TIME_TO_ACCELERATE seconds
        self.ACCELERATION_RATE = self.MAX_VELOCITY / (60 * self.TIME_TO_ACCELERATE)

    # all the necessary methods for the player to function in one method to call in main
    def draw(self):
        self.update_verticies()
        self.reset_angles()
        self.rotate()
        self.move()
        self.out_of_bounds()
        pygame.draw.polygon(self.surface, self.color, self.verticies, 1)

    # each vertex of the triangle is calculated as a point on a circle at a certain angle
    def update_verticies(self):
        head_radians = math.radians(self.angle)
        left_radians = math.radians(self.angle + 120)
        right_radians = math.radians(self.angle - 120)

        self.verticies = [
            [self.x - round(math.cos(head_radians) * self.RADIUS * 1.5), self.y - round(math.sin(head_radians) * self.RADIUS * 1.5)],
            [self.x - round(math.cos(left_radians) * self.RADIUS), self.y - round(math.sin(left_radians) * self.RADIUS)],
            [self.x - round(math.cos(right_radians) * self.RADIUS), self.y - round(math.sin(right_radians) * self.RADIUS)]
        ]

    def move(self):
        radians = math.radians(self.angle)
        keys = pygame.key.get_pressed()

        # limit speed by velocity
        # complete freedom of movement whilst at max speed
        if self.velocity <= self.MAX_VELOCITY:
            self.at_max_speed = False
            if keys[pygame.K_w]:
                self.x_velocity += self.ACCELERATION_RATE * math.cos(radians)
                self.y_velocity += self.ACCELERATION_RATE * math.sin(radians)
            elif keys[pygame.K_s]:
                self.x_velocity -= self.ACCELERATION_RATE * math.cos(radians)
                self.y_velocity -= self.ACCELERATION_RATE * math.sin(radians)
        elif self.velocity >= self.MAX_VELOCITY:
            self.velocity_angle_forward = self.angle
            self.velocity_angle_backward = calc.opposite_angle(self.velocity_angle_forward)
            self.velocity = calc.pythagorean(self.x_velocity, self.y_velocity)
            # allows player to accelerate backwards down while at max speed
            if (self.velocity_angle_forward == self.angle) and keys[pygame.K_s]:
                self.x_velocity -= self.ACCELERATION_RATE * math.cos(radians)
                self.y_velocity -= self.ACCELERATION_RATE * math.sin(radians)
            if (self.velocity_angle_backward == self.angle) and keys[pygame.K_w]:
                self.x_velocity += self.ACCELERATION_RATE * math.cos(radians)
                self.y_velocity += self.ACCELERATION_RATE * math.sin(radians)

        self.x -= self.x_velocity
        self.y -= self.y_velocity
        
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



    def reset_angles(self):
        if self.angle == 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360 + self.angle
