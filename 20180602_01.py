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


#decorator with params

def pre_str(pre=''):
	def decorator(F):
		def new_f(a,b):
			print pre,a,b
			return F(a,b)
		return new_f
	return decorator

@pre_str("7777")
def aaa_sum(a,b):
	return a+b

@pre_str("8888")
def aaa_diff(a,b):
	return a-b

print aaa_sum(4,5)
print aaa_diff(5,4)



#decorator calss


def decoratorclass(aClass):
	class new_class:
		def __init__(self,age):
			self.totaldisplay = 0
			self.wrapper = aClass(age)
		def display(self):
			print 'total display',self.totaldisplay
			self.totaldisplay += 1
			self.wrapper.display()
	return new_class


@decoratorclass
class newnew_class:
	def __init__(self,age):
		self.age = age
	def display(self):
		print 'newnew_class display'


niuniu = newnew_class(9);


for i in range(5):
	niuniu.display()











