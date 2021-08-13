#!/usr/bin/python

import datetime

basename = 'bogus'
filetype = '.jpg'
NOW = datetime.datetime.now().strftime('%Y-%m%d-%H%M%S')

filename = basename+filetype
newname = basename + '-' + NOW + filetype

print '   filename:',filename
print '    newname:',newname

