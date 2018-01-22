#!/usr/bin/env python

#  Hi wanderer, this __ is
#        _______    /°_>-<  Tiny Python Server
#    ___/ _____ \__/ /
#   <____/     \____/          a simple HTTP server by Miki - version 0.1

import http.server
import socketserver

PORT = 1337

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', PORT), Handler)
print('Tiny Phyton Server - listening on PORT : ', PORT)

if __name__ == "__main__":
    httpd.serve_forever()