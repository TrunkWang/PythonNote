#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import getrefcount
import objgraph
# memery manager


a = 1
print id(a)
print hex(id(a))

a = 'abc'
print id(a)
print hex(id(a))


m = 'sshishishishi'
n = 'sshishishishi'
q = 'sshishishishi'


print id(m),id(n),id(q)

q = a
print id(m),id(n),id(q)


print getrefcount(a)
print getrefcount(m)
print getrefcount(n)
print getrefcount(q)



class fromeobj(object):
	def __init__(self,to_obj):
		self.to_obj = to_obj

b = [1,2,3,4,5]

a = fromeobj(b)

print a.to_obj
print id(a.to_obj)
print id(b)




x = [1,2,3,4]
y = [x,dict(key1=x)]
z = [y,(x,y)]

objgraph.show_refs([z],filename='ref_topo.png')


