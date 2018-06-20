#!/usr/bin/env python
#-*- conding:utf-8 -*-


import multiprocessing

def f(n,a):
	n.value = 3.14
	a[0] = 5

num = multiprocessing.Value('d',0.0)
arr = multiprocessing.Array('i',range(10))

p = multiprocessing.Process(target=f,args=(num,arr))
p.start()
p.join()


print num.value
print arr[:]





def fn(x,arr,l):
	x.value = 3.14
	arr[0] = 5
	l.append('Hello')


server = multiprocessing.Manager()

x = server.Value('d',0.0)
arr = server.Array('i',range(10))
l = server.list()


proc = multiprocessing.Process(target = fn,args=(x,arr,l))
proc.start()
proc.join()


print x.value
print arr
print l
