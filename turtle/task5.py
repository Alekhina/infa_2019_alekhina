import turtle

k=5 #кол-во квадратов
n=4     #сколькоугольник
l=20   #длина 1 стороны
t=5 #отступ


for i in range(k):
    for j in range (n):
        turtle.pendown()
        turtle.forward(l)
        turtle.left(180-180*(n-2)/n)
    turtle.penup()
    turtle.right(90)
    turtle.forward(t)
    turtle.right(90)
    turtle.forward(t)
    turtle.left(180)
    l += 2*t