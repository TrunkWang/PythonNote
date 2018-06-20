#!/usr/bin/env python
# -*- coding:utf-8-*-



import threading
import time
import os


def coChore():
	time.sleep(0.5)



class BootThread(threading.Thread):
	def __init__(self,tid,monitor):
		self.tid = tid
		self.monitor = monitor
		threading.Thread.__init__(self)

	def run(self):
		while True:

			monitor['lock'].acquire()

			if monitor['ticks'] != 0 :
				monitor['ticks'] = monitor['ticks'] - 1
				print 'self tid ' , self.tid , 'ticks ' ,monitor['ticks']
				coChore()
			else:
				print 'self tid ' ,self.tid ,'finish'
				os._exit(0)
			monitor['lock'].release()
			coChore()




lock = threading.Lock()

monitor = {'ticks':100,'lock':lock}


for k in range(10):
	newclassthread = BootThread(k,monitor)
	newclassthread.start()


