
--------------------------------------------------------------------------------

The EINTR error can be returned from many system calls when the
application receives a signal while waiting for other input. Typically
these signals can be quite benign and already handled by Python, but the
underlying system call still ends up being interrupted. When doing C/C++
coding this is one reason why you can't entirely rely on functions like
sleep(). The Python libraries sometimes handle this error code internally,
but obviously in this case they're not.

You might be interested to read this thread which discusses this problem.

The general approach to EINTR is to simply handle the error and retry the
operation again - this should be a safe thing to do with the get() method
on the queue. Something like this could be used, passing the queue as a
parameter and replacing the use of the get() method on the queue:

import errno

def my_queue_get(queue, block=True, timeout=None):
    while True:
        try:
            return queue.get(block, timeout)
        except IOError, e:
            if e.errno != errno.EINTR:
                raise

# Now replace instances of queue.get() with my_queue_get(queue), with other
# parameters passed as usual.

Typically you shouldn't need to worry about EINTR in a Python program
unless you know you're waiting for a particular signal (for example
SIGHUP) and you've installed a signal handler which sets a flag and relies
on the main body of the code to pick up the flag. In this case, you might
need to break out of your loop and check the signal flag if you receive
EINTR.

However, if you're not using any signal handling then you should be able
to just ignore EINTR and repeat your operation - if Python itself needs to
do something with the signal it should have already dealt with it in the
signal handler.

--------------------------------------------------------------------------------

Old question, modern solution: as of Python 3.5, the wonderful PEP 475 -
Retry system calls failing with EINTR has been implemented and solves the
problem for you. Here is the abstract:

System call wrappers provided in the standard library should be retried
automatically when they fail with EINTR , to relieve application code from
the burden of doing so.

By system calls, we mean the functions exposed by the standard C library
pertaining to I/O or handling of other system resources.

Basically, the system will catch and retry for you a piece of code that
failed with EINTR so you don't have to handle it anymore. If you are
targeting an older release, the while True loop still is the way to go.
Note however that if you are using Python 3.3 or 3.4, you can catch the
dedicated exception InterruptedError instead of catching IOError and
checking for EINTR.

--------------------------------------------------------------------------------

