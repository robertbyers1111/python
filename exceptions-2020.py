#!/usr/bin/python3

import sys
import os
import threading
import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NOTE: According to this info (found on stack overflow), my examples below are not the latest exception handling technique. Need more
# info on the __traceback__ method.
#
#     The __traceback__ attribute is available only since Python 3.0, so if you're looking to make your code compatible with Python 2 you
#     should use sys.exc_info() instead; otherwise, per PEP-3134, the introduction of the __traceback__ attribute is indeed meant to
#     fully replace sys.exc_info(), and possibly deprecate it:
#
#     In today's Python implementation, exceptions are composed of three parts: the type, the value, and the traceback. The sys module,
#     exposes the current exception in three parallel variables, exc_type, exc_value, and exc_traceback, the sys.exc_info() function
#     returns a tuple of these three parts, and the raise statement has a three-argument form accepting these three parts. Manipulating
#     exceptions often requires passing these three things in parallel, which can be tedious and error-prone. Additionally, the except
#     statement can only provide access to the value, not the traceback. Adding the __traceback__ attribute to exception values makes all
#     the exception information accessible from a single place.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   +--------------+
#---| With threads |---
#   +--------------+
#
# (from https://pymotw.com/2/sys/exceptions.html)
#
#   def do_something_with_exception():
#       exc_type, exc_value = sys.exc_info()[:2]
#       print('Handling %s exception with message "%s" in %s' % \
#           (exc_type.__name__, exc_value, threading.current_thread().name))
#
#   def cause_exception(delay):
#       time.sleep(delay)
#       raise RuntimeError('This is the error message')
#
#   def thread_target(delay):
#       try:
#           cause_exception(delay)
#       except:
#           do_something_with_exception()
#
#   threads = [ threading.Thread(target=thread_target, args=(0.3,)),
#               threading.Thread(target=thread_target, args=(0.1,)),
#               ]
#
#   for t in threads:
#       t.start()
#   for t in threads:
#       t.join()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   +--------+
#---| Simple |---
#   +--------+

def exceptionDemo(testnum):

    bbb = {}
    bbb['en'] = 'English'
    bbb['es'] = 'Espanol'
    default_lang = 'en'
    lang = 'fr'

    try:
        if testnum == 0:
            return bbb[lang]
        else:
            return 0/0

    # Catches, rectifies and continues
    except KeyError:
        print(f"\n\tUnsupported key '{lang}'\n")
        return bbb[default_lang]

    # Catches, lets you print something and re-raise
    except:
        exc_info = sys.exc_info()
        print(f'\n\tCaught {exc_info[0].__name__}: {exc_info[1]}\n')
        raise

exceptionDemo(0)
exceptionDemo(1)

