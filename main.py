import pygame
from constants import *  # noqa: F403
from player import * # noqa: F403
from asteroid import * # noqa: F403
from asteroidfield import * # noqa: F403


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # noqa: F405
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # noqa: F405
    print(f"Screen height: {SCREEN_HEIGHT}") # noqa: F405

    updateable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # noqa: F405

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player.update(dt)
        for obj in updateable:
            obj.update(dt)
        
        screen.fill("black")
        # player.draw(screen) 
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
