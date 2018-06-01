#!/usr/bin/env python
# -*- coding:utf-8 -*-




sl = [9,8,7,6,8]
print len(sl)

print min(sl),max(sl),all(sl),any(sl)

print sum(sl),sl.count(8),sl.index(8)


sl2 = [1,2,3,4]

sl.extend(sl2)
print sl

sl.append(0)
print sl

sl.sort()
print sl

sl.pop()
print sl

del sl[3]
print sl

strl = 'hello world hello everyone'
substrl = 'hello'

print strl.count(substrl)
print strl.find(substrl),strl.rfind(substrl)
print strl.index(substrl),strl.rindex(substrl)

print strl.isalnum(),strl.isalpha(),strl.isdigit()

print strl.istitle(),strl.isspace(),strl.islower(),strl.isupper()

print strl.split(' ',2)
print strl.rsplit(' ',2)

print strl

mm = '+'
print mm.join(strl)
print strl

print strl.strip('home')

print strl.replace('hello','some')

print strl.capitalize()

print strl.lower()

print strl.upper()

print strl.swapcase()

print strl.title()

print strl.center(50)

print strl.ljust(50)

print strl.rjust(50)






