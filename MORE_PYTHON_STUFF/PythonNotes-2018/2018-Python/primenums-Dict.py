#!/usr/bin/python3

from datetime import datetime
from datetime import timedelta

class Primes():

  def __init__(self):
    self.t0 = datetime.now()
    self.primes = {}
    self.primes[2] = True

  def isprime(self,n):
    #print()
    #print('Checking',n)
    isprime=True
    stopval=int(n/2)
    for i in sorted(self.primes.keys()):
      if i > stopval:
        break
      #print(n,'%',i,'=',n%i)
      if n % i == 0:
        isprime=False
        break
    if isprime:
      #print(n,'is prime')
      self.primes[n] = True

  def computeprimes(self,max):
    self.max = max
    for i in range(3,max+1):
      self.isprime(i)

  def showprimes(self):
    self.t1 = datetime.now()
    self.delta = self.t1 - self.t0
    print('Computed primes up to',self.max)
    print('Elapsed:',str(self.delta))
    for k in range(self.max):
      if k in self.primes.keys():
        print('%12d' % (k))

x = Primes()
x.computeprimes(2**16)
x.showprimes()

