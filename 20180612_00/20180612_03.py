#!/usr/bin/env python
#-*- coding:utf-8 -*-



import time
print time.time()
print time.clock()

#time.sleep(3)

print 'sleep 3 seconds'

st = time.gmtime()
print st
st = time.localtime()
print st
print st.tm_year

s = time.mktime(st)
print s



import datetime

s = datetime.datetime(2018,6,12,20,22)
print s



t1 = datetime.datetime(2018,6,12,20,22,33,234)
t2 = datetime.datetime(2019,6,12,20,22,33)


delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks= 3)

print t1+delta1
print t2+delta2

print t1 > t2


print t2.strftime('%Y--%m==%d +%H*%M*%S')


format  = "output_%Y_%m_%d_%H%M%S.txt"
str = "output_2018_06_23_124534.txt"

t = datetime.datetime.strptime(str,format)

print t





