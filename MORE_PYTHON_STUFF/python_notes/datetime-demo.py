#!/usr/bin/python

from datetime import datetime
from datetime import timedelta
from time import sleep

def doit():

    epoch_seconds = 0
    epoch = datetime.utcfromtimestamp(epoch_seconds)

    print
    print '  epoch:',epoch,'(default format)'
    print '  epoch:',epoch.strftime('%Y-%m%d-%H:%M:%S'),'(my format)'
    print

    t0 = datetime.now()
    print '    now:',t0.strftime('%Y-%m%d-%H:%M:%S')

    sleep(12.345)

    t1 = datetime.now()
    print '  later:',t1.strftime('%Y-%m%d-%H:%M:%S')

    elapsed = t1 - t0

    print
    print '             elapsed:',elapsed
    print '        elapsed.days:',elapsed.days
    print '     elapsed.seconds:',elapsed.seconds
    print 'elapsed.microseconds:',elapsed.microseconds

doit()
