import turtle
import math

N=10000 #the number of the cycles
n=100 #the number of the angles of my polygon
t=1 #time
R=0.05 #the radius
delta_R=0.005 #radius increment
pi=3.14 

for t in range(N):
    turtle.forward(2*R*math.cos(pi/n))
    turtle.left(360/n)
    turtle.left(360/n)
    R+=delta_R
    t+=1