'''ref:-https://www.hackerrank.com/challenges/common-child/problem'''
import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild1(s1,s2,m,n,memo):
    #base case
    # print ( s1, s2 )
    if m==0 or n==0:
        return 0
    if memo[m-1][n-1]!=-1:
        return memo[m-1][n-1]

    if s1[m-1]==s2[n-1]:
        memo[m-1][n-1]= commonChild(s1,s2,m-1,n-1,memo)+1
        return memo[m-1][n-1]
    else:
        memo[m - 1][n - 1] = max(commonChild(s1,s2,m-1,n,memo),commonChild(s1,s2,m,n-1,memo))
        return memo[m-1][n-1]
def commonChild(str1,str2):
    '''solution using tabulation'''
    if str1==str2:
      return len(str1)
    if len(str1)==0 or len(str2)==0:
      return 0
    table=[[0]*(len(str1)+1) for i in range(len(str2)+1)]
    # str1=" "+str1
    # str2= " "+str2
    #row
    for i in range(len(str2)):
        #column
        # print(table)
        for j in range(len(str1)):
            # when char are empty
            # if str1[j]==" " or str2[i]== " ":
            #     table[i][j]=0
            #when char matches
            if str2[i]==str1[j]:
                table[i][j]= table[i-1][j-1]+1
            # when char does not match
            if str2[i]!=str1[j]:
                table[i][j]=max(table[i][j-1], table[i-1][j])
    return table[-2][-2]



if __name__ == '__main__':
    s1 = 'ABCD'
    s2 = 'ABDC'
    print(commonChild(s1, s2))
    s1 = 'SHINCHAN'
    s2 = 'NOHARAAA'
    print(commonChild(s1, s2))
    s1 = 'abcdbbdbdbajhfaeuhafnbuegrabfafiuheruiahruaehraiuehraebfaiufeuirabfaifbaiube'
    s2 = 'adhfauidfhaduifhadfiuhadfliuahdfliuahdfliuahdfiluahdfilauhdfailufhailuhdfail'
    print(commonChild(s1, s2))


