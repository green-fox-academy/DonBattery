# Mapper

import pygame
from pygame.locals import *
import ImagR
import FilR

class Tile_set():
    def __init__(self, filepath, file, size):
        self.image = ImagR.load_image(filepath, file)
        self.size = size

class Map():
    def __init__(self, filepath, file):
        self.file_con = FilR.File_Controller(filepath, file)
        self.file_con.test_file()
        self.data = self.file_con.get_lines()
        self.info = self.data[0].split(';')
        self.tilemap = self.data[1].split(';')
