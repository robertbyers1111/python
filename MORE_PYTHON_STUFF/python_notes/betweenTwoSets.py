#!/usr/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#

def getTotalX(a, b):
    #
    # Write your code here.
    #

    result=0

    start = sorted(a)[-1]
    print('start:',start)

    end = sorted(b)[0]+1
    print('end:',end)

    res=[]

    for n in range(start,end):

        ok=1

        print()
        print('~'*44)
        print('n:',n)

        if ok:
            for i in a:
                if i == 0 or n % i != 0:
                    ok=0
                    print('A',n,'%',i,'not ok')
                    break
                print(n,'%',i,'ok')

        if ok:
            for i in b:
                if n == 0 or i % n != 0:
                    ok=0
                    print('B',i,'%',n,'not ok')
                    break
                print(i,'%',n,'ok')

        if ok:
              res.append(n)

        print('ok:',ok,'res:',res)

    total=len(res)
    print('done. res:',res,'total:',total)
    return(total)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

