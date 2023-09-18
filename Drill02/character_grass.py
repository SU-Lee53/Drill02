from pico2d import *
import math
import os

os.chdir('C:\\Users\\dltmd\\OneDrive\\Documents\\2-2\\2DGP\\Drill02')
open_canvas(800, 600)

# fill here

grass = load_image('grass.png')
character = load_image('character.png')


temp = 0
midX = 250
midY = 250
pi = math.pi

while True:
    if temp % 2 == 0:
        for deg in range(270, 630):
            deg = math.radians(deg)
            clear_canvas_now()
            grass.draw_now(400, 30)
            currX = (midX * math.cos(deg)) + 400
            currY = (midY * math.sin(deg)) + 340
            character.draw_now(currX, currY)
            delay(0.01)
        temp += 1
        
    else:
        x = 400
        y = 90
        while x <= 750:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01) 
            x += 3

        while y <= 550:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01) 
            y += 3

        while x >= 50:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01) 
            x -= 3

        while y >= 90:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01) 
            y -= 3

        while x <= 400:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01) 
            x += 3
        temp += 1
    
    
close_canvas()