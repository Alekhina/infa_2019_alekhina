import turtle
import math

R=40 #the radius of the circles
n=100 #the "accuracy"
x=6 #the number of the circles
pi=3.1415

def circle(R):
    l=2*R*math.cos(pi*(n-2)/(2*n))
    for i in range(n):
        turtle.forward(l)
        turtle.left(360/n)
        
for j in range(x):
    circle(R)
    turtle.left(360/x)