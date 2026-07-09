import pygame
pygame.init()

WIDTH=600
HEIGHT=600

WHITE=(255,255,255)
LIGHTBLUE=(173, 216, 230)

FPS=1000


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ultimate growing Circle")
clock=pygame.time.Clock()

class Circle:
    def __init__(self,pos,radius,color):
        self.pos=pos
        self.radius=radius
        self.color=color
        self.growing=False

    def update(self):
        if self.growing:
            self.radius+=1

    def draw(self,surface):
        pygame.draw.circle(
            surface,
            self.color,
            self.pos,
            int(self.radius)
        )
circle=Circle((300,300),20,LIGHTBLUE)
running=True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            circle.growing=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            circle.growing=False

    circle.update()
    circle.draw(screen)
    pygame.display.flip()
pygame.quit()
