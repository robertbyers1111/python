#!/usr/bin/python

import datetime, os, re, shutil, sys
from subprocess import Popen, PIPE

destdir = '/home/bbyers/deleteme_now/'

#-- Get filename from command line

if len(sys.argv[1:]) != 1:
  print '\nUSAGE:',os.path.basename(__file__),'file\n'
  sys.exit(-1)

filename = sys.argv[1]

#-- Make sure file exists

if not os.path.isfile(filename):
  print '\nERROR:',filename,'does not exist, or is not a file\n'
  sys.exit(-1)

print '\n  Original file:',filename

#-- Parse filename into basename and extension

matches = re.search('(\S+)(\.\S+)', filename)

if not matches:
  print '\nCannot parse filename',filename,'\n'
  sys.exit(-1)

basename = matches.groups()[0]
extension = matches.groups()[1]

#   +------------------+
#---| RENAME ORIG FILE |---
#   +------------------+

#-- RENAME TO A TEMP NAME (thus making room for the incoming svn update)

NOW = datetime.datetime.now().strftime('-%Y-%m%d-%H%M%S')
bbfilename1 = basename + '-zbb' + NOW + extension
print '  temp location:',bbfilename1

#-- Make sure destination doesn't already exist

if os.path.exists(bbfilename1):
  print '\nERROR:',bbfilename1,'already exists'
  sys.exit(-1)

#-- RENAME ORIG to a temp name

os.rename(filename, bbfilename1)

#-- Make sure original file is gone and temp file does exist

if os.path.exists(filename):
  print '\nERROR: Original file',filename,'still exists after attempting to rename it to',bbfilename1
  sys.exit(-1)

if not os.path.exists(bbfilename1):
  print '\nERROR: Renamed filename',bbfilename1,'not found!'
  sys.exit(-1)

print '        Renamed!'

#   +---------------------------------------+
#---| COPY ORIG TO file-compare DESTINATION |---
#   +---------------------------------------+

bbfilename2 = destdir + bbfilename1
print ' FC Destination:',bbfilename2

#-- Make sure destination doesn't already exist

if os.path.exists(bbfilename2):
  print '\nERROR:',bbfilename2,'already exists'
  sys.exit(-1)

#-- Copy original file to its temp destination

shutil.copy2(bbfilename1, bbfilename2)

#-- Make sure temp file still exists and also exists in the file-compare destination

if not os.path.exists(bbfilename1):
  print '\nERROR: Original temp file',bbfilename1,'is GONE!'
  sys.exit(-1)

if not os.path.exists(bbfilename2):
  print '\nERROR: Copied filename',bbfilename2,'not found!'
  sys.exit(-1)

print '        Copied!'

#   +----------------------------------+
#---| RETRIEVE LATEST VERSION FROM SVN |---
#   +----------------------------------+

cmd = 'svn update ' + filename

print '\nRETRIEVING SVN VERSION OF',filename,'..'
print '  %',cmd

p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)

for line in p.stdout:
    print '  ',line.rstrip()

out, err = p.communicate()

#-- Make sure the file was successfully retrieved

if not os.path.exists(filename):
  print '\nERROR: Original file',filename,'not successfully retrieved from svn'
  sys.exit(-1)

#-- Rename svn's version

svnfilename1 = basename + '-svn' + NOW + extension

if os.path.exists(svnfilename1):
  print '\nERROR:',svnfilename1,'already exists'
  sys.exit(-1)

os.rename(filename, svnfilename1)

if os.path.exists(filename):
  print '\nERROR: Original file',filename,'still exists after attempting to rename it to',svnfilename1
  sys.exit(-1)

if not os.path.exists(svnfilename1):
  print '\nERROR: Renamed filename',svnfilename1,'not found!'
  sys.exit(-1)

print '        Renamed!'

#-- Move SVN's version to the file-compare destination

svnfilename2 = destdir + svnfilename1
print ' FC Destination:',svnfilename2

if os.path.exists(svnfilename2):
  print '\nERROR:',svnfilename2,'already exists'
  sys.exit(-1)

shutil.move(svnfilename1, svnfilename2)

#-- Make sure the move completed successfully

if os.path.exists(svnfilename1):
  print '\nERROR: Original temp file',svnfilename1,'still exists'
  sys.exit(-1)

if not os.path.exists(svnfilename2):
  print '\nERROR: Destination filename',svnfilename2,'not found!'
  sys.exit(-1)

print '        MOVED!'

print '\nmv',bbfilename1,filename,'\n'

#   +-----------------------+
#---| RESTORE ORIGINAL FILE |---
#   +-----------------------+

print ' Restoring original file'

if os.path.exists(filename):
  print '\nERROR:',filename,'already exists'
  sys.exit(-1)

if not os.path.exists(bbfilename1):
  print '\nERROR:',bbfilename1,'not exist'
  sys.exit(-1)

shutil.move(bbfilename1, filename)

#-- Make sure the move completed successfully

if os.path.exists(bbfilename1):
  print '\nERROR: Original temp file',bbfilename1,'still exists'
  sys.exit(-1)

if not os.path.exists(filename):
  print '\nERROR: Destination filename',filename,'not found!'
  sys.exit(-1)

print '        MOVED!'

#   +---------------------+
#---| That is all for now |---
#   +---------------------+

print '\nFiles are ready for comparison..'
print '    ',bbfilename2
print '    ',svnfilename2
print ''

