#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extraLongFactorials(n, memo={}) :
    key = n
    if key in memo.keys():
        return memo[key]
    if n == 1 :
        return 1
    memo[n]=n*extraLongFactorials(n-1,memo)

    return memo[n]

if __name__ == '__main__' :
    # n = int ( input () )
    n=30

    print(extraLongFactorials ( n ))
