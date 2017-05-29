import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
width=wn.window_width()
w3=width/3
x1=0.0-w3
x2=0.0
x3=0.0+w3
def drawSquare(size) :
    for i in range(1,5) :
        t1.fd(size)
        t1.rt(90)
drawSquare(100)
t1.clear()
def triangle(size) :
    for i in range(1,4) :
        t1.fd(size)
        t1.lt(120)
def pentagon(size) :
    for i in range(1,6) :
        t1.fd(size)
        t1.lt(72)
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
def drawTriangleAt(x,y,size) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.setheading(0)
    triangle(size)
def drawPentagonAt(x,y,size) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.setheading(0)
    pentagon(size)
def drawStarAt(x,y,size) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.setheading(0)
    star(size)
drawTriangleAt(x1,0,100)
drawPentagonAt(x2,0,100)
drawStarAt(x3,0,100)
wn.exitonclick()