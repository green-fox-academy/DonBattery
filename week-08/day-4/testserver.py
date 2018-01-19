#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from filer import File_Controller
from sys import argv
from sys import exit as abandonship
import json

my_html_file = File_Controller('', 'jsoner.html')
my_html_data = []

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print('GET ',end='')
        self._set_headers()
        for line in my_html_data:
            self.wfile.write(line.encode("utf-8"))

    def do_HEAD(self):
        self._set_headers()
           
    def do_POST(self):
        self._set_headers()
        self.wfile.write("posted".encode("utf-8")) 
        
def run(server_class=HTTPServer, handler_class=S, html_file='', port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

def terminate_server(msg = 'exiting...'):
    print('\n' + msg)
    abandonship()

if __name__ == "__main__":
    if not my_html_file.test_file():
        print('\nCannot load HTML')
        print('\n', my_html_file.get_errors())
        terminate_server()
    else:
        my_html_data = my_html_file.file_as_lines
        if len(argv) == 2:
            run(html_file=my_html_file, port=int(argv[1]))
        else:
            run(html_file=my_html_file)