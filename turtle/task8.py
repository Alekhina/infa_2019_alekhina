import turtle

a=5 #lenght of side of my square
delta_a=3 #side increment
N=50 #the number of of the cycles

for i in range (N):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    a+=delta_a