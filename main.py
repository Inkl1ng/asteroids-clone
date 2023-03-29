import pygame
import sys
import os
from player import Player


def main():
    pygame.init()
    os.system('cls||clear')
    running = True
    screen_width = 1280
    screen_height = 720
    basic_colors = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((screen_width, screen_height))
    player = Player(window, basic_colors['white'], 100, 40, 40)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        print(f"{player.velocity}\t{player.x}\t{player.y}\t{player.angle}\t{len(player.projectiles)}")
        window.fill((0, 0, 0))
        player.draw()
        player.draw_projectiles()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
