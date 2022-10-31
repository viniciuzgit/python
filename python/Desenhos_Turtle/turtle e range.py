from turtle import *
color('chartreuse')
tracer(50)
bgcolor('black')
for i in range(100):
    circle(1-185)
    right(91)
for i in range(140):
    tracer(70)
    circle(1 - 185)
    right(91)

for r in range(600):
    penup()
    setpos(0,0)
    pendown()
    tracer(70)
    color('red')
    forward(200)
    right(91)