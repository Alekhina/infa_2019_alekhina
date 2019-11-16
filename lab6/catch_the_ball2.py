from tkinter import *
from random import randrange as rnd, choice
import time


class Ball:
    def __init__(self):
        self.x=rnd(100,700)
        self.y=rnd(100,500)
        self.r=rnd(30,50)
        self.dx=rnd(1,5)
        self.dy=rnd(1,5)
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
   
        
    def check_hit():
        pass
        
    def check_colision():
        pass
        
    def check_click(event):
        pass

def tick():
    for ball in balls:
        ball.move()
    root.after(10,tick)
   
    
def new_ball():
    canv.delete(balls[0])
    balls[0]=balls[1]
    balls[1]=balls[2]
    balls[2]=Ball()
    root.after(1000,new_ball)

def main():
    global root,canv,balls
    root=Tk()
    root.geometry('800x600')

    canv=Canvas(root,bg='white')
    canv.pack(fill=BOTH,expand=1)
    
    balls=[Ball() for i in range (3)]
    
    tick()
    new_ball()
        
    root.mainloop()
    
main()