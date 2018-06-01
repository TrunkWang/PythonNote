#!/usr/bin/env python
# -*- coding:utf-8 -*-


a = [1,2,3,4,5,6,7,8,9]

m = 0

for i in a :
	m += i
print m


a = [1,2.3,4,5,'this is a string',(2,3,4,'this is a tuple string'),[4,5,6]]

for i in a :
	print i


print range(10)
print range(10,3)
print range(10,-3)

print (type(range(10)))

for i in range(3,10) :
	print i

i = 3
while i in range(3,10) :
	print i
	if i == 8 :
		break
	i = i + 1


def square_sum(a,b):
	c = a**2 + b**2
	return c

print square_sum(3,4)


def test_param1(a):
	a += 2
	return a

m = 2
m = test_param1(m)
print m
