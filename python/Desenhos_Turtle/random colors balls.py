from turtle import *
from random import randint
from random import random

while True:
    speed(20)
    up()
    goto(randint(-400,400),
         randint(-400,400))
    down()
    R = random()
    B = random()
    G = random()
    color(R,G,B)
    dot(randint(20,80))




