from graph import *
from math import sin,cos

pi=3.1415
aa=255
bb=255
cc=255
xx=-30
yy=70
rr=40


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
    
def oblako():
#массив из кругов
#меняет переменные цвета и координат, удаляет старые круги, рисует новые
    global aa,bb,cc,xx,yy
    global o
    for j in range(10):
        deleteObject(o[j])
    penColor(aa,bb,cc)
    brushColor(aa,bb,cc)
    o[0]=circle(xx,yy,0.7*rr)
    o[1]=circle(xx+2*rr,yy,rr/2)
    o[2]=circle(xx+rr,yy,0.8*rr)
    o[3]=circle(xx+1.6*rr,yy-0.65*rr,0.6*rr)
    o[4]=circle(xx+rr/2,yy-0.7*rr,rr/1.4)
    o[5]=circle(xx+50,yy+90,1.2*0.7*rr)
    o[6]=circle(xx+2*rr+50,yy+90,1.2*rr/2)
    o[7]=circle(xx+rr+50,yy+90,1.2*0.8*rr)
    o[8]=circle(xx+1.6*rr+50,yy-0.65*rr+90,1.2*0.6*rr)
    o[9]=circle(xx+rr/2+50,yy-0.7*rr+90,1.2*rr/1.4)
    if aa>=1:
        aa-=1
    if bb>=1:        
        bb-=1
    if cc>=1:    
        cc-=1
    xx+=3


    
    
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
sun(420,90,30,12)
brushColor(255,173,9)
zmey(280,100,60)
brushColor(252,71,231)
zmey(180,170,-70)

o=[0,1,2,3,4,5,6,7,8,9]
for k in range(10):
    o[k]=circle(1,1,1)

onTimer(oblako,50) 

run()