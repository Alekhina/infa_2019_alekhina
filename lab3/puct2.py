from graph import *
from math import sin

a=1
c=0

def linia(x):
    global a,c
    return(20*sin(x/20+c)+200)

def risyet():
    global a,c
    moveTo(0,linia(0))    
    for i in range(500):
        lineTo(i,linia(i)

 
onTimer(risyet,50)
    
run()