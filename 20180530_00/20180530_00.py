#!/usr/bin/env python
# -*- coding:utf-8 -*-


def function1(a,b,c):
	return a+b+c


print function1(4,5,6)


def function2(a,b,c=10):
	return a+b+c

print function2(4,5,6)
print function2(4,5)


def function3(*params):
	print type(params)
	print params

print function3(('a','b','c'))
print function3(['a','b','c'])
print function3(1,2,3)


def function4(**params):
	print type(params)
	print params

print function4(a=1,b=2,c=3)
print function4(a=(3,2,1),b=[1,2,3],c={'z':3,'y':2,'x':1})


argct = (1,2,3)
print function1(*argct)

argct = {'a':4,'b':5,'c':7}
print function1(**argct)

argct = {'a':4,'b':5}
print function2(**argct)



