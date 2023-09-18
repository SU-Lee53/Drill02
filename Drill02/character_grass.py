from pico2d import *
import math
open_canvas(800, 600)

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
temp = 0
midX = 250
midY = 250
pi = math.pi

while True:
    if temp % 2 == 1:
        for deg in range(270, 630):
            deg = math.radians(deg)
            clear_canvas_now()
            grass.draw_now(400, 30)
            currX = (midX * math.cos(deg)) + 400
            currY = (midY * math.sin(deg)) + 300
            character.draw_now(currX, currY)
        temp += 1
    else:
        for x in range(400, 750):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)

        for y in range(90, 550):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
    
        for x in range(750, 50, -1):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)

        for y in range(550, 90, -1):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
        temp += 1
                       


close_canvas()