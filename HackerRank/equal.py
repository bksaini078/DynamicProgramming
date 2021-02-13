#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    target=[0,1,2]
    min_arr = min ( arr )
    results = [0] * len(target)  # array for results with each target
    for item in arr :
        for i in target :
            gap = item - min_arr + i
            # print(item,min_arr,i,gap)
            results[i] += gap // 5 + (gap % 5) // 2 + (gap % 5) % 2
            # print(results[i])
    return min(results)


if __name__ == '__main__':
    arr=[1,2,3,7]
    print(equal(arr))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # t = int(input())
    #
    # for t_itr in range(t):
    #     n = int(input())
    #
    #     arr = list(map(int, input().rstrip().split()))
    #
    #     result = equal(arr)
    #
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
