import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    game_dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field1 = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(game_dt)
        
        for rock in asteroids:
            if rock.collides_with(player1):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if rock.collides_with(bullet):
                    log_event("asteroid_shot")
                    rock.split()
                    bullet.kill()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        game_dt = (game_clock.tick(60) / 1000)
        

if __name__ == "__main__":
    main()
