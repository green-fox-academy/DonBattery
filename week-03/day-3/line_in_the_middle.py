from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = int(canvas['width'])
y = int(canvas['height'])

# draw a red horizontal line to the canvas' middle.
red_line = canvas.create_line(0, y // 2, x, y // 2, fill ='red')

# draw a green vertical line to the canvas' middle.
green_line = canvas.create_line(x // 2, 0, x // 2, y, fill = 'green')

root.mainloop()

