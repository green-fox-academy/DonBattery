from tkinter import *

class EditorGUI:

    def __init__(self, master):
        self.master = master        
        master.title("Coon Runner - level editor")
        self.master.iconbitmap("leveleditor.ico")
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
    
    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = Tk()
editor_gui = EditorGUI(root)
root.mainloop()