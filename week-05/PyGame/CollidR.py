# CollideR

import CharactR
import MappR
import pygame
from pygame.locals import *

# This class will create collosion self.boxes for walls
class Wall_collider():
    
    def __init__(self, map, x_off, y_off):

        self.map = map

        self.wall_boxes = []
        
        self.boxes = [[{'iswall' : False, 'added' : False} for x in range(self.map.width)] for y in range(self.map.height)]

        tile_third = self.map.tileset.height // 3

        for y in range(self.map.height):
            for x in range(self.map.width):
                if self.map.tilemap[y][x] == 1:
                    tile_type = self.map.get_tile_type(y, x)
                    if tile_type[0]:
                        self.boxes[y][x]['rect'] = pygame.Rect((x_off + x * self.map.tileset.width, y_off + y * self.map.tileset.height), self.map.tileset.size)
                    else:
                        self.boxes[y][x]['rect'] = pygame.Rect(x_off + x * self.map.tileset.width, y_off + tile_third + y * self.map.tileset.height, self.map.tileset.width, self.map.tileset.height - tile_third)
                    self.boxes[y][x]['iswall'] = True
        
        for y in range(self.map.height):
            for x in range(self.map.width):
                if self.boxes[y][x]['iswall']:
                    if not self.boxes[y][x]['added']:
                        wall_segment = self.boxes[y][x]['rect']
                        self.boxes[y][x]['added'] = True                       
                        tile_type = self.map.get_tile_type(y, x)
                        if tile_type[1]:
                            wall_segment.unionall_ip(self.getbricks_v(y, x))
                        self.wall_boxes.append(wall_segment)
     
    # returns list of connecting vertical wall boxes, turns their added value to True,
    # so they cannot be added to another wall_segnment    
    def getbricks_v(self, y, x):

        bricklist = []        
        found_end = False
        off_y = y + 1

        while not found_end and off_y < self.map.height:            
            if self.boxes[off_y][x]['iswall'] and not self.boxes[off_y][x]['added']:        
                bricklist.append(self.boxes[off_y][x]['rect'])            
                self.boxes[off_y][x]['added'] = True            
            else:
                found_end = True            
            off_y += 1

        return bricklist                

    # Test if box collides to any (left or right) side of a wall
    def side_wall_collide(self, box):
        collide = False
        collosions = box.collidelistall(self.wall_boxes)

        for col in collosions:
            if box.x <= self.wall_boxes[col].x + self.wall_boxes[col].w and box.x >= self.wall_boxes[col].x or box.x + box.w >= self.wall_boxes[col].x and box.x + box.w <= self.wall_boxes[col].x + self.wall_boxes[col].w:
                collide = True
        return collide
    
    # Test if a box collides to any top or moddom side of a wall
    def topdown_wall_collide(self, box):
        collide = False
        collosions = box.collidelistall(self.wall_boxes)
        
        for col in collosions:
            if box.y <= self.wall_boxes[col].y + self.wall_boxes[col].h and box.y >= self.wall_boxes[col].y or box.y + box.h >= self.wall_boxes[col].y and box.y + box.h <= self.wall_boxes[col].y + self.wall_boxes[col].h:
                collide = True
        return collide
