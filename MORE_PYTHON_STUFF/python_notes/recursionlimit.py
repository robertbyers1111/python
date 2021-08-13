import sys

limit = sys.getrecursionlimit()
print("limit: %d" % (limit))
Newlimit = 500
sys.setrecursionlimit(Newlimit)
limit = sys.getrecursionlimit()
print("limit: %d" % (limit))
