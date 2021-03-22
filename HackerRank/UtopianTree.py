import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(n) :
    h = 1
    for i in range ( 1, n + 1 ) :
        if i % 2 != 0 :
            h = 2 * h
            print('h1-->',h)
        if i % 2 == 0 :
            h += 1
            print('h2-->',h)
    return h


if __name__ == '__main__' :
    n=5
    print(utopianTree ( n ))

