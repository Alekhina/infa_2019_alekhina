import turtle
import math

R=40 #the radius of the big acr
r=10 #the radius of the small acr
n=100 #the "accuracy"
x=4 #the number of the bis arcs
pi=3.1415

def arc(R):
    l=2*R*math.cos(pi*(n-2)/(2*n))
    for i in range(n//2):
        turtle.forward(l)
        turtle.right(360/n)
       
turtle.left(90)  

arc(R)     
for j in range(x-1):
    arc(r)
    arc(R)