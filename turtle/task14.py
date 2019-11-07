import turtle
import math

l=70 #the lenght of the side of the stars
n1=5
n2=11
x1=50
y1=50
x2=-50
y2=-50

def star(n,l):
    for i in range(n):
        turtle.forward(l)
        turtle.left(180*(n-1)/n)
        
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
star(n1,l)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
star(n2,l)