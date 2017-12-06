from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x_top, y_top, x_bot, y_bot = 10, 10, 290, 290

# draw a box that has different colored lines on each edge.
canvas.create_rectangle(x_top, y_top, x_bot, y_bot, outline="", fill="#579fb4")
canvas.create_line(x_top, y_top, x_top, y_bot, fill = 'red', width = 3) #left
canvas.create_line(x_top, y_bot, x_bot, y_bot, fill = 'green', width = 3) #bot
canvas.create_line(x_bot, y_top, x_bot, y_bot, fill = 'blue', width = 3) #right
canvas.create_line(x_top, y_top, x_bot, y_top, fill = 'magenta', width = 3) #top

root.mainloop()
