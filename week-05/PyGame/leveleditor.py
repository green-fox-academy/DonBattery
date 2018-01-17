# Basic level editor tool for the Coon Runner Pygame

from tkinter import *
import os.path

# The Leveleditor god-class
class EditorGUI:

    def __init__(self, master):

        # Set up our directories
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.grafx_dir = os.path.join(self.main_dir, 'GrafX')
        self.lvl_dir = os.path.join(self.main_dir, 'LevelZ')
        self.iconfile = os.path.join(self.grafx_dir, 'leveleditor.ico')

        # Set up the Window
        self.master = master        
        master.title("Coon Runner - level editor")
        self.master.iconbitmap(self.iconfile)
        self.master.resizable(0,0)
        self.main_frame = Frame(self.master, width = 900, height = 600)
        self.main_frame.pack()
        self.center()

        # Set up the editor frame
        self.editor_frame = Frame(self.main_frame, width = 600, height = 600)
        self.editor_frame.grid(row = 0, column = 0)

        # Set up the tool frame
        self.tool_frame = Frame(self.main_frame, width = 300, height = 600)
        self.tool_frame.grid(row = 0, column = 1)

        # Set up the editor canvas
        self.editor_canvas = Canvas(self.editor_frame, width = 600, height = 600) 
        self.editor_canvas.pack()  
        self.editor_canvas.create_rectangle(0,0,600,600, outline = "", fill = "Red")

    # Center the window
    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    def draw_map(self):
        pass


# Start the app
root = Tk()
editor_gui = EditorGUI(root)
root.mainloop()