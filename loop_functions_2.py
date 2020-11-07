"""
Randy Zhu
11-06-2020
Draw a dart board
"""
import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)


def make_circle_with_radius(x_axis: int, y_axis: int, radius: int):
    """
    Draw a circle with a given axes, and radius.
    """
    my_turtle.penup()
    my_turtle.goto(x_axis, y_axis)
    my_turtle.pendown()
    my_turtle.circle(radius)
    my_turtle.penup()
    my_turtle.goto(x_axis, y_axis)


for index in range(30, 121, 30):
    make_circle_with_radius(0, -index, index)

turtle.done()
