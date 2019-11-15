from graph import *

a=255
b=255
c=255
x=50
y=50
r=40

obj=circle(4,4,1)


def oblako():
    global a,b,c,x,y
    global o
    deleteObject(o[0])
    deleteObject(o[1])
    deleteObject(o[2])
    deleteObject(o[3])
    deleteObject(o[4])
    penColor(a,b,c)
    brushColor(a,b,c)
    o[0]=circle(x,y,0.7*r)
    o[1]=circle(x+2*r,y,r/2)
    o[2]=circle(x+r,y,0.8*r)
    o[3]=circle(x+1.6*r,y-0.65*r,0.6*r)
    o[4]=circle(x+r/2,y-0.7*r,r/1.4)
    if a>=1:
        a-=1
    if b>=1:        
        b-=1
    if c>=1:    
        c-=1
    x+=3

    
o=[1,2,3,4,5]
onTimer(oblako,50)

def veter(t):
    def upd1():
        moveObjectBy(t,1,0)
    onTimer(upd1,50) 


run()