#!/usr/bin/env python
# -*- coding:utf-8 -*-


print dir(1)

print '--------------------------------------------------'


s = 'abcdefghi'
s2 = 'jklmnopq'

print s+s2

print s.__add__(s2)

print (1.8).__mul__(2.0) , 1.8*2.0
print True.__or__(False) ,True or False ,True | False

print dir(str)


with open('20180531_03.py','r') as f:
	print f.closed
	f.read()

print f.closed



class guesthello():
	def __init__(self,text):
		self.text = text

	def __enter__(self):
		self.text  = 'hello i\'m ' + self.text
		return self

	def __exit__(self,exc_type,exc_value,traceback):
		print exc_type
		print exc_value
		print traceback
		self.text = self.text + ' !!!!'


with guesthello('tom') as n:
	print n.text

print n.text

