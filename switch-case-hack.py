#!/usr/bin/python3

# Here is the code that uses a dictionary to imitate a switch-case
# construct.

def myswitch(x): 
	return myswitch._system_dict.get(x, None) 

myswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

print(myswitch('default'))
print(myswitch('devices'))

#1-> None
#2-> 2
