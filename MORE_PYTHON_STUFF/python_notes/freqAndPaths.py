#!/usr/bin/python

"""
========================================================================
=== SCRIPT: freqs.py
=== Author: Bob Byers
=== Tested Python Version: 2.6.6

This script demos my use of python to solve the following task:

Process a log file containing a list of URLs (one URL per line), printing a
tally of the occurrences for each 'netloc' part of the URLs (netloc is from
the urlparse module). Also for each netloc, print a list of all paths (no duplicates)

EXAMPLE INPUT:

http://yahoo.com/login.js
http://google.com/login.js
http://google.com/login.js
http://wikipedia.org/login.js
http://wikipedia.org/about.htm

EXAMPLE OUTPUT:

          yahoo.com: freq=1 paths = login.js
         google.com: freq=2 paths = login.js
      wikipedia.org: freq=2 paths = about.htm, login.js

DATA STRUCTURE:

I used a dictionary whose keys are the unique netlocs, and values are
a tuple consisting of the frequency and a set of unique paths. For example:

      freqAndPaths{
       'yahoo.com' : (1, set('login.js'))
       'google.com' : (2, set('login.js'))
       'wikipedia.org' : (2, set('about.htm', 'login.js'))
      }

LIMITATIONS:

1. Not much exception handling or data validation

========================================================================
"""

MAXURLS = 256

import os
import re
import tempfile
import random as ra
import sys
from urlparse import urlparse

tmpf = tempfile.NamedTemporaryFile(delete=False)

#   +------------------------------------+
#---| Generate random URLs, save to disk |-------------------------------------
#   +------------------------------------+

def mkURLs(tmpf):
  
  hosts = ('google', 'yahoo', 'bing', 'wikipedia')
  tlds = ('com', 'net', 'org', 'co.uk', 'mil', 'gov', 'ie')
  paths = ('index.html', 'about.htm', 'login.js', '404.html', 'jsquery.htm', 'query=junk&page=3')

  numwritten = 0
  
  for i in range(MAXURLS):
    randnum = ra.randint(0,9999)
    host = ra.choice(hosts)
    tld = ra.choice(tlds)
    path = ra.choice(paths)
    URL = 'http://%s.%s/%s' % (host, tld, path)
    tmpf.write(URL+'\n')
    numwritten += 1
  
  tmpf.close()

  #-- Reopen the file, this time for reading
  tmpf = open(tmpf.name, 'r')

  return tmpf

#   +------+
#---| MAIN |-------------------------------------------------------------------
#   +------+

#   +------------------------------+
#---| Generate lots of random URLs |---
#   +------------------------------+

tmpf = mkURLs(tmpf)

#   +---------------+
#---| Read the URLs |---
#   +---------------+

for line in tmpf:

  line = line.strip()

  #-- Parse the URL into standard components (scheme, netloc, path, params, query, and fragment)

  theurl = urlparse(line)
  netloc = theurl.netloc
  path = theurl.path+theurl.params+theurl.query+theurl.fragment

  if netloc != '':

    #-- Update this netloc's dictionary entry

    try:
      count,paths = freqAndPaths[netloc]
      count += 1
      paths.add(path)
      freqAndPaths[netloc] = (count,paths)

    except NameError:
      #-- The dictionary doesn't exist at all
      pathset = set()
      pathset.add(path)
      freqAndPaths = {netloc : (1,pathset)}

    except KeyError:
      #-- The dictionary structure exists, but first time seeing this key
      pathset = set()
      pathset.add(path)
      freqAndPaths[netloc] = (1,pathset)

#-- Display the results

for key in sorted(freqAndPaths.keys()):

  #-- Retrive the frequency and paths for this netloc

  freq,paths = freqAndPaths[key]

  #-- Write the netloc and frequency. Do not write a newline yet

  sys.stdout.write('%16s: freq = %3d,  paths: ' % (key, freq))

  #(first of the paths gets no prefix)
  prefix = ''

  for path in sorted(paths):

    #-- Write one path (still no newline yet)
    sys.stdout.write(prefix+path)

    #(subsequent paths get a prefix consisting of a comma and space)
    prefix = ', '

  #-- OK now we can write a newline
  print

#-- Close and remove the temp file

tmpf.close()
os.remove(tmpf.name)

