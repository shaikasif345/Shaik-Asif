import turtle as r
r.bgcolor("black")
r.pencolor("aqua")
r.title("Asif Shaik")
r.speed(20)
r.width(3)

def form(x):
    r.circle(100,x)
    r.penup()
    r.goto(0,0)
    r.pendown()
    r.circle(-100,x)

def leaf():
    for i in range(0,140,5):
        form(i)
leaf()
r.setheading(90)
leaf()
r.setheading(180)
leaf()
r.setheading(270)
leaf()
r.setheading(360)
r.exitonclick()
r.done