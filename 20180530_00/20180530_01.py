#!/usr/bin/env python
# -*- coding:utf-8 -*-



ta = [1,2,3]
tb = [9,8,7]


zipped = zip(ta,tb)
print zipped

na,nb = zip(*zipped)
print na,nb



strs = 'abcdefghijklmnopqrstuvwxyz'

for (index,enu) in enumerate(strs):
	print index,enu




for i in range(0,100,5):
	print i
