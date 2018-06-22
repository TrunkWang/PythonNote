#!/usr/bin/env python
#-*- coding:utf-8 -*-





import socket



HOST = '127.0.0.1'
PORT = 8000


text_connect = '''HTTP/1.0 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow,Python Server ! </p>
<IMG src = "test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type = "text" name="firstname"><br>
<input type = "submit" value = "Submit">
</form>
</html>
'''

f = open('test.jpg','rb')

pic_content = '''HTTP/1.0 200 OK
Content-Type: image/jpg

'''

pic_content = pic_content + f.read()
f.close()



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(3)


while True:
	conn,addr = s.accept()

	rett = conn.recv(1024)

	if len(rett) == 0:
		conn.close()
		continue
	#print rett

	method = rett.split(' ')[0]
	src = rett.split(' ')[1]

	if method == 'GET':
		print 'GET'
		if src == '/test.jpg':
			print 'image'
			content = pic_content
		else:
			print 'text'
			content = text_connect
		conn.sendall(content)
	elif method == 'POST':
		print 'POST'
		print rett
		form = rett.split('\r\n')
		idx = form.index('')
		entry = form[idx:]

		value = entry[-1].split('=')[-1]
		conn.sendall(text_connect + '\n <p>' + value + '</p>')


	conn.close()










