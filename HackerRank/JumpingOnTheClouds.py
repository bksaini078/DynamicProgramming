#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    #base condition
    if len(c)==1:
        return 0
    if len(c)==2:
        return 0 if c[1]==1 else 1
    if c[2]==1:
        return 1+jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1+ jumpingOnClouds(c[2:])



if __name__ == '__main__':


    n =6

    c = list(map(int, '0 0 1 0 0 1 0'.split()))

    result = jumpingOnClouds(c)
    print(result)

