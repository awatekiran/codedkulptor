# Implementation of classic arcade game Pong
# watch implementation at http://www.codeskulptor.org/#user13_sa3ibOzo4Q_8.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [-1, -1]
paddle1_pos = 40.0
paddle1_vel = 0.0
paddle2_pos = 40.0
paddle2_vel = 0.0
score1 = 0
score2 = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if right :
        ball_vel = [random.randrange(1, 5),- random.randrange(1, 5)]
    else:
        ball_vel = [- random.randrange(1, 5),- random.randrange(1, 5)]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(True)
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    if paddle1_pos >= HEIGHT-40: 
        paddle1_pos = HEIGHT-40
    elif paddle1_pos <= 40:
        paddle1_pos = 40
    if paddle2_pos >= HEIGHT-40: 
        paddle2_pos = HEIGHT-40
    elif paddle2_pos <= 40:
        paddle2_pos = 40
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line((0, paddle1_pos-40), (0, paddle1_pos + 40), 16, "White")
    c.draw_line((WIDTH, paddle2_pos-40), (WIDTH, paddle2_pos+40), 16, "White")
                
                
    # update ball
    ball_pos[0] +=1*ball_vel[0]
    ball_pos[1] +=1*ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= (PAD_WIDTH+BALL_RADIUS):
        if ball_pos[1]<paddle1_pos+40 and ball_pos[1]>paddle1_pos-40:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = 1.5*ball_vel[0] # Increases velocity of ball
            ball_vel[1] = 1.5*ball_vel[1] # with each bounce off paddle
        else:
            ball_init(True)
            score2 +=1
        
    if ball_pos[0] >= ((WIDTH-1)-(PAD_WIDTH+BALL_RADIUS)):
        if ball_pos[1]<paddle2_pos+40 and ball_pos[1]>paddle2_pos-40:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = 1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
        else:
            ball_init(False)
            score1 +=1
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 5, "White", "White")
    c.draw_text(str(score1), [WIDTH/4, 60], 50, "White")
    c.draw_text(str(score2), [WIDTH/1.4, 60], 50, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel-=4
    elif key == simplegui.KEY_MAP['S']:
        paddle1_vel+=4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel-=4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel+=4
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP['S']:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel=0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button("Restart", new_game, 100)
Text= frame.add_label("W|S to move left paddle and Up|Down to move right paddle", 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
