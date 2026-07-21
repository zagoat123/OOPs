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

def yellow_handle_movment(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]and yellow.x-VEL>0: #left
        yellow.x-=VEL

    if keys_pressed[pygame.K_s]and yellow.y+VEL+yellow.height<HEIGHT-15: #down
        yellow.y+=VEL
    
    if keys_pressed[pygame.K_d]and yellow.x+VEL+yellow.width<BORDER.x: #right
        yellow.x+=VEL

    if keys_pressed[pygame.K_w]and yellow.y-VEL>0: #up
        yellow.y-=VEL


def red_handle_movment(keys_pressed,red):
    if keys_pressed[pygame.K_a]and red.x-VEL>0: #left
        red.x-=VEL

    if keys_pressed[pygame.K_s]and red.y+VEL+red.height<HEIGHT-15: #down
        red.y-=VEL
    
    if keys_pressed[pygame.K_d]and red.x+VEL+red.width<BORDER.x: #right
        red.x+=VEL

    if keys_pressed[pygame.K_w]and red.y-VEL>0: #up
        red.y+=VEL

def draw_window(yellow,red):
    WIN.blit(background,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(100,200))
    WIN.blit(RED_SPACESHIP,(800,200))
    pygame.display.update()



def main():
    yellow=pygame.Rect(100,200,spaceship_width,spaceship_height)
    red=pygame.Rect(800,200,spaceship_width,spaceship_height)
    clock=pygame.time.Clock()


    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #if it is quit the pygame
                run=False
        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movment(keys_pressed,yellow)
        red_handle_movment(keys_pressed,red)
        
        draw_window(yellow,red)
    pygame.quit()

if __name__=="__main__":
    main()


   
