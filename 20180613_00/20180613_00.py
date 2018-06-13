#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
import os
import shutil

print os.listdir('..')

f = open('aaa.txt','wb')
f.close()

time.sleep(3)

os.rename('aaa.txt','bbb.txt')

time.sleep(3)


shutil.copy('bbb.txt','ccc.txt')

print os.stat('bbb.txt')

time.sleep(2)
os.remove('bbb.txt')
os.remove('ccc.txt')



os.mkdir('abc')

time.sleep(5)

os.rmdir('abc')



