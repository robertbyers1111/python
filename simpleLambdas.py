#!/usr/bin/python3

# Use a dictionary to store an expression using a lambda..

stdcalc = {
	'sum': lambda x, y: x + y,
	'subtract': lambda x, y: x - y
}

print(stdcalc['sum'](9,3))
print(stdcalc['subtract'](9,3))

#1-> 12
#2-> 6
