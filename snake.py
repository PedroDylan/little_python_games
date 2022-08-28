import pygame, sys 

pygame.init()
screen = pygame.display.set_mode((400,500))

#defining a clock to control the FPS
#in order to the game run equally in every machine
clock = pygame.time.Clock()

#creating a surface in the background
test_surface = pygame.Surface((100,200))

#game loop that closes when the user closes it
while True:
    for event in pygame.event.get():
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    test_surface.fill((50,50,250))
    screen.fill((175,250,70))

    screen.blit(test_surface,(200,250))
    pygame.display.update()
    clock.tick(60)
