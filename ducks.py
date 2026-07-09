import pygame
from pygame.locals import *
from time import *

pygame.init()
screen=pygame.display.set_mode((600,400))

player_x=200
player_y=200

player=pygame.image.load("duck.png")
background=pygame.image.load("sea.jpeg")

while player_x>600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
   