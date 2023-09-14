import turtle
import random

turtle.shape('turtle')

turtle.penup()
turtle.goto(-400, -400)
turtle.pendown()

while(True):
    turtle.setheading(random.randint(0,60))
    turtle.forward(random.randint(30, 70))
    turtle.stamp()
