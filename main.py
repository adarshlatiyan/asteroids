# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from player import Player
from shot import Shot

INCREASE_SCORE_EVENT = 9999


def asteroid_game(
    screen: pygame.Surface, font: pygame.font.Font, clock: pygame.time.Clock
):
    dt = 0

    pygame.time.set_timer(INCREASE_SCORE_EVENT, 5000)

    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == INCREASE_SCORE_EVENT:
                player.increase_score()

        screen.fill((0, 0, 0))
        show_score(screen, font, player.score)

        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    is_destroyed = asteroid.on_shot()
                    if is_destroyed:
                        player.increase_score()
                    shot.kill()

            if player.check_collision(asteroid):
                print("Game Over!")
                # return

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def show_score(screen: pygame.Surface, font: pygame.font.Font, score: int):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (constants.SCREEN_WIDTH - text.get_width() - 10, 10))


def main():
    pygame.init()

    font: pygame.Font = pygame.font.SysFont("Arial", 24)
    screen: pygame.font.Font = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
    clock = pygame.time.Clock()

    asteroid_game(screen=screen, font=font, clock=clock)


if __name__ == "__main__":
    main()
