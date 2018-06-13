#!/usr/bin/env python
# -*- coding:utf-8 -*-


dictt = {'tom':11,'sam':37,'lily':100}

print dictt['tom']

print type(dictt)


dictt['tom'] = 40

print dictt['tom']

newdict = {}

newdict['jery'] = 90

print newdict


for key in dictt:
	print dictt[key]

print dictt.keys()
print dictt.values()

