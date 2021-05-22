''''ref:https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=nutanix'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_arr=[]
    for i in range(len(arr)):
        if i < len(arr)-2:
            for j in range(len(arr)):
                if j<len(arr)-2:
                    sum_arr.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                               arr[i+1][j+1]+
                               arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    return max(sum_arr)

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[-9, -9,-9,1, 1, 1 ],
           [0, -9,  0,  4, 3, 2],
           [-9, -9, -9,  1, 2, 3],
           [0,  0,  8,  6, 6, 0],
           [ 0,  0, 0, -2, 0, 0],
           [0,  0,  1,  2, 4, 0]]


    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
