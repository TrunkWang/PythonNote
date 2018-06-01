#!/usr/bin/env python
# -*- coding:utf-8 -*-


class bird(object):
	feather = True

class chicken(bird):
	fly = False
	def __init__(self,a):
		self.age = a
	def getadult(self):
		if self.age > 1.0 :
			return True
		else:
			return False
	def __getattr__(self,name):
		if name == 'gogogo':
			if self.age > 10 :
				print 'flying flying'
				return 'sky'
			else:
				print 'running running'
				return 'land'
		else:
			raise AttributeError(name)
	adult = property(getadult)


summer3 = chicken(8)
summer4 = chicken(11)



print summer3.gogogo
print summer4.gogogo


summer = chicken(9)

print bird.__dict__
print chicken.__dict__
print summer.__dict__


print summer.__class__
print summer.__class__.__base__
print chicken.__base__


summer1 = chicken(2)

print summer1.adult

summer2 = chicken(0.5)
print summer2.adult



class num(object):
	def __init__(self,value):
		print 'init'
		self.val = value

	def getNeg(self):
		print 'get'
		return self.val

	def setNeg(self,value):
		print 'set'
		self.val = value

	def delNeg(self):
		print 'del'
		del self.val

	negv = property(getNeg,setNeg,delNeg,"i'm negative")



suumer  = num(9)
print suumer.val
print suumer.negv

print num.negv.__doc__

suumer.val = 10
print suumer.val

suumer.negv = 90
print suumer.val

del suumer.negv







