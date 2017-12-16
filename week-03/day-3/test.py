''' from Tkinter import *

root = Tk()

canvas = Canvas(root, width='200', height='100', bg='yellow')
canvas.pack() '''

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("True1.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()


