
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from shared import *
from datetime import datetime

t0 = datetime.now().strftime('[%Y/%m/%d %H:%M:%S]')
print('t0:',t0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 6. Print the file path of imported modules.

import threading 
import socket

print(threading)
print(socket)

#1- <module 'threading' from '/usr/lib/python2.7/threading.py'>
#2- <module 'socket' from '/usr/lib/python2.7/socket.py'>

