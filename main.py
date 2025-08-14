import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    dt = 0
    Player.containers = (updatable, drawable)
    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)/1000
        
        updatable.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
