#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
import time
import os



def coChore(a):
	if a == 10:
		print 'that a'
	time.sleep(0.5)


def booth(tid):
	global i
	global lock

	while True:
		lock.acquire()

		if i != 0 :
			i = i -1
			print 'tid ',tid,'ticks',i
			coChore(1)
		else:
			print 'thread id ',tid
			os._exit(0)
		lock.release()
		coChore(10)






i = 100
lock = threading.Lock()


for k in range(10):
	new_thread = threading.Thread(target = booth,args=(k,))
	new_thread.start()


