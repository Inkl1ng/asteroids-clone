import pygame
import sys
from player import Player


def main():
    RUNNING = True
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    # center_of_screen = pygame.Rect(400, 400, 3, 3)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    player_surface = pygame.Surface((60,60))
    # player_surface.fill((0,0,0))
    player = Player(player_surface)

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        player.update()

        print(f"{player.x_velocity}\t{player.y_velocity}\t{player.x}\t{player.y}\t{player.angle}")

        screen.fill((0, 0, 0))
        player.draw()
        screen.blit(player_surface, [player.x, player.y])
        # pygame.draw.rect(screen, (255,0,0), center_of_screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    main()
