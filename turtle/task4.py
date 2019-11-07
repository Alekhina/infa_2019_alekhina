import turtle

n=100
l=5
for i in range(n):
    turtle.forward(l)
    turtle.left(180-180*(n-2)/n)
