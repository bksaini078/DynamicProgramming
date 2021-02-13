#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    total_len=len(a)+len(b)
    count=0
    for item in a:
        if item in b:
            # if item in a:
            count += 1
            a=a.replace(item,'',1)
            b=b.replace(item,'',1)
    return total_len-2*count

if __name__ == '__main__':
    # fptr = open ( os.environ['OUTPUT_PATH'], 'w' )
    #
    # a = input ()
    #
    # b = input ()
    a='cde'
    b='abcc'
    print(makeAnagram ( a, b ))
    a='cde'
    b='dcf'
    print(makeAnagram ( a, b ))
    a='fcrxzwscanmligyxyvym'
    b='jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    print(makeAnagram(a,b)) #expected output=30

    # fptr.write ( str ( res ) + '\n' )
    #
    # fptr.close ()
