#!/usr/bin/env python
# -*- coding:utf-8 -*-



import multiprocessing as mul
import time


def proc1(pipe):
	print 'proc1 start'
	time.sleep(2)
	pipe.send('i\'m proc1,hello')
	print 'proc1',pipe.recv()

def proc2(pipe):
	print 'proc2 start'
	print 'proc2',pipe.recv()
	time.sleep(2)
	pipe.send('i\'m proc2,hello')
	print 'proc2 end'


pipe = mul.Pipe()


p1 = mul.Process(target = proc1,args=(pipe[0],))
p2 = mul.Process(target = proc2,args=(pipe[1],))

p1.start()
p2.start()


p1.join()
p2.join()




