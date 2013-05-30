#Watch implementation at http://www.codeskulptor.org/#user15_SqfksRaUtu_0.py
import simplegui
import random

width = 500
height = 400
radius = 8
color_list = ["Green", "Yellow", "Red", "Blue", "White"]
direction = [[0,1], [-1,1], [1, -1], [-1, -1], [1, 0], [-1, 0]]

class Particle:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        
    def update(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
        
    def draw(self, canvas):
        canvas.draw_circle(self.position, 1, radius, self.color, self.color)

def draw(canvas):
    for p in particle_list:
        p.update(random.choice(direction))
    for p in particle_list:
        p.draw(canvas)
        
frame = simplegui.create_frame("Test", width, height)

particle_list = []
for i in range(100):
    p = Particle([width/2, height/2], random.choice(color_list))
    particle_list.append(p)
        
frame.set_draw_handler(draw)

frame.start()
