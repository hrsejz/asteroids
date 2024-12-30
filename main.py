# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *  # noqa: F403
from player import * # noqa: F403


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # noqa: F405
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)


    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen) 
        pygame.display.flip()
        
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
