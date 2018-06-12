#!/usr/bin/env python
# -*- coding:utf-8 -*-



print complex(3,9)




print ord('A'),chr(65),unichr(65),bool('abc')

print bin(56),hex(56),oct(56)

print list((1,2,3)),tuple([2,3,4]),slice(5,2,-1),dict(a=1,b='hello',c=[1,2,3],d=(2,3,4))



class Me(object):
	def test(self):
		print 'hello'

def new_test():
	print 'new hello'


me =Me()


print hasattr(me,'test'),getattr(me,'test')
setattr(me,'test',new_test)
me.test()
delattr(me,'test')
me.test()
print isinstance(me,Me)
print issubclass(Me,object)


print repr(me)

a = compile("print \'this is a compile function\'",'20180607_02.py','exec')
print a
eval(a)
exec(a)

eval("1+1")
exec('print \'aaa\'')


qqq = input("please input:")

print globals()
print locals()
