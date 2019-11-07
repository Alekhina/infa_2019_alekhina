import turtle
import math

R=50 #THE RADIUS OF THE TRIANGLE
delta_R=30 #THE INCREMENT IF THE RADIUS
x=10 #THE NUMBER OF THE POLYGONS
pi=3.1415

def polygon(n):
    for i in range (n):
        l=2*R*(math.cos(pi*(n-2)/(2*n)))
        turtle.forward(l)
        turtle.left(360/n)

for j in range (x):
    n=j+3
    turtle.left(90*(n+2)/n)
    polygon(n)
    turtle.right(90*(n+2)/n)
    turtle.penup()
    turtle.forward(delta_R)
    turtle.pendown()
    R+=delta_R