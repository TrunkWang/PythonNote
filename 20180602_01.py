#!/usr/bin/env python
# -*- coding:utf-8 -*-

#decorator




def decorator(F):
	def new_f(a,b):
		print 'input',a,b
		return F(a,b)
	return new_f


@decorator
def aa_sum(a,b):
	return a*a +b*b

@decorator
def aa_diff(a,b):
	return a*a-b*b


print aa_sum(3,4)
print aa_diff(4,3)



















