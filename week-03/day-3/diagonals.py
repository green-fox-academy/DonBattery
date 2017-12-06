from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = int(canvas['width'])
y = int(canvas['height'])

# draw the canvas' diagonals in green.
green_line = canvas.create_line(0 , 0, x, y, fill = 'green', width = 3)

green_line = canvas.create_line(0, y, x, 0, fill = 'limegreen', width = 3)

root.mainloop()
