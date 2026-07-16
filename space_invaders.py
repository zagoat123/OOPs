import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH=1000
HEIGHT=500

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space_invaders")

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
FPS=60
VEL=5
Bullet_vel=7
Maxbullets=3
spaceship_width,spaceship_height=55,40
HEALTH_FONT=pygame.font.SysFont("comicsans",40)
WINNER_FONT=pygame.font.SysFont("comicsans",100)


background=pygame.image.load(os.path.join("assets","background.png"))
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","yellow.jpeg"))
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","red.jpeg"))

YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(spaceship_width,spaceship_height)),90)

RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(spaceship_width,spaceship_height)),-90)

def main():


    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #if it is quit the pygame
                pygame.quit()
            exit()

if __name__=="__main__":
    main()


   
