#!/usr/bin/env python
# -*- coding:utf-8 -*-

#print dir(list)
#print help(list)

print [1,2,3] + [2,3,5]


class superlist(list):
	def __sub__(self,other):
		a = self[:]
		b = other[:]

		while len(b) > 0 :
			m = b.pop()
			if m in a:
				a.remove(m)
		return a



print superlist([2,3,4,5,6]) - superlist([4,6,7])
