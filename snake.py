import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        #creating a copy of every element of the body 
        #except for the last one
        body_copy = self.body[:-1]
        #inserting the head in the new body
        body_copy.insert(0,body_copy[0]+self.direction)
        #inserting the copy onto the actual drawn body
        self.body = body_copy





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
snake = SNAKE()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


#game loop that closes when the user closes it
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                snake.move_snake()

            


    #filling the surfaces with color
        screen.fill((175,250,70))
        fruit.draw_fruit()
        snake.draw_snake()
        pygame.display.update()
        clock.tick(60)
