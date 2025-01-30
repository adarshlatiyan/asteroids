# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    dt = 0
    clock = pygame.time.Clock()
    
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(x, y)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill((0, 0, 0))
        
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
            
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
