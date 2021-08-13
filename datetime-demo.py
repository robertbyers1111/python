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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# More datetime notes...
#
# To get seconds since 1/1/1970
#
#     int(datetime.now() - timedelta(days=ndays))
#
# To get YYMMDDHHMM
#     (datetime.now() - timedelta(days=ndays)).strftime('%y%m%d%H%M')

timestamp_two_weeks_ago = (datetime.now() - timedelta(days=14)).timestamp()
seconds_since_1970 = int(timestamp_two_weeks_ago)
yymmddhhmm = timestamp_two_weeks_ago.strftime('%y%m%d%H%M')

