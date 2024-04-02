from turtle import*
from colorsys import*
bgcolor("black")
title("Asif Shaik")
tracer(10)
pensize(1.5)
h = 0.7
for i in range(180):
    c = hsv_to_rgb(h,1,1)
    h+=0.09
    color(c)
    goto(-8,30)
    down()
    fd(i)
    rt(89)
    circle(20,100)
    lt(179)
    bk(i/2)
    lt(6)
done()
exitonclick()