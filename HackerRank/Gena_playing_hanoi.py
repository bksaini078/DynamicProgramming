'''ref:https://www.hackerrank.com/challenges/gena/problem?h_r=next-challenge&h_v=zen&isFullScreen=false'''

import math
import os
import random
import re
import sys


def solve_tower(a) :

    if len(a)==sum(a):
        return 0
    swap=0
    while sum(a)!=len(a):

        for j in range(len(a)-1,-1,-1):
            # print(a[:j],j,len(a))
            if 1 in a[:j]:
                continue
            if 1 not in a[:j]:
                a[j]=1
            if j<len(a)-1  :
                if a[j+1]==1:
                    a[j]=1
                    swap+=1
                    # print(j,a,swap)
            if j==0 and a[j]==1 and sum(a)!=len(a):
                a[j]=abs(a[j+2]-a[j+1])
                swap+=1
                # print(j,swap,a)
    return swap


if __name__ == '__main__' :
    # N = int ( input () )
    #
    # a = list ( map ( int, input ().rstrip ().split () ) )

    a = [1, 4,2]

    print(solve_tower ( a ) )