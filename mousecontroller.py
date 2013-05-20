# watch implementation at http://www.codeskulptor.org/#user13_nS0InDUstk_0.py

import simplegui
import math

width = 500
height = 400
ball_pos = [width/2, height/2]
ball_radius = 20
ball_colour = "Red"

def distance(p, q):
    return math.sqrt( (p[0]-q[0])**2 + (p[1]-p[1])**2)

def click(pos):
    global ball_pos, ball_colour
    
    if distance(pos, ball_pos) < ball_radius:
        ball_colour = "Blue"
    else:
        ball_pos = list(pos)
        ball_colour = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, ball_radius, 1, ball_colour, ball_colour)

frame = simplegui.create_frame("Test", width, height)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()
