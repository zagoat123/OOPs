import pygame
pygame.init()

WIDTH=600
HEIGHT=600

BLACK=(0,0,0)
RED=(255,0,0)

FPS=60


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ultimate growing Square")
clock=pygame.time.Clock()

class Square:
    def __init__(self,pos,side,color):
        self.pos=pos
        self.side=side
        self.color=color
        self.growing=False

    def update(self):
        if self.growing:
            self.side+=1

    def draw(self,surface):
        rect=pygame.Rect(
            self.pos[0]-self.side//2,
            self.pos[1]-self.side//2,
            self.side,
            self.side
        )
        pygame.draw.rect(surface,self.color,rect)
    
square=Square((300,300),20,RED)
running=True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            square.growing=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            square.growing=False

    square.update()
    square.draw(screen)
    pygame.display.flip()
pygame.quit()
