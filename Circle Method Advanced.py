from turtle import *


tur = Turtle()
tur.up()
tur.right(90)
tur.forward(120)
title("Circle Method: Multi-Coloured Circle ")
tur.down()
tur.left(90)
tur.speed(0.45)
for i in range(10,2,-1):
    tur.begin_fill()
    if i%2 == 0:
        tur.fillcolor("blue")
    else:
        tur.fillcolor("white")
    tur.circle(200,steps = i)
    tur.end_fill()
    tur.hideturtle()
