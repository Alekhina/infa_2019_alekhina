import turtle

w=1 #angular velocity
v=0.5 #speed
t=1 #time
N=10000 #the number of cycles

for t in range(N):
    turtle.forward(v)
    R=v*t
    turtle.left(90+w)
    turtle.forward(R*w/180)
    turtle.right(90)
    