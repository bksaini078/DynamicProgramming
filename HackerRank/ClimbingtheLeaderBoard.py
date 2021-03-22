'''https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem'''

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboardx(ranked, player):
    # Write your code here
    # print(sorted(list(set(ranked)),reverse=True))
    sorted_rank = sorted(list(set(ranked)),reverse=True)
    dict_rank ={}
    result= []
    for i in range(1,len(sorted_rank)+1):
        dict_rank[sorted_rank[i-1]]=i
    for p in player:
        #if key present in dict
        if p in dict_rank.keys():
            result.append(dict_rank[p])
        else:
            for key in sorted(dict_rank.keys()):
                if p>key:
                    temp= dict_rank[key]
                    dict_rank.pop(key)
                    dict_rank[p]=temp
                    # print('dict->',dict_rank)
                if p<=key:
                    temp=dict_rank[key]
                    dict_rank[p]=temp+1
                    result.append(temp+1)
                    # print(dict_rank)
                    break
    if len(dict_rank.keys())==1:
        result.append(dict_rank[player[-1]])

    return result
def climbingLeaderboard(ranked, player):
    ranked= sorted(list(set(ranked)),reverse=True)
    result=[]
    l= len(ranked)
    for p in player:
        while l>0 and (p>=ranked[l-1]):
            l-=1
        result.append(l+1)
        # if p in ranked:
        #     result.append(ranked.index(p)+1)
        #     # print('result->',result)
        # else:
        #     for i in range(len(ranked)-1,-1,-1):
        #         if p >=max(ranked):
        #             result.append(1)
        #             break
        #         if p <min(ranked):
        #             ranked.append(p)
        #             result.append ( ranked.index ( p ) + 1 )
        #             break
        #         if p<ranked[i]:
        #             ranked.append(p)
        #             # print('ranked->',ranked)
        #             result.append(ranked.index(p)+1)
        #             break
        #         if p>ranked[i]:
        #             ranked[i]=p
        #             ranked=ranked[:i]
        #             print('ranked',ranked)
        #             continue
    return result



if __name__ == '__main__':


    ranked = [100,90,90,80,75,60]
    player = [50,65,77,90,102]
    # ranked = [100,100,50,40,40,20,10]
    # player = [5,25,50,102]


    result=climbingLeaderboard(ranked, player)
    for item in result:
        print(item)



