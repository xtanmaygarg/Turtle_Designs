from turtle import *

tur = Turtle()
title("Turtle: GOTO Method")
def drawcirle(x,y,color):
    tur.up()
    tur.goto(x,y)
    tur.down()
    tur.begin_fill()
    tur.fillcolor(color)
    tur.circle(50)
    tur.end_fill()
drawcirle(0,0,"green")
drawcirle(200,200,"orange")
drawcirle(-200,200,"blue")
drawcirle(-200,-200,"red")
drawcirle(200,-200,"yellow")

