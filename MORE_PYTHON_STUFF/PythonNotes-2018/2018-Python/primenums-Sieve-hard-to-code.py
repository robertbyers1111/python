#!/usr/bin/python3

# Computes all primes up to a max value. Uses division.

# FROM https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NOTE: NOT WORKING! Getting the following error..
#
# ValueError: attempt to assign sequence of size 22 to extended slice of size 23
#
# .. which I have yet to resolve. It comes from the first sieve
# assignment inside the for loop (and possibly the second sieve
# assignment as well)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import sys
from datetime import datetime
from datetime import timedelta


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Primes():

  def __init__(self):
    self.primes = []
    self.primes.append(2)

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def computePrimes2(self,max):
    """ Input max>=6, Returns a list of primes, 2 <= p < max """

    self.t0 = datetime.now()
    self.max = max

    max, correction = max-max%6+6, 2-(max%6>1)
    sieve = [True] * (int(max/3))

    for i in range(1,int(int(max**0.5)/3)+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      int(k*k/3)      ::2*k] = [False] * (int((max/6-k*k/6-1)/k+1))
        sieve[k*int((k-2*(i&1)+4)/3)::2*k] = [False] * (int((max/6-k*(k-2*(i&1)+4)/6-1)/k+1))

    self.primes = [2,3] + [3*i+1|1 for i in range(1,int(max/3)-correction) if sieve[i]]

    self.t1 = datetime.now()
    self.delta = self.t1 - self.t0

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def computePrimes(self,max):
    """ Returns a list of primes < max """

    self.t0 = datetime.now()
    self.max = max

    sieve = [True] * max

    for i in range(3,int(max**0.5)+1,2):
      if sieve[i]:
        sieve[i*i::2*i]=[False]*(int((max-i*i-1)/(2*i)+1))

    self.primes = [2] + [i for i in range(3,max,2) if sieve[i]]

    self.t1 = datetime.now()
    self.delta = self.t1 - self.t0

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  # def computePrimes(self,max):
  #   self.t0 = datetime.now()
  #   self.max = max
  #
  #   for n in range(3,max+1,2):
  #
  #     isprime=True
  #     stopval=int(n/2)
  #
  #     for i in self.primes:
  #
  #       if i > stopval:
  #         break
  #       if n % i == 0:
  #         isprime=False
  #         break
  #
  #     if isprime:
  #       self.primes.append(n)
  #
  #   self.t1 = datetime.now()
  #   self.delta = self.t1 - self.t0

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def showprimes(self):
    totfound = len(self.primes)
    print('Found',totfound,'primes from 1 to',self.max)
    print('Elapsed:',str(self.delta))

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
#---| M A I N |----------------------------------------------------------------
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

x = Primes()
x.computePrimes2(num)
x.showprimes()

#   +---------------+
#---| R E S U L T S |----------------------------------------------------------
#   +---------------+

