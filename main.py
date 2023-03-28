import pygame
import sys
import os
from player import Player

def main():
    pygame.init()
    os.system('cls'| 'clear')
    RUNNING = True
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