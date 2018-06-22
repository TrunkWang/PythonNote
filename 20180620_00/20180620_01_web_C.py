#!/usr/bin/env python
#-*- coding:utf-8 -*-


import SocketServer


HOST = '127.0.0.1'
PORT = 8000



text_connect = '''HTTP/1.x 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
<title>WOW</title>
</head>

<p>Wow,Python Server </p>
<img src='test.jpg' alt = 'testjpj'>

</html>
'''

f = open('test.jpg','rb')

pic_content = '''HTTP/1.x 200 OK
Content-Type: image/jpg

'''

pic_content = pic_content + f.read()

f.close()

class MyTCPHandle(SocketServer.BaseRequestHandler):
	def handle(self):
		rett = self.request.recv(1024)
		method = rett.split(' ')[0]
		src = rett.split(' ')[1]
		print '----------------------------------'
		print rett
		print method
		print src
		print '----------------------------------'
		if method == 'GET':
			if src == '/test.jpg':
				content = pic_content
				print content
			else:
				content = text_connect
			self.request.sendall(content)

		elif method == 'POST':
			form = rett.split('\r\n')
			idx = form.index('')
			entry = form[idx:]
			print entry

			value = entry[-1].split('=')[-1]
			self.request.sendall(text_connect + '\n<p>' + value + '</p>')




server = SocketServer.TCPServer((HOST,PORT),MyTCPHandle)
server.serve_forever()








