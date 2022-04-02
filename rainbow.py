from turtle import *

speed(0.5)
pu()
fd(300)
pd()


def right():
 rt(90)
 fd(15)
 rt(90)


def left():
 lt(90)
 back(15)
 fd(15)
 lt(90)
 

fillcolor("#9400D3")
begin_fill()
lt(90) 
circle(300, 180)
lt(180)
end_fill()
circle(-300, 180)
fillcolor("#4B0082")
begin_fill()
right()
circle(285, 180)
left()
end_fill()
circle(-285, 180)
fillcolor("#0000FF")
begin_fill()
right()
circle(270, 180)
left()
end_fill()
circle(-270, 180)
fillcolor("#00FF00")
begin_fill()
right()
circle(255, 180)
left()
end_fill()
circle(-255, 180)
fillcolor("#FFFF00")
begin_fill()
right()
circle(240, 180)
left()
end_fill()
circle(-240, 180)
fillcolor("#FF7F00")
begin_fill()
right()
circle(225, 180)
left()
end_fill()
circle(-225, 180)
fillcolor("#FF0000")
begin_fill()
right()
circle(210, 180)
left()
end_fill()
circle(-210, 180)
fillcolor("white")
begin_fill()
right()
circle(195, 180)
left()
end_fill()
circle(-195, 180)








done()
