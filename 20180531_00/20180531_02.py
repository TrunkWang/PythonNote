#!/usr/bin/env python
# -*- coding:utf-8 -*-



a = 5

b = a

a = a + 5


print a
print b


L1 = [1,2,3]
L2 = L1
L1 = 1

print L1,L2


L1 = [1,2,3]
L2 = L1
L1[0] = 10

print L1,L2 


m = 9

def func1(x):
	return x+1


n = func1(m)

print m,n


m = [5,6,7]
def func2(x):
	x[1] = 7

func2(m)

print m





