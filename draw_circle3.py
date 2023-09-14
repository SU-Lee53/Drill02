import turtle
from random import randint as rand

def draw_circle(x,y,r):
    turtle.penup()
    turtle.goto(x,y)
    turtle.stamp()
    turtle.goto(x,y-r)
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()
    

turtle.shape("turtle")
draw_circle(0,0,50)
draw_circle(200, 200, 100)
draw_circle(100, -100, 50)

for _ in range(5):
    draw_circle(rand(30, 200), rand(30,200), rand(30, 100))
