#!/usr/bin/env python
# -*- coding:utf-8 -*-



import math

print math.e
print math.pi


print math.ceil(3.4)
print math.floor(3.4)

print math.pow(5,2)
print math.log(math.e)

print math.sqrt(4)



import random


print random.choice(range(10))
print random.sample(range(10),5)

l = [1,2,3,4,5,6,7]
random.shuffle(l)
print l

print random.random()
print random.uniform(5,6)



ln = ['abc','aaa','563','adcf','ry3f','23456']


random.shuffle(ln)
print ln


print random.sample(range(1,23),5)


s = ''

for i in range(8):
	s = s + str(random.sample(range(1,7),1)[0])

print s


