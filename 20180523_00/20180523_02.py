#!/usr/bin/env python
# -*- coding:utf-8 -*-



class bird(object):
	def __init__(self,more_words):
		print 'hello ' ,more_words

	def setname(self,na):
		self.name = na

	def move(self,x,y):
		self.position = [0,0]
		self.position[0] = x
		self.position[1] = y
		print 'name',self.name,'move',self.position




class chicken(bird):
	possible_in_KFC = True




al = bird('new bird')

al.setname('abc')


al.move(9,9)

print al.name

print al.position


cl = chicken('new chicken')

cl.setname('chicken')

print cl.name

cl.move(10,10)

print cl.possible_in_KFC

