from graph import *
from math import sin,cos

pi=3.1415

def linia(x):
    return(x+20*sin(-0.05*x)+30*sin(-0.03*x)+10*sin(-0.1*x)+24*sin(-0.02*x))

def domik(x,y,s):
#x,y - нижняя левая точка крыши
    brushColor(240, 247, 158)
    rectangle(x,y,x+1.618*s,y+s)
    brushColor(196,24,44)
    polygon([(x,y),(x+0.809*s,y-s/3),(x+1.618*s,y)])
    brushColor(158, 219, 247)
    rectangle(x+1.618*s/3,y+s/3,x+1.1618*s,y+2*s/3)
    
def drevo(x,y,h):
#x,y - нижняя левая точка
    brushColor(61,44,10)
    rectangle(x,y,x+h/10,y-h)
    brushColor(46,92,8)
    penColor(46,92,8)
    circle(x-h/10,y-h/1.5,h/5)
    circle(x+h/8,y-h/1.6,h/4)
    circle(x+h/20,y-h,h/3.5)
    circle(x+h/6,y-h/0.8,h/7)
    circle(x+h/7,y-h/0.9,h/6.5)
    circle(x+h/10,y-h/1.5,h/5)
    circle(x-h/8,y-h,h/5)
    penColor(0,0,0)
    
def oblako(x,y,r):
    penColor(255,255,255)
    brushColor(255,255,255)
    circle(x,y,0.7*r)
    circle(x+2*r,y,r/2)
    circle(x+r,y,0.8*r)
    circle(x+1.6*r,y-0.65*r,0.6*r)
    circle(x+r/2,y-0.7*r,r/1.4)
    penColor(0,0,0)
    
def zmey(x,y,h):
#x,y - точка крепления ниточки к змею
    a=abs(0.8*h)
    b=abs(h/5)
    if h>0:
        polygon([(x,y),(x+a,y-b),(x+a+b,y-a-b),(x+b,y-a)])
    else:
        polygon([(x,y),(x-a,y-b),(x-a+b,y-a-b),(x+b,y-a)])
    
    moveTo(x,y)
    delta=y-linia(x)
    for i in range(x, x+200):
        lineTo(i, linia(i)+delta)           
    
    
def sun(x,y,r,n):
#x,y - центр солнца, n - лучики
    A=[]
    for i in range (n):
        B=(r*cos(2*pi*i/n)+x, r*sin(2*pi*i/n)+y)
        A.append(B)
        C=(2*r*cos(2*pi*i/n+pi/n)+x, 2*r*sin(2*pi*i/n+pi/n)+y)
        A.append(C)
        i+=2
    brushColor(247,251,54)
    polygon(A)
    

#рисую фон    
brushColor(100,168,66)
rectangle(0,350,500,600)
brushColor(158, 219, 247)
rectangle(0,0,500,350)

#рисую объекты
domik(130,320,110)
domik(320, 300, 60)
drevo(110,490,110)
drevo(450,380,90)
drevo(50,520,140)
oblako(100,150,40)
oblako(250,100,50)
oblako(30,70,30)
sun(420,90,30,12)
brushColor(255,173,9)
zmey(280,100,60)
brushColor(252,71,231)
zmey(180,170,-70)

run()