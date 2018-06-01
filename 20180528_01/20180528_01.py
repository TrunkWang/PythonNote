#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sub
from sub import customsubsuper

import moduldir.modulpart



print sub.customsub(1,3)

print customsubsuper(1,2,3)


print moduldir.modulpart.printlist(100)


from moduldir.modulpart import printlistbig

print printlistbig(70)
