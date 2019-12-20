from tkinter import *
from random import randrange as rnd, choice
import time
from math import sqrt

k=0

class Target:
    def __init__(self):
        self.x=rnd(50,750)
        self.y=rnd(50,550)
        self.r=rnd(10,25)
        self.target_id=canv.create_oval(self.x-self.r,self.y-self.r,
                                 self.x+self.r,self.y+self.r,
                                 fill='black',activefill='grey')

class Ball:
    def __init__(self):
        global k
        k+=1
        if k%3==0:
            self.x=rnd(100,300)
            self.y=rnd(100,200)
        if k%3==1:
            self.x=rnd(400,700)
            self.y=rnd(300,500)
        if k%3==2:
            self.x=rnd(100,300)
            self.y=rnd(300,500)
        
        self.r=rnd(30,50)
        self.dx=rnd(3,6)
        self.dy=rnd(3,6)
        self.color=choice(['red','orange','yellow','green','blue'])
        self.ball_id=canv.create_oval(self.x-self.r,self.y-self.r,
                                 self.x+self.r,self.y+self.r,
                                 fill=self.color,width=0)
    
    def show(self):
        canv.delete(self.ball_id)
        self.ball_id=create_oval(self.x-self.r,self.y-self.r,
                                 self.x+self.r,self.y+self.r,
                                 fill=self.color,width=0)
    
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
        if self.x+self.r>=800 or self.x-self.r<=0:
           self.dx*=-1
        if self.y+self.r>=600 or self.y-self.r<=0:
           self.dy*=-1
        canv.delete(self.ball_id)
        self.ball_id=canv.create_oval(self.x-self.r,self.y-self.r,
                                 self.x+self.r,self.y+self.r,
                                 fill=self.color,width=0) 
                                 
        #def change_ball_color():
            #self.color='white'
            
        #root.after(1000,change_ball_color)                            
     
    #def show(self):
        #canv.move(self.ball_id, self.dx, self.dy)
     
    #def check_hit():
        #pass
        
    #def check_colision():
        #pass
        
    #def check_click(event):
        #pass

def tick():
    for ball in balls:
        ball.move()
        #ball.show()
    root.after(10,tick)
   
 
def new_ball():
    canv.delete(ALL)
    balls[0]=balls[1]
    balls[1]=balls[2]
    balls[2]=Ball()
    targ=Target()
    
    root.after(1000,new_ball)
    
def check_colision():
    a=[None,None,None]
    b=[None,None,None]
    c=[None,None,None]  
    
    for i in range (3):
        a[i%3]=(balls[(i+1)%3].x-balls[(i+2)%3].x)
    for i in range (3):
        b[i%3]=(balls[(i+1)%3].y-balls[(i+2)%3].y)
    for i in range (3):
        c[i%3]=(balls[(i+1)%3].r+balls[(i+2)%3].r)    
        
    for i in  range(3):
        if a[i]**2+b[i]**2<=c[i]**2:
            balls[(i+1)%3].dx*=-1
            balls[(i+1)%3].dy*=-1
            balls[(i+2)%3].dx*=-1
            balls[(i+2)%3].dy*=-1

            
    root.after(10,check_colision)

def click(event):
    global score
    for j in range(3):
        if (event.x-balls[j].x)**2+(event.y-balls[j].y)**2 <= balls[j].r**2:
            score+=1
            print('Score: ', score)
    if (event.x-targ.x)**2+(event.y-targ.y)**2 <= targ.r**2:
        score+=3
        print('Score: ', score)
    


def main():
    global root,canv,balls,score,targ
    root=Tk()
    root.geometry('800x600')

    canv=Canvas(root,bg='white')
    canv.pack(fill=BOTH,expand=1)
    
    balls=[Ball() for i in range (3)]
    targ=Target()
    
    score=0
    tick()
    new_ball()
    check_colision()
    canv.bind('<Button-1>', click)
        
    root.mainloop()
    
main()
