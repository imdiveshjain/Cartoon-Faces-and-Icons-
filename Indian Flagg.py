# Indian Flag Code

import turtle
from turtle import *

screen = turtle.Screen()

t = turtle.Turtle()
t.speed(11)
turtle.bgcolor("white")
t.penup()
t.goto(-400,250)
t.pendown()

t.color("orange")
t.begin_fill()
t.fd(800)
t.rt(90)
t.fd(167)
t.rt(90)
t.fd(800)
t.end_fill()
t.lt(90)
t.fd(167)

t.color("green")
t.begin_fill()
t.fd(167)
t.lt(90)
t.fd(800)
t.lt(90)
t.fd(167)
t.end_fill()

t.penup()
t.goto(70,0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(60,0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

t.penup()
t.goto(-57,-8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.pu()
    t.fd(15)
    t.rt(15)
    t.pd()

t.pu()
t.goto(20,0)
t.pd()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)

for i in range(24):
    t.fd(60)
    t.backward(60)
    t.rt(15)

turtle.done()
