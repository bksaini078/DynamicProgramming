'''https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true'''

import math
import os
import random
import re
import sys


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q) :
    result =[]
    for i in range(p,q+1):
        value=-1
        d= len(str(i))
        sq=str(i**2)
        # print ( 'sq-->', sq )
        if len(sq)==1:
            # print(sq[:d])
            value=int(sq[:d])+0
        else:
            # print ( len ( sq ) )
            l = sq[0:len(sq)-d]
            r = sq[len(sq)-d:len(sq)]
            # print ( l,r )
            if int(r)>0 :
                value=int(l )+int(r)
        if value ==i:
            result.append(i)
    if len(result)!=0:
        print(' '.join(str(x) for x in result))
        # [print(x) for x in result]
    else:
        print('INVALID RANGE')




if __name__ == '__main__' :

    p=100
    q=300
    kaprekarNumbers ( p, q )
