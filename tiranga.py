from turtle import*
windo = Screen()
windo.bgcolor("white")
tiranga = Turtle()
tiranga.width(2)
#tiranga.pencolor("green")
tiranga.speed(0)
#tiranga.shape("turtle")
tiranga.setheading(270)
#tiranga.circle(90)
x, y, z, t, p = 1, 1, 1, 1, 1
tiranga.pencolor("orange")
tiranga.begin_fill()
tiranga.fillcolor("orange")
tiranga.circle(-420)
tiranga.end_fill()
tiranga.pencolor("green")
tiranga.begin_fill()
tiranga.fillcolor("green")
tiranga.circle(420)
tiranga.end_fill()
while(p<40):
    tiranga.begin_fill()
    tiranga.fillcolor("blue")
    tiranga.color("blue")
    tiranga.setheading(180+y)
    tiranga.circle(120)
    p = p+1
    y= y+50
    tiranga.end_fill()
while (t<40):
    tiranga.begin_fill()
    tiranga.fillcolor("orange")
    tiranga.color("orange")
    tiranga.setheading(180+y)
    tiranga.circle(120)
    t=t+1
    y=y+50
while (z<40):
    tiranga.color("white")
    tiranga.setheading(180+y)
    tiranga.circle(100)
    z=z+1
    y=y+50
while(x<40):
    tiranga.color("green")
    tiranga.setheading(180+y)
    tiranga.circle(80)
    x=x+1
    y=y+50
    tiranga.hideturtle()
    tiranga.up()
    tiranga.goto(0, -300)
    tiranga.down()
    tiranga.color('blue')
    tiranga.write("15 Aug",False, align='center',font=('monospace corciva', 30, 'bold'))
    tiranga.seth(0)
    tiranga.forward(120)
    tiranga.seth(90)
    tiranga.forward(40)
    tiranga.seth(180)
    tiranga.forward(260)
    tiranga.seth(270)
    tiranga.forward(40)
    tiiranga.seth(0)
    tiranga.forward(120)
    windo.exitonclick()
