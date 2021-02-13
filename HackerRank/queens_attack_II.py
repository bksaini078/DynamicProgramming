'''Queen's Attack II
Ref: https://www.hackerrank.com/challenges/queens-attack-2/problem'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # go right
    right= abs(n-c_q)
    left=abs(1-c_q)
    bottom=abs(1-r_q)
    up=abs(n-r_q)
    dia_up_r= min(right,up)
    # dia_up_l=abs(1-c_q)
    dia_up_l = min(left,up)
    dia_bot_r = min(right,bottom)
    # dia_bot_r= abs(1-r_q)
    dia_bot_l= min(left,bottom)
    print(right,left,bottom,up,dia_up_r,dia_up_l,dia_bot_r,dia_bot_l)
    total= right+left+bottom+up+dia_up_r+dia_up_l+dia_bot_r+dia_bot_l
    print('total-->',total)
    if k==0:
        return total
    avoid=0
    for item in obstacles:
        if item[0]>n or item[1]>n or item[0]<0 or item[1]<0:
            return total
        if r_q==item[0] and c_q==item[1]:
             continue
        if r_q == item[0]:
            if c_q-item[1]>0:
                avoid += item[1]
                # print('avoid1-->',avoid)
            else :
                avoid += (n - item[1] + 1)
                # print('avoid2-->',avoid)
        if c_q==item[1]:
            if r_q - item[0] > 0 :
                avoid += item[0]
                # print('avoid3-->', avoid )
            else :
                avoid += (n - item[0] + 1)
                # print ( 'avoid4-->', avoid )
        if abs(r_q-item[0])==abs(c_q-item[1]):
            # print('e')
            if r_q-item[0]<0 and c_q-item[1]<0:
                avoid+= min(n-item[0]+1,n-item[1]+1)
                # print('avoid5-->',avoid)
                continue
            if r_q-item[0]<0 and c_q-item[1]>0:
                avoid+= min(item[1]-1+1,n-item[0]+1) #abs(1-item[1])
                # print('avoid6-->', avoid)
                continue
            if r_q-item[0]>0 and c_q-item[1]<0:
                avoid+= min(item[0]-1+1,n-item[1]+1)#abs(1-item[0])
                # print('avoid7-->', avoid)
                continue
            if r_q-item[0]>0 and c_q-item[1]>0:
                avoid+=min(item[0],item[1])#abs(1-item[0])
                # print ( 'avoid8-->', avoid )
                continue

    result=total-avoid
    # print('result-->', result)
    return result

if __name__ == '__main__':
    # fptr = open('/Users/teetu/Documents/Master_in_Web_science/DynamicProgramming/HackerRank/queens', 'w')
    #
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    print(obstacles)
    # n=5
    # k=3
    # obstacles=[[5,5],[4,2],[2,3]]
    # r_q=4
    # c_q=3
    # print(queensAttack(n, k, r_q, c_q, obstacles))
    #
    # n=8
    # k=1
    # obstacles=[[5,6]]
    # r_q=5
    # c_q=1
    print(queensAttack(n, k, r_q, c_q, obstacles))

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
