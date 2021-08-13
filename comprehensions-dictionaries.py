#!/usr/bin/python3

# Useful dictionary comprehension template..
#
# dict_variable = {key:value for (key,value) in dictonary.items()}

# Example..

n=15
dict1 = {k:v for (k,v) in enumerate(range(n))}
dict2 = {k:v*2 for (k,v) in dict1.items()}
dict3 = {k:v*3 for (k,v) in dict1.items()}
dict4 = {k:v*4 for (k,v) in dict1.items()}
dict5 = {k:v*5 for (k,v) in dict1.items()}
dict6 = {k:v*6 for (k,v) in dict1.items()}
dict7 = {k:v*7 for (k,v) in dict1.items()}
dict8 = {k:v*8 for (k,v) in dict1.items()}
dict9 = {k:v*9 for (k,v) in dict1.items()}
dict10 = {k:v*10 for (k,v) in dict1.items()}
dict11 = {k:v*11 for (k,v) in dict1.items()}
dict12 = {k:v*12 for (k,v) in dict1.items()}

for k in dict1.keys():
  print('{:3d} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d}'.format(
    dict1[k],dict2[k],dict3[k],dict4[k],dict5[k],dict6[k],
    dict7[k], dict8[k], dict9[k], dict10[k], dict11[k], dict12[k] ))

