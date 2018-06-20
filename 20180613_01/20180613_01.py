#!/usr/bin/env python
#-*-coding:utf-8 -*-


import pickle

class Bird(object):
	have_feather = True
	way_of_reproduction = 'egg'


summer = Bird()
picklestring = pickle.dumps(summer)

print picklestring



fn = 'a.pk1'
with open(fn,'w') as f:
	picklestr = pickle.dump(summer,f)



