"""
Randy Zhu
2020-10-28
Draw Cookies
"""

import turtle

# CONSTANT to define how much to shift each cookie.
SHIFT = 100

# Create turtle instance.
my_turtle = turtle.Turtle()

# Do it for times.
for i in range(4):
    # Draw the outside circle.
    my_turtle.penup()
    # Add the shift value + the index, so we can move the cookies.
    my_turtle.goto(-5 + SHIFT * i, -30)
    my_turtle.pendown()
    my_turtle.circle(30)
    my_turtle.penup()

    # Draw the chocolate chips.
    my_turtle.goto(-10 + SHIFT * i, 10)
    my_turtle.stamp()

    my_turtle.goto(-10 + SHIFT * i, -10)
    my_turtle.stamp()

    my_turtle.goto(10 + SHIFT * i, 10)
    my_turtle.stamp()

    my_turtle.goto(10 + SHIFT * i, -10)
    my_turtle.stamp()

# Close the turtle.
turtle.done()
