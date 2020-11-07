"""
Randy Zhu
11-06-2020
Draw squares
"""
import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)


def draw_square(edge_length: int):
    """
    Draw a squares with given coords, and edge length.
    """
    for _ in range(4):
        my_turtle.pendown()
        my_turtle.left(90)
        my_turtle.forward(edge_length)
        my_turtle.penup()


for index in range(0, 51, 10):
    my_turtle.forward(index * 2)
    draw_square(index)

turtle.done()
