# watch implementation at http://www.codeskulptor.org/#user13_m98NV5Ucrr_0.py

import simplegui
width = 500
height = 500
circle_pos = [width/2, height/2]


def keydown(key):
    global circle_pos
    if key == simplegui.KEY_MAP['down']:
        circle_pos[1] = circle_pos[1]+5
    if key == simplegui.KEY_MAP['up']:
        circle_pos[1]= circle_pos[1]-5
    if key ==simplegui.KEY_MAP['left']:
        circle_pos[0]= circle_pos[0]-5
    if key == simplegui.KEY_MAP['right']:
        circle_pos[0] = circle_pos[0]+5
    
   
    
def draw_handler(canvas):
    canvas.draw_circle(circle_pos, 15, 10, "White")

frame = simplegui.create_frame("Test keyboard", width, height)
text = frame.add_label("Press up|down|left|right key")
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown)

frame.start()
