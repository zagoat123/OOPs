import pygame
import time 

pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday card!!!")

CYAN=(0, 255, 255)
RED=(255, 0, 0)
font=pygame.font.SysFont("Arial",50)
screen.fill(CYAN)
pygame.display.update()

running=True
shown=False
shown2=False
shown3=False
shown4=False
shown5=False
shown6=False
start_time=time.time()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    if not shown and time.time()-start_time>=2:
        screen.fill(CYAN)
        text=font.render("Happy Birthday MOM!",True,RED)
        text_rect=text.get_rect(center=(300,300))

        screen.blit(text,text_rect)
        pygame.display.update()
        shown=True

    if shown and not shown2 and time.time()-start_time>=4:
        screen.fill(CYAN)
        text=font.render("Hope you have the ",True,RED)
        text_rect=text.get_rect(center=(300,250))
        text2=font.render("best birthday ever!!!",True,RED)
        text2_rect=text.get_rect(center=(300,350))

        screen.blit(text,text_rect)
        screen.blit(text2,text2_rect)
        pygame.display.update()
        shown2=True

    if shown and not shown3 and time.time()-start_time>=6:
        screen.fill(CYAN)
        text=font.render("I hope you had a ",True,RED)
        text_rect=text.get_rect(center=(300,250))
        text3=font.render("amazing year so far!!",True,RED)
        text3_rect=text.get_rect(center=(300,350))

        screen.blit(text,text_rect)
        screen.blit(text3,text3_rect)
        pygame.display.update()
        shown3=True

    if not shown4 and time.time()-start_time>=8:
        screen.fill(CYAN)
        text=font.render("Love you tooo much!!",True,RED)
        text_rect=text.get_rect(center=(300,300))

        screen.blit(text,text_rect)
        pygame.display.update()
        shown4=True

    
    
    if not shown5 and time.time()-start_time>=10:
        screen.fill(CYAN)
        text=font.render("Hope you like my card!!",True,RED)
        text_rect=text.get_rect(center=(300,300))

        screen.blit(text,text_rect)
        pygame.display.update()
        shown5=True

    if not shown6 and time.time()-start_time>=12:
        screen.fill(CYAN)
        text=font.render("Love Dev!!",True,RED)
        text_rect=text.get_rect(center=(300,300))

        screen.blit(text,text_rect)
        pygame.display.update()
        shown6=True





            
pygame.quit()