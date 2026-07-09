import pgzrun

WIDTH=800
HEIGHT=800
TITLE="Crazy Ball"


class ball:

    def __init__(self,x,y,color,size):
        self.x=x
        self.y=y
        self.color=color
        self.size=size
        


    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.size,self.color)



b1=ball(50,50,"blue",30)
b2=ball(150,150,"green",45)
b3=ball(250,250,"red",60)

def draw():
    screen.clear()
    b1.draw()
    b2.draw()
    b3.draw()

vx=5
vy=5

vx1=3
vy1=3

vx2=7
vy2=7



def update():
    global vx,vy,vx1,vy1,vx2,vy2
    b1.x+=vx
    b2.x+=vx1
    b3.x+=vx2
    b1.y+=vy
    b2.y+=vy1
    b3.y+=vy2
    if b1.x<=0 or b1.x>=WIDTH:
        vx=vx*-1
    if b1.y<=0 or b1.y>=HEIGHT:
        vy=vy*-1
    
    if b2.x<=0 or b2.x>=WIDTH:
        vx1=vx1*-1
    if b2.y<=0 or b2.y>=HEIGHT:
        vy1=vy1*-1

    if b3.x<=0 or b3.x>=WIDTH:
        vx2=vx2*-1
    if b3.y<=0 or b3.y>=HEIGHT:
        vy2=vy2*-1










pgzrun.go()