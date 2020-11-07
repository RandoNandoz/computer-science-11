"""
Randy Zhu
11-04-2020
Draw black & red checkerboard /w/ turtles.
"""

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

# def square(hex_color: str, radius: int):
#     """
#     Draw a square.
#     """
#     my_turtle.pendown()
#     my_turtle.color(hex_color)
#     my_turtle.begin_fill()
#     for _ in range(4):
#         my_turtle.right(90)
#         my_turtle.forward(radius)
#     my_turtle.end_fill()

# Do this ten times.
for row in range(10):
    # If it's an even row, set the initial number to even.
    if row % 2:
        init = 0
    # If it's an odd row, set the initial number to odd.
    else:
        init = 1
    # Do this ten times again.
    for col in range(10):
        # If the initial number is even, draw a red square
        if init % 2 == 0:
            my_turtle.pendown()
            my_turtle.color("#FF0000")
            my_turtle.begin_fill()
            for _ in range(4):
                my_turtle.right(90)
                my_turtle.forward(10)
            my_turtle.end_fill()
        # If the initial number is odd, draw a black square
        else:
            my_turtle.pendown()
            my_turtle.color("#000000")
            my_turtle.begin_fill()
            for _ in range(4):
                my_turtle.right(90)
                my_turtle.forward(10)
            my_turtle.end_fill()
        # increment one to the squares drawn
        init += 1
        my_turtle.penup()
        my_turtle.forward(10)

    my_turtle.goto(-10, 10 * (row + 1))
    my_turtle.forward(10)

turtle.done()
