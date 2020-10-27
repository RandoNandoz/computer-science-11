import turtle
anna = turtle.Turtle()

# Draw the outside
anna.penup()
anna.goto(-5, -30)
anna.pendown()
anna.circle(30)
anna.penup()

# Chocolate chip middle
anna.goto(0, 0)
anna.stamp()


# Chocolate chip top left
anna.goto(-10, 10)
anna.stamp()


# Chocolate chip bottom left
anna.goto(-10, -10)
anna.stamp()


# Chocolate chip bottom right
anna.goto(10, -10)
anna.stamp()

# Chocolate chip top right
anna.goto(10, 10)
anna.stamp()


turtle.done()
