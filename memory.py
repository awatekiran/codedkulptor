# implementation of card game - Memory
# Watch implementation at http://www.codeskulptor.org/#user14_R0dCmcihshWzGnM.py

import simplegui
import random
list1 = range(0, 8)
list2 = range(0, 8)
pos = [15, 60]
pos2 = [410, 60]
exposed = False
deck = list1+list2
cards = len(deck)
exposed = [False]*16
count = 0


# helper function to initialize globals
def init():
    global pos, list1, list2, deck, cards, state, count, exposed
    count = 0
    exposed = [False]*16
#    print list1
#    print list2
#    print deck
    random.shuffle(deck)
    state = 0
    label.set_text("Moves = 0")  
       
     
# define event handlers
def mouseclick(pos):
    global state, count, deck, card1, card2
    
    click = pos[0]//50
    if exposed[click]== False:
        exposed[click]=True
    else:
        pass
    
    # add game state logic here
    
    if state == 0:
        state = 1
        card1 = click
        exposed[card1] = True 
        count += 1
#        label.set_text("Moves = " + str(count))
    elif state == 1:
        state = 2
        card2 = click
        exposed[card2] = True
#        label.set_text("Moves = " + str(count))
    elif state == 2:
        if deck[card1] != deck[card2]:
            exposed[card1] = False
            exposed[card2] = False
            exposed[click] = True
            state = 1
            card1 = click
            if exposed[card1] == True:
                count +=1
            else:
                pass
#            label.set_text("Moves = " + str(count))
        else:
            exposed[card1] = True
            exposed[card2] = True
            state = 1
            card1 = click
            if exposed[click]== True:
                count += 1
#            label.set_text("Moves = " + str(count))
    
    label.set_text("Moves = " + str(count))            
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos, list1, list2, exposed, deck
    for n in range(len(deck)):
        if exposed[n]==True:
            canvas.draw_text(str(deck[n]), (pos[0]+n*50, pos[1]), 40, "White")
        else:
            canvas.draw_polygon([[(n*50)+0, 0], [(n*50)+50, 0], [(n*50)+50, 100], [(n*50)+0, 100]], 4, "Black", "Green")
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")


# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
