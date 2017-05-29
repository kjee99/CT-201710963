import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
width=wn.window_width()
w3=width/3
x1=0.0-w3
x2=0.0
x3=0.0+w3
def triangle(size) :
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
def drawTriangleAt(size,at) :
    t1.penup()
    t1.goto(at,0)
    t1.pendown()
    t1.setheading(0)
    triangle(size)
def pentagon(size) :
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
def drawPentagonAt(size,at) :
    t1.penup()
    t1.goto(at,0)
    t1.pendown()
    t1.setheading(0)
    pentagon(size)
def star(size) :
    t1.fd(size)
    t1.rt(150)
    t1.fd(size)
    t1.rt(150)
    t1.fd(size)
    t1.rt(150)
    t1.fd(size)
    t1.rt(135)
    t1.fd(size)
def drawStarAt(size,at) :
    t1.penup()
    t1.goto(at,0)
    t1.pendown()
    t1.setheading(0)
    star(size)
drawTriangleAt(100,x1)
drawPentagonAt(100,x2)
drawStarAt(100,x3)
wn.exitonclick()