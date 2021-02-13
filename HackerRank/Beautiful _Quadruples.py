#!/bin/python3
'''ref:
https://www.hackerrank.com/challenges/xor-quadruples/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign'''
import os
import sys
from itertools import permutations

#
# Complete the beautifulQuadruples function below.
#

# def beautifulQuadruples(a,b,c,d,count=0,memo={}):
#     # Write your code here.
#     key = str(sorted([a, b, c, d] ))
#     if key in memo.keys():
#         return 0
#     if a<1 or b<1 or c<1 or d<1:
#         return count
#     if a^b^c^d !=0:
#         print(a,b,c,d)
#         print('count',count)
#         count+=1
#         memo[str ( sorted ( [a, b, c, d] ) )] = count
#     return beautifulQuadruples(a-1,b,c,d,count,memo)\
#            +beautifulQuadruples(a,b-1,c,d,count,memo)\
#            +beautifulQuadruples(a,b,c-1,d,count,memo)\
#            +beautifulQuadruples(a,b,c,d-1,count,memo)
    # return count

def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
  if a==b==c==d:
    return 0

  memo={}
  count = 0
  for i in range(1,a+1):
      for j in range(1,b+1):
          for k in range(1,c+1):
              for l in range(1,d+1):
                 key=str(sorted([i,j,k,l]))
                 if key in memo.keys() or a==b==c==d:
                    continue
                 if ((i ^ j ^ k ^ l) != 0):
                    memo[str(sorted([i,j,k,l]))]= [i,j,k,l]
                    count+=1
  return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # abcd = input().split()
    #
    # a = int(abcd[0])
    #
    # b = int(abcd[1])
    #
    # c = int(abcd[2])
    #
    # d = int(abcd[3])
    # abcd=[1,2,3,4]
    # perm=permutations(abcd,len(abcd))
    # for i in list(perm):
    #     print(i)

    print(beautifulQuadruples(1, 2, 3, 4))



    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
