import pygame
import math
import calc
import random


class Player:
    """
    A class to represent the player. Handles inputs from the player for
    movement and shooting.

    Attributes
    ---------
    surface : pygame.Surface
        the surface that the player will be drawn on. that same surface
        is then drawn on the screen
    angle : float
        angle the player is facing, greater than 0, less than 360
    x : float
        x position of the player
    y : float
        y position of the player
    x_velocity : float
        x_velocity of the player
    y_velocity : float
        y_velocity of the player
    moving : bool
        keeps track of if the player if a movement key is pressed down
    mask : pygame.Mask
        mask of surface, used for collision detection
    MAX_VELOCITY : int
        max velocity of the player, player can go a little over it becuase
        of how the limit is enforced
    ACCELERATION_RATE : float
        how fast the player accelerates
        formula: MAX_VELOCITY / (framerate * time_to_reach_max_speed)
        time_to_reach_max_speed is in seconds
    DECELERATION_RATE : float
        how fast the player decelerates
        x and y velocities are multiplied by this every frame
    ROTATION_RATE : int
        how much the player rotates in a single frame (degrees)
        formula: (degrees to rate in a second) / framerate

    Methods
    -------
    update()
        handles player roation, movement, and shooting
    draw()
        calculates the verticies and draws the resulting triangle on to
        self.surface
    """
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.angle = 0
        self.x = 400 - 15
        self.y = 400
        self.x_velocity = 0
        self.y_velocity = 0
        self.moving = False
        self.mask = None
        self.MAX_VELOCITY = 10
        self.ACCELERATION_RATE = self.MAX_VELOCITY / (60 * 2)
        self.DECELERATION_RATE = 0.96
        self.ROTATION_RATE = 270 / 60

    # handles player movement, rotation, and shooting
    def update(self) -> None:
        """
        Handles player rotation, movement, and shooting
        """
        keys = pygame.key.get_pressed()
        radians = math.radians(self.angle)

        # rotation
        if keys[pygame.K_LEFT]:
            self.angle -= self.ROTATION_RATE
        if keys[pygame.K_RIGHT]:
            self.angle += self.ROTATION_RATE

        # normalizes angle to be between 0 and 359 for ease of debugging
        if self.angle < 0:
            self.angle = 360 + self.angle
        elif self.angle > 359:
            self.angle = 360 - self.angle

        # movement
        if keys[pygame.K_w]:
            self.moving = True
        else:
            self.moving = False

        if self.moving:
            self.x_velocity += self.ACCELERATION_RATE * math.cos(radians)
            self.y_velocity += self.ACCELERATION_RATE * math.sin(radians)
            resultant_velocity = calc.pythagorean(self.x_velocity, 
                    self.y_velocity)
            if resultant_velocity > self.MAX_VELOCITY:
                # keeps the velocity of the ship under MAX_VELOCITY
                # by scaling down the velocity vectors
                # keeps the angle of the resultant velocity the same
                #  but just keeps them slower
                ratio = self.MAX_VELOCITY / resultant_velocity
                self.x_velocity *= abs(ratio)
                self.y_velocity *= abs(ratio)
        else:
            self.x_velocity *= self.DECELERATION_RATE
            self.y_velocity *= self.DECELERATION_RATE

        self.x += self.x_velocity
        self.y += self.y_velocity

        # resets player location to stay within the screen
        # randomly chooses a point to place the player after they go off screen
        if self.x < -30:
            self.x = 800
            self.y = random.randint(0, 801)
        elif self.x > 800 + 10:
            self.x = 0
            self.y = random.randint(0, 801)
        if self.y < -30:
            self.x = random.randint(0, 801)
            self.y = 800
        elif self.y > 800 + 10:
            self.x = random.randint(0, 801)
            self.y = 0

        calc.off_screen(self)

    def draw(self) -> None:
        """
        calculates the verticies and draws the 
        resulting triangle on to self.surface
        """
        head_radians = math.radians(self.angle)
        left_radians = math.radians(self.angle - 120)
        right_radians = math.radians(self.angle + 120)
        # triangle is 3 points a certain radius away and a 
        # certain angle from the center point (30, 30) in player_surface
        verticies = [
            [30 + (20 * math.cos(head_radians) * 1.5), # head vertex x
             30 + (20 * math.sin(head_radians) * 1.5)], # head vertex y
            [30 + (20 * math.cos(left_radians)), # left vertex x
             30 + (20 * math.sin(left_radians))], # left vertex y
            [30 + (20 * math.cos(right_radians)), # right vertex x
             30 + (20 * math.sin(right_radians))] # right vertex y 
        ]
        self.surface.fill((0,0,0))
        pygame.draw.polygon(self.surface, (255, 255, 255), verticies, 1)
        self.mask = pygame.mask.from_surface(self.surface)
