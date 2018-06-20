#!/usr/bin/env python
#-*- coding:utf-8 -*-




import cPickle as pickle


class Bird(object):
	have_feather = True
	way_of_reproduction = 'egg'

fn =  'a.pk1'
with open(fn,'r') as f:
	summer = pickle.load(f)


print summer.way_of_reproduction




