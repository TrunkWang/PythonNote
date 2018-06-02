#!/usr/bin/env python
# -*- coding:utf-8 -*-

#closure


def function1():
	def in_fun(a):
		if a < 10 :
			return 1000
		else:
			return a
	return in_fun

print function1()

ff = function1()
print ff(3)
print ff(11)


def line_conf():
	b = 15
	def line(a):
		return 2*a+b
	return line

ff1 = line_conf()

print ff1(5)


print ff1.__closure__
print ff1.__closure__[0]
print ff1.__closure__[0].cell_contents





def linefun(a,b):
	def linex(x):
		return a*x+b
	return linex


linm = linefun(2,3)
linn = linefun(4,5)

print linm(3)
print linn(3)




