import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.speed(200)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)
    if i == 80:
        break
def draw_text(text, size, color):
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.color(color)
    t.write(text, align="center", font=("Arial", size, "bold"))
draw_text("By Asif Shaik", 40, "white")
t.hideturtle()
turtle.done()
turtle.exitonclick()