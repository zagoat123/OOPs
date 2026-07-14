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

background=pygame.image.load(os.path.join("Assets","background.png"))
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
for event in pygame.event.get():
    if event.type==pygame.QUIT:
        #if it is quit the pygame
        pygame.quit()
    exit()


print=("yooo this is dev")