import re

# https://pymotw.com/2/re/

#--------------------------------------------------------------------------------
#
# re.match() only matches from start of string, re.search() searches anywhere in the string
#
#--------------------------------------------------------------------------------

lines = """
-rwxr-xr-x 1 bbyers     224473 2015-07-22 18:21:35 acliConnection.itcl*
-rw-r--r-- 1 bbyers      23142 2015-08-06 15:36:56 dhcpHost.itcl
-rwxr-xr-x 1 bbyers      17084 2015-09-09 08:26:46 linuxHost.itcl*
-rwxr-xr-x 1 bbyers      23694 2015-09-09 13:32:03 interfaceProcs.tcl*
-rwxr-xr-x 1 bbyers     145315 2015-09-10 16:32:05 acliv1_0.itcl*
-rw-r--r-- 1 root        17778 2015-10-06 15:29:14 tclIndex
2015-09-06 15:29:14 tclIndex 2015-09-06 15:29:14 tclIndex 2015-09-06 15:29:14 tclIndex 2015-09-06 15:29:14 tclIndex 2015-09-06 15:29:14 tclIndex 2015-09-06 15:29:14 tclIndex
"""

#--------------------------------------------------------------------------------
#
#--- Basic re.search() (A)

if re.search( ':\s*$' , 'abc :' ):
    print(f"YAY! {line} ends in a colon!")

#--------------------------------------------------------------------------------
#
#--- Basic re.search() (B)

print '\n====== re.search()..'

pattern = '2015-09-\d{2}\s+\d{2}:\d{2}:\d{2}\s+'

for line in lines.split('\n'):
  searched = re.search(pattern, line)
  if searched:
    s = searched.start()
    e = searched.end()
    basename = line[s:e]
    print '\n',line
    print '     MATCH FOUND!'
    print '        COLUMN RANGE:',s,'-',e
    print '       MATCHING TEXT:',basename
    print '     MATCHED PATTERN:',searched.re.pattern
    print '      MATCHED STRING:',searched.string

#--------------------------------------------------------------------------------
#
#--- Compiled regex

print '\n====== compiled regex..'

reTimestamp = re.compile('.*\s+20\d\d-09-\d\d\s+\d\d:\d\d:\d\d\s+.*')

for line in lines.split('\n'):
  if reTimestamp.match(line):
    print line

#--------------------------------------------------------------------------------
#
#--- findall()

print '\n====== findall()..'

pattern = '\S+Host'

for line in lines.split('\n'):
  for match in re.findall(pattern,line):
    print '\n',line
    print '     MATCH FOUND!'
    print '     MATCHING TEXT:',match

#--------------------------------------------------------------------------------
#
#--- finditer()

print '\n====== finditer()..'

pattern = '\S+Host'
print 'SEARCH PATTERN:',pattern

for line in lines.split('\n'):
  for match in re.finditer(pattern,line):
    s = match.start()
    e = match.end()
    basename = line[s:e]
    print '\n',line
    print '     MATCH FOUND!'
    print '     COLUMN RANGE:',s,'-',e
    print '     MATCHING TEXT:',basename

#--------------------------------------------------------------------------------
#
#--- GROUPS

print '\n====== GROUPS..'

pattern = '^(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s+(20\d\d-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s*$'

print 'SEARCH PATTERN:',pattern

for line in lines.split('\n'):
  for match in re.finditer(pattern,line):
    s = match.start()
    e = match.end()
    basename = line[s:e]
    print '\n',line
    print '     GROUPS FOUND!'

    #-- Access each group directly ..

    print '         group(3):',match.group(3),'(via direct access)'
    print '         group(4):',match.group(4),'(via direct access)'

    #-- Iterate through all groups ..

    i=0
    for group in match.groups():
      i=i+1
      print '          group',i,': ',group

#--------------------------------------------------------------------------------
#
#--- NAMED GROUPS

print '\n====== NAMED GROUPS..'

pattern = '^(?P<perms>\S+)\s+(?P<inodes>\d+)\s+(?P<uname>\S+)\s+(?P<size>\d+)\s+(?P<timestamp>20\d\d-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(?P<filename>\S+)\s*$'

print 'SEARCH PATTERN:',pattern

for line in lines.split('\n'):
  for match in re.finditer(pattern,line):
    if match:
      dict = match.groupdict()
      print
      print '     perms : ',dict['perms'],'(via direct access)'
      for key in dict:
        print '    ',key,': ',dict[key]

#--------------------------------------------------------------------------------
#
#--- SIMPLE EXAMPLE..

import re

filename = 'bogus.jpg'

m = re.search('(\S+)\.(\S+)', filename)

if m:
  print m.groups()[0]
  print m.groups()[1]

