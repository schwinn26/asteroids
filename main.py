# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot

def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0

    #set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating groups for objects to live in
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group, shots_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group

    Shot.containers = (updatable_group, drawable_group)

    #set player size
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        
        #create the screen and make it black
        screen.fill("black", rect=None, special_flags=0)

        updatable_group.update(dt)

        #draw player on the screen
        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        for asteroid in asteroid_group:
            CircleShape.collisions(asteroid, player)

        player.update(dt)
        player.draw(screen)

        #this limits the game to 60fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
