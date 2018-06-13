#!/usr/bin/env python
#-*- coding:utf-8 -*-


import re

m = re.search('[a-z]','asdf2lkfajsdl4alskdflkj6laskdjf6')


print m.group(0)


n = re.match('[a-z]','asdf2lkfajsdl4alskdflkj6laskdjf6')

print n

o = re.sub('[0-9]','VVVVV','sdf2lkfajsdl4alskdflkj6laskdjf6')

print o


p = re.findall('[0-9]','sdf2lkfajsdl4alskdflkj6laskdjf6')

print p



regp = re.compile('[0-9]')

r = re.findall(regp,'sdf2lkfajsdl4alskdflkj6laskdjf6')

print r


respil = re.split('[0-9]','sdf2lkfajsdl4alskdflkj6laskdjf6')

print respil


s = re.search('output_(\d{4})','output_1986.txt')
print s.group(1)
print s.group(0)


t = re.search('output_(?P<year>\d{4})','output_1986.txt,output_1987.txt,output_1988.txt')
print t.group('year')
print t.group(1)
print t.group()



import calendar

y = re.search('_(?P<year>\d{4})','output_1981.10.21.txt')
m = re.search('\.(?P<month>\d{2})','output_1981.10.21.txt')
d = re.search('\.(?P<day>\d{2})\.t','output_1981.10.21.txt')


print y.group(1),m.group(1),d.group(1)

week_day = str(calendar.weekday(int(str(y.group(1))),int(str(m.group(1))),int(str(d.group(1)))) +1 )
print week_day

z = re.sub('_\d{d}',str(y.group(1)),'output_1981.10.21.txt')
print z
z = re.sub('\.','-',z)
print z

zf = 'output_' + str(y.group(1))+ '-' +str(m.group(1))+ '-' +str(d.group(1)) + '-' + str(week_day) +  '.txt'
print zf

ymd = re.search('\d{4}\.\d{2}\.\d{2}','output_1981.10.21.txt')
print ymd.group()
#print ymd.group(1)
#print ymd.group(2)
#print ymd.group(3)

