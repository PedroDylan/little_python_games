import pygame, sys, random
from pygame.math import Vector2

class BALL:
    def __init__(self):
        self.x =375
        self.y =300

    def draw_ball(self):
        ball_rect = pygame.Rect(self.x,self.y,10,10)
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),10,10)

class PLAYER:
    def __init__(self):
        self.x = 150
        self.y = 300

    def draw_rect(self):
        player_rect = pygame.Rect(self.x-100,self.y-50,25,100)
        pygame.draw.rect(screen,(255,255,255),player_rect)


pygame.init()
screen = pygame.display.set_mode((750,600))
ball = BALL()
player = PLAYER()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    ball.draw_ball()
    player.draw_rect()
    pygame.display.update()

