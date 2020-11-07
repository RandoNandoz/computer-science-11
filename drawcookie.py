# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:47:46 2020

@author: 1257035
"""

import turtle
from random import randint
anna = turtle.Turtle()
anna.speed(0)


def draw_cookie(x: int, y: int) -> None:
    """
    Draw a cookie.
    """
    # Draw cookie outside
    anna.penup()
    anna.goto(-5 + x, -30 + y)
    anna.pendown()
    anna.circle(30)
    anna.penup()

    # Chocolate chip in the middle.
    anna.goto(0 + x, 0 + y)
    anna.stamp()

    # Chocolate chip bottom left.
    anna.goto(-10 + x, -10 + y)
    anna.stamp()

    # Chocolate chip top left.
    anna.goto(-10 + x, 10 + y)
    anna.stamp()

    # Chocolate chip top right.
    anna.goto(10 + x, -10 + y)
    anna.stamp()

    anna.goto(10 + x, 10 + y)
    anna.stamp()


while True:
    draw_cookie(randint(-500, 500), randint(-500, 500))

for index in range(0, 500, 100):
    draw_cookie(index, 0)

turtle.done()
