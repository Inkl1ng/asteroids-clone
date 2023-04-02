import pygame
import sys
from player import Player
from asteroid import Asteroid

def collision(asteroids: list[Asteroid], player: Player) -> bool:
    """
    checks for collision between the player and asteroids
    returns "True" if there is a collision
    returns "False" otherwise
    """
    pass

def main():
    running = True
    screen_width = 800
    screen_height = 800

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height),
            flags=pygame.SRCALPHA)
    pygame.display.set_caption("Asteroids clone")
    clock = pygame.time.Clock()

    player_surface = pygame.Surface((60,60), flags=pygame.SRCALPHA)
    player_surface.fill((0,0,0))
    player_surface.set_colorkey((0,0,0))
    player = Player(player_surface)

    test_surface = pygame.Surface((300,300), flags=pygame.SRCALPHA)

    # keeps track of all the asteroid objects on screen
    asteroids = []

    # main gameloop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        player.update()
        player.draw()

        # used for testing
        # prints out (and in this order):
        #   x velocity, y velocity, x position, y position, angle
        print(f"{player.x_velocity}\t{player.y_velocity}\t{player.x}"
              f"\t{player.y}\t{player.angle}")

        screen.fill((0,0,0,0))
        pygame.draw.rect(test_surface, (255,0,0), (10,10,50,50))
        test_mask = pygame.mask.from_surface(test_surface)
        converted_test_mask = test_mask.to_surface(
                unsetcolor=(0,0,0,0), setcolor=(255,0,0,255)
        )
        screen.blit(converted_test_mask, (200,200))

        converted_player_mask = player.mask.to_surface(
                unsetcolor=(0,0,0,0), setcolor=(255,255,255,255)
        )
        screen.blit(converted_player_mask, [player.x - 30, player.y - 30])
        # screen.blit(player_surface, [player.x - 30, player.y - 30])
        # pygame.draw.rect(screen, (255,0,0), center_of_screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
