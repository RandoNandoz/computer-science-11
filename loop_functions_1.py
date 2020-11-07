"""
Randy Zhu
11-06-2020
Draw loops with functions
"""

import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)


def draw_hash_mark() -> None:
    """
    Draw a hash mark.
    """
    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.back(50)
    my_turtle.forward(25)
    my_turtle.right(90)


my_turtle.goto(25, 0)
draw_hash_mark()
my_turtle.goto(50, 0)
draw_hash_mark()
my_turtle.goto(100, 0)
draw_hash_mark()
my_turtle.goto(200, 0)
draw_hash_mark()

turtle.done()
