#!/usr/bin/env python
# -*- coding:utf-8 -*-




import os

print os.uname()

print os.getuid()
print os.getpid()




import threading
import multiprocessing

def worker(sign,lock):
	lock.acquire()
	print sign,'---',os.getpid()
	lock.release()

print 'main--',os.getpid()

record = []
lock = threading.Lock()
for i in range(5):
	thread = threading.Thread(target = worker,args=('thread',lock))
	thread.start()
	record.append(thread)


for thread in record:
	thread.join()

print 'all thread exit'




record = []
lock = multiprocessing.Lock()
for i in range(5):
	process = multiprocessing.Process(target = worker,args=('thread',lock))
	process.start()
	record.append(process)


for process in record:
	process.join()

print 'all process exit'

