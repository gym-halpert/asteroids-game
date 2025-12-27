import pygame
from player import Player
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width: 1280")
    print("Screen height: 720")

    while True:
        log_state()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
