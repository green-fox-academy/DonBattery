#!/usr/bin/env python
# encoding: utf-8

import sys
import os.path as dir
from arger import Argument_Compiler

class GalleryGenerator(object):
    
    def __init__(self, arglist):

        # we can pass these dictionaries to the argumentum-compiler so
        # it will know what commands to search for
        self.allowed_commands = ({'operator' : '-f', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-g', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-s', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-nogif', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-css', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-h', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-help', 'type' : 'Single', 'item' : ''})

        # the sys.argv list
        self.arg_list = arglist

        # this object is the argumentum-compiler: from the argv list and excepted commands
        # it puts the actual calculated commands into its command_lsit
        self.arg_con = Argument_Compiler(self.arg_list, self.allowed_commands)
    
    def print_usage(self):
        print('\nGGNORE Web Gallery Generator')
        print('\nUsage :')
        print('\n-f <path to be searched for images>   If not defined the pwd will be searched')
        print('-g <gallery path>                     If not defined the gallery folder will be created in the pwd')
        print('-s                                    Inclued subfolders')
        print('-nogif                                Exclude gif files')
        print('-css <stylename>                      If not defined the gallery will have no style')
        print('-h / -help                            Display help')

    def go(self):

        if self.arg_con.no_commands():
            self.print_usage()

        print(self.arg_con.get_commands())    

def main(args):
    gallery = GalleryGenerator(args)
    gallery.go() 

if __name__ == '__main__':
    main(sys.argv)