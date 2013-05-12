import simplegui
current_key = ' '


def keydown(key):
    global current_key
    current_key = chr(key)
    
def keyup(key):
    global current_key
    current_key = ' '  
    
    
    
def draw_handler(canvas):
    canvas.draw_text(current_key, [75, 120], 80, "White")

frame = simplegui.create_frame("Test keyboard", 200, 200)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
