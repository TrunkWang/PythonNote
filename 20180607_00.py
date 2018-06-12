#!/usr/bin/env python
# -*- coding:utf-8 -*-


list_str = 'Im an 81 man'
list_list = [1,2,'s','g',4,6,'s',5,0]
list_tuple = (1,2,3,0,'f','t','uh','f','sa')
#dit一般不遵循以下原則，放置在此用來對比
list_dict = {'key1':1,'Key2':2,'key3':3 ,'key4':0,'key5':'ad'}

print len(list_str),len(list_list),len(list_tuple),len(list_dict)

print min(list_str),min(list_list),min(list_tuple),min(list_dict)

print max(list_str),max(list_list),max(list_tuple),max(list_dict)

print all(list_str),all(list_list),all(list_tuple),all(list_dict)

print any(list_str),any(list_list),any(list_tuple),any(list_dict)



#print sum(list_list)

list_number = [1,2,3,4,5,6,7,8,9,0]
list_char = ['1','2','3','4']
tuple_number = (1,2,3,4,5,6,7,8,9)
tuple_char = ('1','2','3','4')

print sum(list_number)
#print sum(list_char)
print sum(tuple_number)
#print sum(tuple_char)


print list_number.count(2)
print list_number.index(2)

print list_char.count('3')
print list_char.index('3')


list_number.extend(list_char)
print list_number

list_number.append('abc')
print list_number

list_number.sort()
print list_number

list_number.reverse()
print list_number

list_number.pop()
print list_number

del list_number[9]
print list_number



s1 = 'I\'m an 30 age Programer , Ok Let\'s go'
s2 = 'Stupid Program Monkey'

print s1.count('a')
print s1.find('a')
print s1.index('Ok')
print s1.rfind('a')
print s1.rindex('Ok')

print s1.isalnum(),s2.isalnum()
print s1.isalpha(),s2.isalpha()
print s1.isdigit(),s2.isdigit()
print s1.istitle(),s2.istitle()
print s1.isspace(),s2.isspace()
print s1.islower(),s2.islower()
print s1.isupper(),s2.isupper()

print s1.split(' ',3),s1
print s2.strip('y'),s2
print s2.replace('Monke','Monkey'),s2
print s2.replace('Stupid','stupid').capitalize(),s2
print s1.lower(),s1
print s1.upper(),s1
print s1.swapcase(),s1
print s1.title(),s1

s3 = 'q\'r\'a'
print s3.title(),s3


print s1.center(50)
print s1.ljust(50)



















