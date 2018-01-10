from tkinter import *
from PIL import ImageTk, Image
import os
import time

root = Tk()

root.title('Hatalmas RPG Játék')

root.iconbitmap(r'C:\Users\Miki\greenfox\DonBattery\week-05\RPG_Game\Tiles\badcat3.ico')

map_width = 15

map_height = 15

tile_size = 32

map1 = []

canvas = Canvas(root, height = map_height * tile_size, width = map_width * tile_size)

tile1 = ImageTk.PhotoImage(Image.open("C:/Users/Miki/greenfox/DonBattery/week-05/RPG_Game/Tiles/floor1.png"))

character1 = ImageTk.PhotoImage(Image.open("C:/Users/Miki/greenfox/DonBattery/week-05/RPG_Game/Tiles/horse.png"))

root.resizable(False, False)

def init_map(base_tile):
    return [[{'Walk': True, 'image' : base_tile} for x in range(map_width)] for y in range(map_height)]

def draw_map(map):
    for x in range(map_width):
        for y in range(map_height):
            if map[y][x]['image'] == 'tile1':
                tile_img = tile1
                canvas.create_image(x * tile_size, y * tile_size, anchor = NW, image = tile_img)

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

map1 = init_map('tile1')

#center(root)

print(root.winfo_width(), root.winfo_height())

lo_x = 115
lo_y = 19
lo_vx = -1
lo_vy = -1

draw_map(map1)

lo = canvas.create_image(lo_x, lo_y, image = character1, anchor = NW)

vonal1 = canvas.create_line(0, 0, map_width * tile_size - 32, map_height * tile_size - 32)

canvas.pack()


while True:

    canvas.move(lo, lo_vx, lo_vy)
    lo_coords = canvas.coords(lo)
    lo_x = lo_coords[0]
    lo_y = lo_coords[1]
    print(lo_coords)
    print((map_height - 1) * tile_size)
    time.sleep(0.05)
    if lo_x >= (map_width - 1)* tile_size:
        lo_vx = -1
    if lo_x <= 1:
        lo_vx = 1
    if lo_y >= (map_height - 1) * tile_size:
        lo_vy = -1
    if lo_y <= 1:
        lo_vy = 1
    root.update()



#canvas.create_image(0, 0, anchor=NW, image = tile1)