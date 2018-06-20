#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
import subprocess

out = subprocess.call(['ls','-l'])
print out
out1 = subprocess.call(['ls','-a'])
print out1


out3 = subprocess.call('ls -al',shell=True)
if out3 == 0:
	print '^^success'
else:
	print '^^error'

out4 = subprocess.call('cd .',shell=True)

if out4 == 0:
	print '^^success'
else:
	print '^^error'




child = subprocess.Popen(['ping','-c','5','192.168.3.102'])
print 'parent process'

child2 = subprocess.Popen(['ping','-c','10','192.168.3.102'])
print child.poll()
child2.wait()
print 'parent process2'



child3 = subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE)
child4 = subprocess.Popen(['wc'],stdin = child3.stdout,stdout =  subprocess.PIPE)
out = child4.communicate()
print out


child5 = subprocess.Popen(['cat'],stdin = subprocess.PIPE)
print child5.communicate('vamei')

