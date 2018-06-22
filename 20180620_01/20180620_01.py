#!/usr/bin/env python
#-*-coding:utf-8 -*-



import BaseHTTPServer
import CGIHTTPServer


HOST = '127.0.0.1'
PORT = 8000


server = BaseHTTPServer.HTTPServer((HOST,PORT),CGIHTTPServer.CGIHTTPRequestHandler)
server.serve_forever()





