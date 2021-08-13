#!/usr/bin/python3

import os
import sys
from datetime import datetime
from datetime import timedelta

class Primes():

  def __init__(self,n):
    self.primes=[]
    self.n = n
    t0 = datetime.now()
    self.primes = [x for x in range(2,n+1)]
    t1 = datetime.now()
    self.delta1 = t1-t0

  def eliminateNonPrimes(self):
    #print()
    #print('n:',self.n)

    t0 = datetime.now()
    for i in range(2,self.n + 1):
      k = i
      #print()
      #print('Removing multiples of',i)
      for j in self.primes:
        k += i
        if k > self.n:
          break
        #print('  k:',k)
        if k in self.primes:
          #print('  removing',k)
          self.primes.remove(k)
    t1 = datetime.now()
    self.delta2 = t1-t0

  def showPrimes(self):
    totfound = len(self.primes)
    print('Found',totfound,'primes from 1 to',self.n)
    print('Time to populate initial list:', self.delta1)
    print(' Time to eliminate non-primes:', self.delta2)

    if totfound <= 50:
      for k in self.primes:
        print('%12d' % (k))
    else:
      print()
      print('First 25 primes..')
      for k in self.primes[:25]:
        print('%12d' % (k))
      print()
      print('Last 25 primes..')
      for k in self.primes[-25:-1]:
        print('%12d' % (k))


#   +---------+
#---| M A I N |---
#   +---------+

nargs = len(sys.argv[1:])

if nargs == 0:
  num = 100
elif nargs == 1:
  num = int(sys.argv[1])
else:
  print('USAGE:',os.path.basename(__file__),'[max]')
  sys.exit(-1)

print('Computing primes up to',num,'..')

primes = Primes(num)
primes.eliminateNonPrimes()
primes.showPrimes()
