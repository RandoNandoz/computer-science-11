"""
Draw shape from user input
Randy Zhu
11-2-2020
"""

import turtle

n_side_num = int(
    input("How many sides would you like your shape to have? (3 - 10): "))
if n_side_num < 3:
    exit()
elif n_side_num > 10:
    exit()

my_turtle = turtle.Turtle()
my_turtle.penup()
angle = 360 / n_side_num
RADIUS = 500

for _ in range(n_side_num):
    my_turtle.pendown()
    my_turtle.forward(RADIUS)
    my_turtle.left(angle)

turtle.done()
