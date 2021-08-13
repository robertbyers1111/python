#!/usr/bin/python3
import sys

##-- [1] Basic file i/o..
#
#for arg in sys.argv[1:]:
#    try:
#        f = open(arg, 'r')
#    except IOError:
#        print('cannot open', arg)
#    else:
#        print(arg, 'has', len(f.readlines()), 'lines')
#        f.close()
#
##-- [2] Use 'with' for efficient cleanup..
#
#with open("myTextFile.txt") as f:
#    for line in f:
#        print('     ', line, end="")

#-- [3] For writing...

f = open('zoofile.txt', 'w')
f.write('this is a line\n')
f.write('this is a line\n')
f.write('this is a line\n')
f.close()
