import pygame
from pygame.locals import *
from time import *

pygame.init()
screen=pygame.display.set_mode((600,600))

player_x=200
player_y=200
keys=[False,False,False,False]

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
    if event.type == pygame.KEYDOWN:
        if event.key==K_UP:
            keys[0]=True
        if event.key==K_DOWN:
            keys[1]=True
        if event.key==K_LEFT:
            keys[2]=True
        if event.key==K_RIGHT:
            keys[3]=True

    
    if event.type == pygame.KEYUP:
        if event.key==K_UP:
            keys[0]=False
        if event.key==K_DOWN:
            keys[1]=False
        if event.key==K_LEFT:
            keys[2]=False
        if event.key==K_RIGHT:
            keys[3]=False

    if keys[0]:#up
        if player_y>0:
            player_y-=7

    elif keys[1]:#down
        if player_y<600:
            player_y+=7

    elif keys[2]:#left
        if player_x>0:
            player_x-=7

    elif keys[3]:#right
        if player_x<600:
            player_x+=7

    sleep(0.05)
    player_y+=5

