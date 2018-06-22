#!/usr/bin/env python
#-*- coding:utf-8 -*-






import socket


SERVER = '127.0.0.1'
PORT = 8000

request = 'can you hear me ?'


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((SERVER,PORT))

s.sendall(request)

reply = s.recv(1024)

print 'reply is :',reply

s.close()









