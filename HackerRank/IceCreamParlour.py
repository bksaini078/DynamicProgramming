#!/bin/python3
#ref: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=nutanix
import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
#explanation: if money is 4 and cost is [1,2,3].
# if first instance 4-1 =3 search in dictionary. Its not there
# then dictionary with key 1, memo[1]=0
# now second instance 4-2, same memo[2]=1
#in third instance 4-3 that is 1 is present in memo
# so the 0,2 original index is the answer.
def whatFlavors(cost, money):
    memo={}
    for id,price in enumerate(cost):
        if money-price in memo.keys():
            print('{} {}'.format(memo[money-price]+1, id+1))
            # return memo[money-price], id
        memo[price]=id
    return None



# with tabulation
# def whatFlavors(cost, money):
#     table=[None]*(money+1)
#     table[0]=[]
#     for i in range(money):
#         # print('#')
#         if table[i] != None :
#             for j in range(len(cost)):
#                 # print(i,j,cost[j])
#                 if i+cost[j]<=money and i!=j+1:
#                     temp=table[i].copy()
#                     temp.append(j+1)
#                     if len(temp)<=2:
#                         if len(temp)==2:
#                             if temp[0]==temp[1]:
#                                 continue
#                         table[i+cost[j]]=temp
#                     # if len(temp)>2:
#                     #     temp=[i]
#                     #     temp.append(j+1)
#                     #     table[i+cost[j]]=temp
#                     # print(table)
#     table[-1].sort()
#     print("{} {} ".format(table[-1][0],table[-1][1]))

if __name__ == '__main__':
    cost=[99,4,2,3,3,2,2,2,2,2,
          3,3,3,3,3,3,3,33,3,3,3,
          3,3,3,3,3,3,3,3,3,3,322,
          3,3,3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,33,3,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,33,
         3,3,3,3,3,3,3,3,33,3,3,3,3,332,
         3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,32,3,3,3,3,33,3,
         3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3
    ,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,1]
    money=100
    # print(cost[2:])
    whatFlavors(cost, money)
    cost=[2,2,4,3]
    money=4
    # print(cost[2:])
    whatFlavors(cost, money)
    cost = [2, 1, 3, 5, 6]
    money = 5
    whatFlavors(cost, money)
    cost = [1, 4, 5, 3, 2]
    money = 4
    whatFlavors(cost, money)
    cost = [ 3, 8, 3,7]
    money = 6
    whatFlavors ( cost, money )
    #
    # t = int(input())
    #
    # for t_itr in range(t):
    #     money = int(input())
    #
    #     n = int(input())
    #
    #     cost = list(map(int, input().rstrip().split()))
    #
    #     whatFlavors(cost, money)
