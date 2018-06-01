#!/usr/bin/env python
# -*- coding:utf-8 -*-




re = iter(range(5))



try:
  for i in range(4):
    print re.next()

except Exception as StopIteration:
	print 'end come'
else:
	pass
finally:
	pass



try:
	print 'abc StopIteration'
	raise StopIteration
except StopIteration:
	print 'throw except'
finally:
	print 'finally'


try:
  print 'Throw exception'
  raise StopIteration	
except Exception as StopIteration:
	print 'test throw excetion'
else:
	pass
finally:
	pass



