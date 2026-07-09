import pygame
from pygame.locals import *
from time import *

pygame.init()
screen=pygame.display.set_mode((600,600))

player_x=200
player_y=200

player=pygame.image.load("character.png")
background=pygame.image.load("background.png")

while player_y<600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    player_y+=2