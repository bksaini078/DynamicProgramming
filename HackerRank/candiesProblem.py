#!/bin/python3

#ref https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=nutanix&h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candy_ltori= [0]*n
    candy_ltori[0]=1
    candy_ritol= [0]*n
    candy_ritol[n-1]=1
    # print(arr)
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            candy_ltori[i]=candy_ltori[i-1]+1
        else:
            candy_ltori[i]=1
        # print(candy_ltori)

    for i in range(len(arr)-2,-1,-1):
        if arr[i]>arr[i+1]:
            # print(arr[i],arr[i+1])
            candy_ritol[i]=candy_ritol[i+1]+1
        else:
            candy_ritol[i]=1

    max_list=[max(x,y) for x,y in zip(candy_ltori,candy_ritol)]
    # print(max_list)
    return sum(max_list)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    n=6
    arr = [4,6,4,5,6,2]
    print(candies(n,arr))
    n = 3
    arr = [1, 2, 2]
    print ( candies ( n, arr ) )
    n=10
    arr = [2,4,2,6,1,7,8,9,2,1]
    print ( candies ( n, arr ) )
    n=8
    arr = [2,4,3,5,2,6,4,5]
    print ( candies ( n, arr ) )
    #
    # for _ in range(n):
    #     arr_item = int(input())
    #     arr.append(arr_item)
    #
    # result = candies(n, arr)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
