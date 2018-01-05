# Cascading Style Pythons

# gif -> pil -> html, css

# kek

from filecontroller import File_Controller
import os.path 
from random import randint

screen_size = screen_width, screen_height = 10, 10

class Box_array(object):
    def __init__(self, size):
        self.size = self.width, self.height = size

class Cspys(object):
    def __init__(self, size, file_name, title):
        self.title = title
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.page_dir = os.path.join(self.main_dir, "page")
        self.css_filename = file_name + ".css"
        self.html_filename = file_name + ".html"
        self.size = self.width, self.height = size
        self.html_file = File_Controller(self.page_dir, self.html_filename)
        self.css_file = File_Controller(self.page_dir, self.css_filename)
        self.html_data = []
        self.css_data = []
        self.array = Box_array(self.size)
        self.css_file.test_file('C')
        self.html_file.test_file('C')

    def generate_html_data(self):

        self.html_data = [
            '<!DOCTYPE html>', 
            '<html lang="en">',
            '<head>',
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<meta http-equiv="X-UA-Compatible" content="ie=edge">',
            '<link rel="stylesheet" href="' + self.css_filename + '">',
            '<title>' + self.title + '</title>',
            '</head>',
            '<body>',
            '\n']

        for row in range(self.height):
            new_row = ''
            for col in range(self.width):
                new_row += '<div class="' + 'row' + str(row) + ' ' + 'col' + str(col) + '"></div>'
            self.html_data.append(new_row + '\n')

        self.html_data += ['</body>','</html>']

        self.html_file.multiple_line_writer(self.html_data)

    def generate_css_data(self):

        self.css_data = ['* {box-sizing: border-box;margin: 0px;padding: 0px;position: absolute;height: 100%; width: 100%} \n']

        for row in range(self.height):
            new_row = ''
            for col in range(self.width):
                color1 = str(randint(0,255))
                color2 = str(randint(0,255))
                color3 = str(randint(0,255))
                colorset = color1 + ', ' + color2 + ', ' + color3
                new_row += '.row' + str(row) + '.col' + str(col) + '{left: ' + str(100 // self.width * col) + '%;top :' + str(100 // self.height * row) + '%; height: ' + str(100 // self.height) + '%; width: ' + str(100 // self.width) + '%; background : rgb(' + colorset + ');} \n'
            self.css_data.append(new_row)
        self.css_file.multiple_line_writer(self.css_data)

app = Cspys(screen_size, "test2", "Cascading Style PythonS")

app.generate_html_data()

app.generate_css_data()
    