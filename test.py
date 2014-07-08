#!/usr/bin/env python
import sys
import subprocess
import optparse

print('Hello World')

x = subprocess.call(['sublime', 'foo.txt'])
print('Error Code:')
print(x)
#subprocess.call(['cd','..','..'])

##

cmd1 = 'tail /var/log/messages'
cmd2 = 'dir'

cmds = [cmd1, cmd2]

def runCommands(cmds):
	count = 0
	for cmd in cmds:
		count +=1
		print("Running Command Number %s" % count)
		subprocess.call(cmd, shell=True)

#runCommands(cmds)