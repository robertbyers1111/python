#!/usr/bin/python3

"""
minimal.py
"""

import os
import sys

def Usage():
    print('USAGE: %s FILE', os.path.basename(__file__))
    sys.exit(-1)

def main():
    Usage if len(sys.argv) < 1
    for arg in sys.argv:
        print("arg:", arg)

if __name__ == '__main__':
    main()

