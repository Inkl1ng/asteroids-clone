import pygame
import sys
import os

class Player:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel
        if keys[pygame.K_w]:
            self.y -= self.vel
        if keys[pygame.K_s]:
            self.y += self.vel
    
    def out_of_bounds(self):
        if self.x < 0:
            self.x = SCREEN_WIDTH
        if self.x > SCREEN_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT
        if self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self):
        self.move()
        self.out_of_bounds()
        pygame.draw.rect(self.surface, (255, 255, 255), (self.x, self.y, self.width, self.height))

def main():
    pygame.init()
    RUNNING = True
    global SCREEN_WIDTH 
    global SCREEN_HEIGHT
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(window, 40, 100, 40, 40)

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((0, 0, 0))
        player.draw()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()