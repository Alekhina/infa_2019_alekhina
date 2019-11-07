import turtle
l=90 #длина лапы
n=22 #число лапы

for i in range (n):
    turtle.forward(l)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(l)
    turtle.left(180 - 360/n)
    