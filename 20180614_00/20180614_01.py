#!/usr/bin/env python
# -*- coding:utf-8 -*-





import signal
print signal.SIGALRM
print signal.SIGCONT



def signal_handle(signum,frame):
	print 'I receied',signum


signal.signal(signal.SIGTSTP,signal_handle)
signal.pause()
print 'End of signal Demo'


def signal_handle_2(signum,frame):
	print 'Now it\'s the time'
	exit()

signal.signal(signal.SIGALRM,signal_handle_2)
signal.alarm(5)
while True:
	print 'not yet'



