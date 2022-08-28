import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))

#defining a clock to control the FPS
#in order to the game run equally in every machine
clock = pygame.time.Clock()

fruit = FRUIT()


#game loop that closes when the user closes it
while True:
    for event in pygame.event.get():
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


#filling the surfaces with color
    
    screen.fill((175,250,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
