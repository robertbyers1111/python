#!/usr/bin/python3

# The try statement has another optional clause which is intended to
# define clean-up actions that must be executed under all circumstances.
#
# A finally clause is always executed before leaving the try statement,
# whether an exception has occurred or not. When an exception has
# occurred in the try clause and has not been handled by an except
# clause (or it has occurred in an except or else clause), it is
# re-raised after the finally clause has been executed. The finally
# clause is also executed “on the way out” when any other clause of the
# try statement is left via a break, continue or return statement.

def test1():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')

def test2():
    try:
        print('returning 1')
        return 1
    finally:
        print('returning 2')
        return 2

def main():
    test1()
    test2()

if __name__ == '__main__':
    main()

