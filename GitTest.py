#!/usr/bin/env python
from subprocess import call, Popen

proc = Popen(['git','add','.'])

proc2 = Popen(['git','status'])

print('Proc 1:\n')
proc.communicate()
print('Proc 2:\n')
#proc2.communicate()