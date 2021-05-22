'''https://www.hackerrank.com/challenges/encryption/problem?h_r=next-challenge&h_v=zen'''
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s) :
    spaceRemove = s.replace ( " ", "" )
    L = len(spaceRemove)
    column = math.ceil(math.sqrt( L ))
    row = math.floor ( math.sqrt(L))

    result_s = [''* 1 for i in range(column)]

    for i in range(0,L,column):
        temp=spaceRemove[i:i+column]

        for j in range(len(temp)):
            result_s[j]= result_s[j]+temp[j]


    return ' '.join(word for word in result_s)


if __name__ == '__main__' :
    # fptr = open ( os.environ['OUTPUT_PATH'], 'w' )

    s = 'wclwfoznbmyycxvaxagjhtexdkwjqhlojy' \
        'kopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny'

    print(encryption ( s ))
    s1='haveaniceday'
    print(encryption ( s1 ))


    # fptr.write ( result + '\n' )