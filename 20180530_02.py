#!/usr/bin/env python
# -*- coding:utf-8 -*-



x1 = [1,3,5]
y1 = [9,12,13]

#表推導
L = [ x**2 for (x,y) in zip(x1,y1) if y > 10 ]
print L


def gen():
	a = 100
	yield a

	b = 100

	yield a+b

	yield 1000

for i in gen():
	print i




for line in open('20180530_01.py','r'):
	print line


