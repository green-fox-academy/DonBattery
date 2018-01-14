#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from arger import Argument_Compiler
from filer import File_Controller

class GalleryGenerator(object):
    
    def __init__(self, arglist):
        
        # Allowed file formats
        self.extensions = ['.jpg', 'jpeg', '.png', '.bmp', '.gif', '.pcx']

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

        self.gallery_dir = 'gallery'

        # This list will contain the URL-s to image files found_dir in search directories
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

    # Fill the file_list with image URLs found_dir in search directories
    def populate_file_list(self):
        new_list = []
        if self.arg_con.is_command_present('-s'):
            for sdir in self.search_dirs:
                for root, dirs, files in os.walk(sdir):
                    for file in files:
                        if len(file) > 3:
                            if file[-4:] in self.extensions:
                                file_list_element = os.path.abspath(os.path.join(root, file))
                                #print('Picture Found :', file_list_element)
                                new_list.append(file_list_element)
        self.file_list = new_list

    # Generate HTML file based on file_list
    def make_html(self, title = 'Image Gallery', mode = 'lot'):
        html_file = File_Controller(os.path.join(self.main_dir, 'gallery'), 'index.html')
        if not html_file.test_file('C'):
            print('\n Error : Cannot create HTML')
            print(html_file.get_errors())
            self.terminate()
        else:
            if mode == 'lot':

                html_data = [
                '<!DOCTYPE html>\n', 
                '<html lang="en">\n',
                '<head>\n',
                '<meta charset="UTF-8">\n',
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
                '<meta http-equiv="X-UA-Compatible" content="ie=edge">\n',
                #'<link rel="stylesheet" href="' + self.css_filename + '">',
                '<title>' + title + '</title>\n',
                '</head>\n',
                '<body>\n',
                '\n']

                for file in self.file_list:
                    new_row = '<div class="image"><img src="' + file + '" alt=""></div>'
                    html_data.append(new_row + '\n')

                html_data += ['</body>','</html>']

            if not html_file.multiple_line_writer(html_data):
                print('\n Error : Cannot create HTML')
                print(html_file.get_errors())
                self.terminate()


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
            print(self.arg_con.command_list)
            found_dir = False
            found_gallery_dir = False
            generate = False
            getinfo = False
            # Go through the commans list and execute them
            for com in self.arg_con.command_list:
                
                if com['command'] in ['-h', '-help']:
                    self.print_help()
                
                if com['command'] == '-f':
                    if os.path.isdir(com['item']):
                        found_dir = True
                        self.search_dirs.append(com['item'])
                    else:
                        print('\n Error: ' + com['item'] + ' is not a valid directory')
                
                if com['command'] == '-g':
                    self.gallery_dir = com['item']

            if (not found_dir) and (self.arg_con.is_command_present('-i') or self.arg_con.is_command_present('-m')):                
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
#                if len(self.gallery_dir) > 0:
 #                   if 

            if getinfo or generate:
                self.populate_file_list()
                if generate:
                    if len(self.file_list) == 0:
                        Print('\n Error: no picture to work with...')
                    else:                        
                        self.make_html()

def main(args):
    gallery = GalleryGenerator(args)
    gallery.go() 

if __name__ == '__main__':
    main(sys.argv)