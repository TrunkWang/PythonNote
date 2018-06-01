#!/usr/bin/env python
# -*- coding:utf-8 -*-




fun = lambda x : x + 3

print fun(9)



def funclamb(f,a,b):
	print type(f)
	print f(a,b)
	return True


print funclamb((lambda x,y : x*10+y),1,2)

print map((lambda x : x*10 ),[1,4,5])



def filterfun(x):
	if x > 100 :
		return True
	else:
		return False


print filter(filterfun,[1,2,3,4,5,100,200,300,400])



def reducefun(x,y):
	if x > y :
		return x
	else:
		return y

print reduce(reducefun,[1,2,3,4,5,6,7,8])

