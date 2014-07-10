#!/usr/bin/env python
from subprocess import Popen, PIPE, call


origin = 'C:\SourceControl\Test.git'
branch = 'master'

arg1 = ['touch','TestingGitTest2.txt']

arg2 = ['git','add','TestingGitTest2.txt']

arg2ish = ['git','add','GitTest.py']

arg3 = ['git','status']

arg4 = ['git','push', origin, branch]

arg5 = ['touch', 'deleteme.txt']

args = [arg1,arg2,arg2ish,arg3,arg4]

'''
def SysCommand(args,**kwargs):
	kwargs.setdefault('stdout', PIPE)
	proc = Popen(args,**kwargs)#,stdout=PIPE,stderr=PIPE)#, kwargs)
	out, err = proc.communicate()
	proc.wait()
	code = proc.returncode
	return out
''' 
class SysCommand:
	def __init__(self,args,**kwargs):
		self.args = args
		kwargs.setdefault('stdout',PIPE)
		proc = Popen(args,**kwargs)
		self.out, self.err = proc.communicate()
		proc.wait()
		self.code = proc.returncode


print(SysCommand(['git','commit']).out)

for a in args:
	print(SysCommand(a).out)

print(SysCommand(arg5,cwd='InnerTest').out)