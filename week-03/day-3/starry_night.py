# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
from random import randint
# from os import system

# R G B to HEX converter
def rgbhex(r,g,b):
    return '#%02x%02x%02x' % (r, g, b)

root = Tk()

canvas = Canvas(root, width='400', height='300')
canvas.pack()

max_x = int(canvas['width'])
max_y = int(canvas['height'])

canvas['bg'] = rgbhex(0,0,60)

def star(relx, rely, dim, moon = False):
    step = randint(2,15)   
    for i in range(step, 1, -1):
        relx += randint(-1,1)
        rely += randint(-1,1)
        topx = relx - dim // 2
        topy = rely - dim // 2
        botx = relx + dim // 2
        boty = rely + dim // 2
        canvas.create_oval(topx, topy, botx, boty, outline="", fill = rgbhex(255 - i * randint(7,15), 255 - i * randint(7,15), 255 - i * randint(3,6)))
        dim -= 2
    canvas.create_oval(relx - 2, rely - 2, relx + 1, rely + 1, outline = "", fill = rgbhex(250,250,15))
    if moon:
        canvas.create_oval(relx - randint(15, 20), rely - randint(15, 20),  relx + randint(15, 20), rely + randint(15, 20), outline = "", fill = rgbhex(233,233,0))
        canvas.create_oval(relx, rely - randint(20, 25),  relx + randint(25, 30), rely + randint(5, 10), outline = "", fill = rgbhex(233,233,233))

def star2(centx, centy, size, moon = False):
    step = randint(10, 30)
    half = size // 2
    for i in range(0, step):
        diff = randint(1,5)
        for j in range(10):
            ext = j * 36
            canvas.create_arc(centx - half - diff, centy - half - diff, centx + half + diff, centy + half + diff, start = ext, extent = ext + randint(30,40), width = randint(1,3), outline = rgbhex(randint(220, 255), randint(220, 255), randint(220, 255)), fill = '', style = ARC)
            canvas.create_rectangle(centx - half - diff, centy - half - diff, centx + half + diff, centy + half + diff, outline = "", fill = rgbhex(randint(5,20),randint(10,25),randint(10,25)))
            half -= randint(1, 3)

def bush(topx, topy, maxw, complexity):
    h = max_y - topy
    for i in range(complexity):
            pos = randint(topx, topx + maxw)
            canvas.create_rectangle(pos, topy + h // 10 * randint(1, 6) , randint(pos, topx + maxw), max_y, outline = "", fill = rgbhex(randint(5,20),randint(10,25),randint(10,25)))
    canvas.create_rectangle(topx + maxw // 5 * 2, topy, topx + maxw // 5 * 3, max_y, outline = "", fill = rgbhex(randint(5,20),randint(10,25),randint(10,25)))

def arc(topx, topy, w, h, stroke, c):
    if c == 'dblue':
        Red = randint(10,20)
        Green = randint(10,20)
        Blue = randint(35,75)
    elif c == 'blue':
        Red = randint(20,30)
        Green = randint(20,30)
        Blue = randint(75,125)
    elif c == 'white':
        Red = randint(222,255)
        Green = randint(222,255)
        Blue = randint(222,255)
    elif c == 'lgrey':
        Red = randint(125,200)
        Green = randint(125,200)
        Blue = randint(125,200)
    canvas.create_arc(topx, topy, topx + w, topy + h, start = randint(66, 180), extent = stroke, width = randint(1,3), outline = rgbhex(Red,Green,Blue), fill = '', style = ARC)

#background bars
for i in range(10):
    canvas.create_rectangle(0, ((max_y // 20) * 10) + (i * max_y // 20), max_x, max_y, outline = "", fill = rgbhex(0,0,60 - i * 6))

#background arcs
for i in range(400):
    arc(randint(0, max_x - 10), randint(0, max_y // 5 * 3), randint(10,15), randint(10,15), randint(33,188), 'dblue')
for i in range(300):
    arc(randint(0, max_x - 10), randint(0, max_y // 5 * 3), randint(10,15), randint(10,15), randint(33,188), 'blue')
for i in range(200):
    arc(randint(0, max_x - 10), randint(0, max_y // 5 * 3), randint(10,15), randint(10,15), randint(33,188), 'lgrey')
for i in range(50):
    arc(randint(0, max_x - 10), randint(0, max_y // 5 * 3), randint(10,15), randint(10,15), randint(33,188), 'white')

#stars
for i in range(1):
    #star(randint(5,max_x - max_x // 11), randint(5, max_y - max_y // 11 * 5), randint(11, 35), False)
    star2(randint(5, max_x - 5), randint(5, max_y // 7 * 4), randint(5,15), False)

#moon
star(randint(max_x - max_x // 5 - 5, max_x - max_x // 5 -5), randint(5, max_y // 5), randint(65, 75), True)

#houses
for i in range(66):
    h = randint(11, 35)
    w = randint(11, 45)
    topx = randint(0, max_x - w)
    topy = randint((max_y) // 5 * 3, max_y - h) 
    c = rgbhex(0,randint(0, 55), randint(0, 77))
    canvas.create_rectangle(topx, topy, topx + w, topy + h, outline = "", fill = c)
    for j in range(randint(1, 2)):
        wh = randint(3,7)
        ww = randint(3,7)
        wx = topx + randint(0, w - ww - 1)
        wy = topy + randint(0, h - wh - 1)
        c = rgbhex(randint(150,200),randint(150, 200), 0)
        canvas.create_rectangle(wx, wy, wx + ww, wy + wh, outline = "", fill = c)

#bush
bush(randint(10, max_x - max_x // 5 * 4), max_y // 7, max_x // 5 + randint(0, 10), 7)

root.mainloop()