from curses import KEY_DOWN
import pygame, sys, random
from pygame.math import Vector2

class BALL:
    def __init__(self):
        self.x =375
        self.y =300
        self.speed = 5
        self.direction = Vector2(-1,0)

    def draw_ball(self):
        ball_rect = pygame.Rect(self.x,self.y,10,10)
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),10,10)

    def move_ball(self):
        self.x += self.direction.x*self.speed

class OPPONENT:
    def __init__(self):
        self.x = 600
        self.y = 300
        self.speed = 0
        self.direction = Vector2(0,-1)
    
    def draw_rect(self):
        op_rect = pygame.Rect(self.x+75,self.y-50,25,100)
        pygame.draw.rect(screen,(255,255,255),op_rect)

class PLAYER:
    def __init__(self):
        self.x = 150
        self.y = 300
        self.speed = 0
        self.direction = Vector2(0,-1)

    def draw_rect(self):
        player_rect = pygame.Rect(self.x-100,self.y-50,25,100)
        pygame.draw.rect(screen,(255,255,255),player_rect)

    #def move_player(self):
    #    self.y += self.speed*self.direction.y

class MAIN:
    def __init__(self):
        self.player = PLAYER()
        self.ball = BALL()
        self.oponnent = OPPONENT()

    def update(self):
        self.ball.move_ball()
        #self.player.move_player()
        #self.check_collision()
        #self.check_fail()

    def draw_elements(self):
        self.ball.draw_ball()
        self.player.draw_rect()
        self.oponnent.draw_rect()

        



pygame.init()
screen = pygame.display.set_mode((750,600))

clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,30)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.player.direction.y = -1
                main_game.player.speed = 7
                #main_game.player.move_player()
            if event.key == pygame.K_DOWN:
                main_game.player.direction.y = 1
                main_game.player.speed = 7
                #main_game.player.move_player()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                main_game.player.direction.y = -1
                main_game.player.speed = 0
                #main_game.player.move_player()
            if event.key == pygame.K_DOWN:
                main_game.player.direction.y = 1
                main_game.player.speed = 0
                #main_game.player.move_player()
        
        




    screen.fill((0,0,0))
    main_game.draw_elements()
    main_game.player.y += main_game.player.speed*main_game.player.direction.y
    pygame.display.update()
    clock.tick(60)

