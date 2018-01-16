import pygame
import os.path
from MappR import Map
from PIL import Image
from PIL import ImageTk
from tkinter import *
from pygame.locals import *

def surf_to_img(surf):
    # export as string / import to PIL
    image_str = pygame.image.tostring(surf, 'RGB')         # use 'RGB' to export
    w, h = surf.get_rect()[2:]
    image = Image.fromstring('RGB', (w, h), image_str) # use 'RGB' to import
    tkimage = ImageTk.PhotoImage(image) # use ImageTk.PhotoImage class instead
    return tkimage

class EditorGUI:

    def __init__(self, master):

        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.grafx_dir = os.path.join(self.main_dir, 'GrafX')
        self.lvl_dir = os.path.join(self.main_dir, 'LevelZ')
        self.iconfile = os.path.join(self.grafx_dir, 'leveleditor.ico')

        self.master = master        
        master.title("Coon Runner - level editor")
        self.master.iconbitmap(self.iconfile)
        self.master.resizable(0,0)

        self.main_frame = Frame(self.master, width = 900, height = 600)
        self.main_frame.pack()

        self.editor_frame = Frame(self.main_frame, width = 600, height = 600)
        self.editor_frame.grid(row = 0, column = 0)
        self.tool_frame = Frame(self.main_frame, width = 300, height = 600)
        self.tool_frame.grid(row = 0, column = 1)
        self.editor_canvas = Canvas(self.editor_frame, width = 600, height = 600) 
        self.editor_canvas.pack()  
        self.editor_canvas.create_rectangle(0,0,600,600, outline = "", fill = "Red")     
        self.center()

        self.map = Map(self.lvl_dir, 'editor.lvl', 'F')
    
    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

pygame.init()
root = Tk()
editor_gui = EditorGUI(root)
root.mainloop()