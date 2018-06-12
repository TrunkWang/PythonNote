#!/usr/bin/env python
#-*- coding:utf-8 -*-


from test_lib import test_lib_t2

print test_lib_t2(3,4)


import test_lib

print test_lib.test_lib_t(3,4)

import test_lib as abc
print abc.test_lib_t2(3,4)



import inspect
print inspect.getargspec(abc.test_lib_t2)




s = [1,2,3,4,5,6]
print hasattr(s,'append')
print hasattr(s,'pop')


print s.__class__.__base__
print s.__class__.__name__
print list.__base__


print '您好'



print 0b1110
print 0o10
print 0x20


import sys
print sys.path


