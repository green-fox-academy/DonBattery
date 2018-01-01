# CollideR

import CharactR
import MappR
import pygame
from pygame.locals import *

# This God-class will be responsible to check collosions in the game
# It create collosion boxes for walls and test the character's footboxes against them 
# Also it can test characters to characters relations and even more ;)
class Collider():
    
    def __init__(self, map, x_off, y_off):

        self.map = map

        self.map_rect = pygame.Rect(x_off, y_off, map.width * map.tileset.width, map.height * map.tileset.height)

        self.foot_boxes = []

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
        
        top_box = pygame.Rect(x_off - 2, y_off - 2, map.width * map.tileset.width + 4, 2)
        left_box = pygame.Rect(x_off -2, y_off - 2, 2, map.height * map.tileset.height + 4)
        bot_box = pygame.Rect(x_off -2, y_off + map.height * map.tileset.height, map.width * map.tileset.width + 4, 2)
        right_box = pygame.Rect(x_off + map.width * map.tileset.width, y_off - 2, 2, map.height * map.tileset.height + 4)

        self.wall_boxes.append(top_box)
        self.wall_boxes.append(left_box)
        self.wall_boxes.append(bot_box)
        self.wall_boxes.append(right_box)
     
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
        collosions = box.collidelistall(self.wall_boxes)
        for col in collosions:
            if box.x <= self.wall_boxes[col].x + self.wall_boxes[col].w and box.x >= self.wall_boxes[col].x or box.x + box.w >= self.wall_boxes[col].x and box.x + box.w <= self.wall_boxes[col].x + self.wall_boxes[col].w:
                return True
        return False
    
    # Test if a box collides to any top or boddom side of a wall
    def topdown_wall_collide(self, box):
        collosions = box.collidelistall(self.wall_boxes)        
        for col in collosions:
            if box.y <= self.wall_boxes[col].y + self.wall_boxes[col].h and box.y >= self.wall_boxes[col].y or box.y + box.h >= self.wall_boxes[col].y and box.y + box.h <= self.wall_boxes[col].y + self.wall_boxes[col].h:
                return True
        return False
    
    # Test if a box collides to any left or right side of a foot_box
    def side_foot_collide(self, foot, box):
        test_boxes = self.foot_boxes + self.wall_boxes
        test_boxes.remove(foot)
        collosions = box.collidelistall(test_boxes)        
        for col in collosions:
            if box.x <= test_boxes[col].x + test_boxes[col].w and box.x >= test_boxes[col].x or box.x + box.w >= test_boxes[col].x and box.x + box.w <= test_boxes[col].x + test_boxes[col].w:
                return True
        return False
    
    # Test if a box collides to top or bottom of a footbox
    def topdown_foot_collide(self, foot, box):
        test_boxes = self.foot_boxes + self.wall_boxes 
        test_boxes.remove(foot)
        collosions = box.collidelistall(test_boxes)        
        for col in collosions:
            if box.y <= test_boxes[col].y + test_boxes[col].h and box.y >= test_boxes[col].y or box.y + box.h >= test_boxes[col].y and box.y + box.h <= test_boxes[col].y + test_boxes[col].h:
                return True
        return False

    # Test if box can go left or right
    def horizontal_ok(self, foot_box, check_box):
        if self.side_foot_collide(foot_box, check_box):
            return False
        return True
    
    # Test if box can move up or down
    def vertical_ok(self, foot_box, check_box):
        if self.topdown_foot_collide(foot_box, check_box):
            return False        
        return True

    def update_foot_boxes(self, unitlist):
        self.foot_boxes = []
        for unit in unitlist:
            self.foot_boxes.append(unit.foot_rect)