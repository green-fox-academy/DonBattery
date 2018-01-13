#!/usr/bin/env python
# encoding: utf-8

import sys
import os.path
from arger import Argument_Compiler
from filer import File_Controller

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
        
        # PWD
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        # Help file to be displayed on -h -help command
        self.help_file = 'ggnore_help'
        # Help file controller
        self.help_file_con = File_Controller(self.main_dir, self.help_file)

        if not self.help_file_con.test_file():
            print('\n')
            print('Error: Cannot read help file')
            for err in self.help_file_con.error_log:
                print(err)

        # this object is the argumentum-compiler: from the argv list and excepted commands
        # it puts the actual calculated commands into its command_lsit
        self.arg_con = Argument_Compiler(self.arg_list, self.allowed_commands)
    
    def print_usage(self):
        print('\nGGNORE Web Gallery Generator')
        print('\nUsage :')
        print('\n-f <path to be searched for images> If not defined the pwd will be searched')
        print('-g <gallery path>                     If not defined the gallery folder will be created in the pwd')
        print('-s                                    Inclued subfolders')
        print('-nogif                                Exclude gif files')
        print('-css <stylename>                      If not defined the gallery will have no style')
        print('-h / -help                            Display help')

    def print_help(self):
        if self.help_file_con.file_stat['present']:
            print('\n')            
            for line in self.help_file_con.file_as_lines:
                print(line)
        else:
            print('\n Sorry pal, no help file is present...')


    def go(self):

        if self.arg_con.no_commands():
            self.print_usage()
        else:
            for com in self.arg_con.command_list:
                if com['command'] == '-h' or '-help':
                    self.print_help()

        print(self.arg_con.get_commands())    

def main(args):
    gallery = GalleryGenerator(args)
    gallery.go() 

if __name__ == '__main__':
    main(sys.argv)