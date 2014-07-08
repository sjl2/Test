#!/usr/bin/env python
from subprocess import Popen, PIPE

arg1 = ['touch','TestingGitTest2.txt']

arg2 = ['git','add','TestingGitTest2.txt']

arg2ish = ['git','add','GitTest.py']

arg3 = ['git','status']

def SysCommand(args,**kwargs):
	#kwargs.setdefault('stdout', PIPE)
	print(args)
	proc = Popen(args)#, kwargs)
	out, err = proc.communicate()
	proc.wait()
	return out

print(SysCommand(arg1))
print(SysCommand(arg2))
print(SysCommand(arg2ish))
print(SysCommand(arg3))

