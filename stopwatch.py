# template for "Stopwatch: The Game"
import simplegui  
# define global variables
a =0 
b =0
c = 0
d = 0
time = 0
#time = str(0)+":"+str(b)+str(c)+"."+str(d)
interval = 0.1
count1 = 0
count2 = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #print "Number: ",t
    if t>600:
        a = t // 600
        a2 = t%600
        b = 0
        c = a2//10
        d = t%10
       # return a, a2, b, c, d
        if c < 10:
            return str(a)+":"+str(b)+str(c)+"."+str(d)
        else:
            return str(a)+":"+str(c)+"."+str(d)
        
    elif t < 600:
        a = 0
        b = 0
        c = t//10
        d = t%10
        if c < 10:
            return str(a)+":"+str(b)+str(c)+"."+str(d)
        else:
            return str(a)+":"+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def start():
    global time, d
    timer.start()
    time = time+1
    return time
        
def stop():
    global d, time, count1, count2
    if timer.is_running():
        timer.stop()
        #success()
        count2 = count2+1
        if time%10==0:
            count1 = count1+1
    return str(count1)+"/"+str(count2)
 
def reset():
    global time, count1, count2
    if timer.is_running():
        stop()
        time = 0
        count1 = 0
        count2 = 0
    else:
        time = 0
        count1 = 0
        count2 = 0
        
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [150, 150], 50, "White")
    canvas.draw_text(str(count1)+"/"+str(count2), [300, 50], 40, "Yellow")
# create frame
frame = simplegui.create_frame("Timer", 400, 300)

# register event handlers
button1 = frame.add_button("Start", start, 100)
button2 = frame.add_button("Stop", stop, 100)
button3 = frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, start)
# start frame
frame.start()
# Please remember to review the grading rubric
