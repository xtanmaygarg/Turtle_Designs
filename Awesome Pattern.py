from turtle import *

tur = Turtle()
list1 = ["purple","red","blue","green"]
tur.speed(0)
for i in range(300):
    tur.color(list1[i%4])
    tur.pensize(i/10 + 1)
    tur.forward(i)
    tur.left(42)
