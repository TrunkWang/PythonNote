#!/usr/bin/env python
#-*- coding:utf-8 -*-





for i in iter([2,4,5,6]):
	print i



from itertools import *


for a in count(5,2):
	print a
	if a > 100 :
		break


i = 0
for b in cycle('abc'):
	print b
	i = i + 1
	if i > 200:
		break




for c in repeat(10,6):
	print c




rlt = imap(pow,[1,2,3],[1,2,3])

for num in rlt:
	print num


lr = starmap(pow,[(1,1),(2,2),(3,3)])
for num in lr:
	print num


abc = ifilter(lambda x:x>5,[2,3,4,5,6,7,8])
bcd = ifilterfalse(lambda x:x>5,[2,3,4,5,6,7,8])
for num in abc:
	print num
for num in bcd:
	print num


mnp = takewhile(lambda x:x>5,[2,3,4,5,6,7,8])
npq = dropwhile(lambda x:x>5,[2,3,4,5,6,7,8])
print '---'
for num in mnp:
	print num
print '---'
for num in npq:
	print num

print '++++++'
n = chain([1,2,3],[4,5,7])

for i in n:
	print i

print '++++++'
for m,n in product('abc',[1,2]):
	print m,n

print '++++++'
for i in permutations('abc',2):
    print i	


print "++++++"
for i in combinations('abc',2):
	print i

print "++++++"
for i in combinations_with_replacement('abc',2):
	print i





def height_class(h):
	if h > 180:
		return 'tall'
	elif h < 160:
		return 'short'
	else:
		return 'middle'

friends = [191,158,159,165,170,177,181,182,190]
friends = sorted(friends,key= height_class)

print friends

for m,n in groupby(friends,key = height_class):
	print m
	print list(n)



for i in compress('ABCD',[1,1,1,0]):
	print i







