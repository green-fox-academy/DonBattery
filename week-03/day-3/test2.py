from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = int(canvas['width'])
y = int(canvas['height'])

# draw the canvas' diagonals in green.

# R G B to HEX converter
def rgbhex(r,g,b):
    return '#%02x%02x%02x' % (r, g, b)

canvas.create_arc(10,10,20,20, start = 200, extent = 250, width = randint(1,3), outline = rgbhex(randint(220, 255), randint(220, 255), randint(220, 255)), fill = '', style = ARC)


root.mainloop()
