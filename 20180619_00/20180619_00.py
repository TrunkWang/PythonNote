#!/usr/bin/env python
# -*- coding:utf-8 -*-




import multiprocessing as mul
import subprocess

def downloadurl(x):
	print x
	filename = x + '.txt'
	subprocess.call(['curl',x,])
	return 0



pool = mul.Pool(5)
rel  = pool.map(downloadurl,['www.sina.com.cn','www.163.com','www.iciba.com','www.cnblogs.com','www.qq.com','www.douban.com',])


print ret







