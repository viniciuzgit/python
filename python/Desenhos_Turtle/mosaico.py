import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate = int(180)


def Circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 3


def dc(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


dc(s, 200, 10)

t1 = turtle.Turtle()
t1.speed(0)
t1.color('white')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def dc(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


dc(t1, 160, 10)

t2 = turtle.Turtle()
t2.speed(0)
t2.color('white')
rotate = int(80)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def dc(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


dc(t2, 120, 10)

t3 = turtle.Turtle()
t3.speed(0)
t3.color('white')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def dc(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


dc(t3, 80, 10)

t4 = turtle.Turtle()
t4.speed(0)
t4.color('white')
rotate = int(90)


def circulos(t, size):
    for i in range(4):
        t.circles(size)
        size = size - 20


def dc(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


dc(t4, 40, 10)




