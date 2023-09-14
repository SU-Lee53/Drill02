import turtle
from random import randint as rand

def drunken_move():
    turtle.setheading(rand(0, 360))
    turtle.forward(rand(50, 300))
    turtle.stamp()

def move_left():
    turtle.right(90)
    turtle.forward(50)
    turtle.stamp()

def move_right():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()


turtle.shape('turtle')

turtle.onkey(drunken_move, ' ')
turtle.onkey(move_left, 'a')
turtle.onkey(move_right, 'd')
turtle.listen()

