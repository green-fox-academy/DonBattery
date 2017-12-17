#Starry Night -Miki

# We need Tkinter for the canvas to draw on, randint to generate some nice integers and sleep to wait a bit...
from tkinter import *
from random import randint
from time import sleep

# The HEX color table
hexer = {'y1' : '#fff5cc', 'y2' : '#ffe680', 'y3' : '#ffd633', 'y4' : '#cca300',
        'b1' : '#ccd9ff', 'b2' : '#809fff', 'b3' : '#3366ff', 'b4' : '#002db3',
        'g1' : '#ccff99', 'g2' : '#8cff1a', 'g3' : '#4d9900', 'g4' : '#1a3300',
        'w1' : '#e6ffff', 'w2' : '#ffffe6', 'w3' : '#e6ffe6', 'w4' : '#ffffff',
        'Black' : '#000033'}

# color lists
yelows = [hexer['y1'], hexer['y2'], hexer['y3'], hexer['y4']]
blues = [hexer['b1'], hexer['b2'], hexer['b3'], hexer['b4']]
greens = [hexer['g1'], hexer['g2'], hexer['g3'], hexer['g4']]
whites = [hexer['w1'], hexer['w2'], hexer['w3'], hexer['w4']]

# stroke sequences
circ = [0, 22, 45, 67, 90, 110, 135, 155, 180, 202, 225, 247, 270, 292, 315, 337]

# Init the canvas and store maxX, maxY
root = Tk()

canvas = Canvas(root, width='400', height='300')
canvas.pack()

maxx = int(canvas['width'])
maxy = int(canvas['height'])

canvas['bg'] = 'Black'

# Colored arc for drawing
def stroke(scentX, scentY, sRad, sStart, sStop, sWidth, sColor):
    stopx = scentX - sRad
    stopy = scentY - sRad
    sbotx = scentX + sRad 
    sboty = scentY + sRad    
    canvas.create_arc(stopx, stopy,  sbotx, sboty, start = sStart, extent = sStop, width = sWidth, outline = sColor, fill = '', style = ARC)

# Draws a star
def star(scentX, scentY, sRad, Moon = False):
    for i in range(sRad, 1, -1):
        for j in range(len(circ)):
            if j > 0 and randint(1,3) == 1: stroke(scentX, scentY, i + randint(-2, 2), circ[j - 1] + randint(-9, 9), circ[j] + randint (-9, 9), randint(2, 8), yelows[i % 4])

# Draws out the stars (it prevents them to placed on eachother)
def stars(amount, maxrad):
    stack = []
    while len(stack) < amount:
        a = True
        x = randint(maxrad, maxx - maxrad)
        y = randint(maxrad, (maxy // 5) * 3)
        for i in range(len(stack)):
            if (stack[i][0] - maxrad // 2 < x < stack[i][0] + maxrad // 2 and stack[i][1] - maxrad // 2 < y < stack[i][1] + maxrad // 2) or ((maxx // 9) * 6 < x and (maxy // 6) > y ): a = False
        if a: stack.append([x, y])
    for i in range(len(stack)):
        star(stack[i][0], stack[i][1], randint((maxrad // 3), maxrad))

def bars():
    for i in range(4):
        canvas.create_rectangle(0, i * maxy // 4, maxx, maxy, outline="", fill=blues[i])

bars()
stars(7, 22)
stars(3, 33)
stars(2, 44)

root.mainloop()

''' for i in range(30):
    stroke(maxx // 2, maxy // 2, maxx // 3, 0, 90, 1, hexer['y2'])
    stroke(maxx // 2, maxy // 2, maxx // 4, 0, 90, 1, hexer['y1'])
    stroke(maxx // 2, maxy // 2, maxx // 5, 0, 90, 1, hexer['y3'])
    stroke(maxx // 2, maxy // 2, maxx // 6, 0, 90, 1, hexer['y4'])
    stroke(maxx // 2, maxy // 2, maxx // 7, 0, 90, 1, hexer['g2'])
    stroke(maxx // 2, maxy // 2, maxx // 8, 0, 90, 1, hexer['w2'])
    stroke(maxx // 2, maxy // 2, maxx // 9, 0, 90, 1, hexer['b2'])
    stroke(maxx // 2, maxy // 2, maxx // 40, 0, 90, 1, hexer['b4']) '''