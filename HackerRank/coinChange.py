'''ref:https://www.hackerrank.com/challenges/coin-change/problem'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
# def getWays(n,c):
#     # Write your code here
#     table=[None]*(n+1)
#     table[0]=0
#     for i in range(len(table)):
#         for num in c:
#             if i + num <= n :
#                 if table[i]!=None:
#                     table[i+num]= table[i]+ 1
#
#     return table[-1]

# def getWays(n, c,m=0,memo={}):
#     # Write your code here
#     # c.remove(1)
#     if n in memo.keys():
#         return memo[n]
#     if n<0 :
#         return 0
#     if n==0:
#         memo[n]=1
#         return memo[n]
#     if n>0 and m==len(c):
#         return 0
#     return getWays(n-c[m],c,m,memo)+getWays(n,c,m+1,memo)
def getWays(n, c,memo={}):
    # Write your code here
    # c.remove(1)
    if n<0 :
        return 0
    if n==0:
        return 1
    if(n,len(c)) in memo.keys():
        return memo[(n,len(c))]
    total_count=0
    for i in range(len(c)):
        if c[i]>n:
            continue
        if c[i]>0:
            temp= n-c[i]
            count=getWays(temp,c[i:],memo)
            if count>0:
                total_count+=count
    memo[(n,len(c))]=total_count
    return total_count

if __name__ == '__main__':
    n = 10
    c = [1,5,3,6]
    # n = 4
    # c = [1,2,3]
   
    t1=time.time()

    ways = getWays(n,c)
    print(ways)
    t2=time.time()
    print(t2-t1)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # m = int(first_multiple_input[1])
    # c = list(map(int, input().rstrip().split()))
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    # fptr.write(str(ways) + '\n')
    #
    # fptr.close()
