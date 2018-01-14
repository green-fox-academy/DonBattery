#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from arger import Argument_Compiler
from filer import File_Controller

class GalleryGenerator(object):
    
    def __init__(self, arglist):

        # we can pass these dictionaries to the argumentum-compiler so
        # it will know what commands to search for
        self.allowed_commands = ({'operator' : '-f', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-g', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-s', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-i', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-m', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-nogif', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-css', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-h', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-help', 'type' : 'Single', 'item' : ''})

        # The sys.argv list
        self.arg_list = arglist
        
        # PWD
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]

        # This directory will be searched, by default it will be the PWD, can be modifyed with -f <path>
        self.search_dirs = []

        # This list will contain the URL-s to image files found in search directories
        self.file_list = []

        # Help file to be displayed on -h -help command
        self.help_file = 'ggnore_help'

        # Help file controller
        self.help_file_con = File_Controller(self.main_dir, self.help_file)

        self.search_subdirs = False

        # This object is the argumentum-compiler: from the argv list and excepted commands
        # it puts the actual calculated commands into its command_lsit
        self.arg_con = Argument_Compiler(self.arg_list, self.allowed_commands)

    # Exit the app
    def terminate(self):
        print('\nExiting...')
        sys.exit()

    # Prints out the usage of GGNORE
    def print_usage(self):
        print('\nGGNORE Web Gallery Generator')
        print('\nUsage :')
        print('\n-m                                    Make gallery')
        print('-i                                    Display information on directories')
        print('-f <path to be searched for images>   If not defined the pwd will be searched')
        print('-g <gallery path>                     If not defined the gallery folder will be created in the pwd')
        print('-s                                    Inclued subfolders')
        print('-nogif                                Exclude gif files')
        print('-css <stylename>                      If not defined the gallery will have no style')
        print('-h / -help                            Display help')

    # Prints out the help file if present
    def print_help(self):
        if self.help_file_con.file_stat['present']:
            print('\n')            
            for line in self.help_file_con.file_as_lines:
                print(line, end = '')
        else:
            print('\n Sorry pal, no help file is present...')

    # Returns all subdirectories of a directory
    def get_subdirectories(self, d_dir):
        return [name for name in os.listdir(d_dir) if os.path.isdir(os.path.join(d_dir, name))]  

    # Fill the file_list with image URLs found in search directories
    def populate_file_list(self):
        new_list = []
        if self.arg_con.is_command_present('-s'):
            for d_dir in self.search_dirs:
                new_list.append(d_dir)
                for s_dir in self.get_subdirectories(d_dir):
                    new_list.append(os.path.join(d_dir, s_dir))
            self.search_dirs = new_list
        for d_dir in self.search_dirs:
            self.file_list.append([os.path.join(d_dir, f) for f in os.listdir(d_dir) if os.path.isfile(os.path.join(d_dir, f)) and f[-4:] in ['.gif']])
        # TEST PRINT ##########################################
        print(self.file_list)

    # Main method, translates arguments, do magic
    def go(self):
        # Help file test
        if not self.help_file_con.test_file():
            print('\n')
            print('Error: Cannot read help file')
            for err in self.help_file_con.error_log:
                print(err)
        # If no valid command print out usage
        if self.arg_con.no_commands():
            self.print_usage()
        else:
            ############### TEST PRINT ##########################
            #print(self.arg_con.command_list)
            found = False
            generate = False
            getinfo = False
            # Go through the commans list and execute them
            for com in self.arg_con.command_list:
                if com['command'] in ['-h', '-help']:
                    self.print_help()
                if com['command'] == '-f':
                    if os.path.isdir(com['item']):
                        found = True
                        self.search_dirs.append(com['item'])
                    else:
                        print('\n Error: ' + com['item'] + ' is not a valid directory')
            if not found and self.arg_con.is_command_present('-i') or self.arg_con.is_command_present('-m'):                
                print('\nNo valid search directory was given. Search present directory (' + self.main_dir + ') ?')
                answer = ''
                while answer not in ['y', 'Y', 'n', 'N']:
                    answer = input('(Y)es / (N)o  ')
                if answer in ['y', 'Y']:
                    self.search_dirs.append(self.main_dir)                    
                else:
                    self.terminate()
            if self.arg_con.is_command_present('-i'):
                getinfo = True
            if self.arg_con.is_command_present('-m'):
                generate = True
            if getinfo or generate:
                self.populate_file_list()

def main(args):
    gallery = GalleryGenerator(args)
    gallery.go() 

if __name__ == '__main__':
    main(sys.argv)