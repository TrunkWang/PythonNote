#!/usr/bin/env python
#-*- coding:utf-8 -*-




import os.path

path = '/home/trunk/workdir/00-python_note_git/PythonNote/20180612_03.py'

print os.path.basename(path)
print os.path.dirname(path)

info = os.path.split(path)
print info

path2 = os.path.join('/','home','trunk','workdir','00-python_note_git','PythonNote','20180612_04.py')
print path2


pathlist = [path,path2]

print os.path.commonprefix(pathlist)


print os.path.exists(path)
print os.path.getsize(path)
print os.path.getatime(path)
print os.path.getmtime(path)
print os.path.isfile(path)
print os.path.isdir(path)



import glob

filel = glob.glob('/home/trunk/workdir/00-python_note_git/PythonNote/*.py')

for s in filel:
	print s




