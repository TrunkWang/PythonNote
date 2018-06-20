#!/usr/bin/env python
#-*- coding:utf-8 -*-



import multiprocessing

def f(x):
	return x*3

def f2(x):
	print 'this is f2',x
	return 1000



pool = multiprocessing.Pool(5)

re =  pool.map(f,[1,2,3,4,5,6,7,8,9,10])
print pool.apply_async(f2,(111,)).get()
print re




