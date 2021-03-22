'''ref: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem'''
import math
import os
import random
import re
import sys
import time
# Complete the sherlockAndAnagrams function below.

def sherlockAndAnagrams(s):
    ls= len(s)
    count=0
    for i in range(1,ls):
        dict={}
        for j in range(ls-i+1):
            substr= list(s[j:j+i])
            substr.sort()
            substr=''.join(substr)
            print(substr)
            if substr in dict:
                dict[substr]+=1
            else:
                dict[substr]=1
            print(dict)
            count+=dict[substr]-1

    return count




if __name__ == '__main__':
    t1= time.time()
    # s='ifailuhkqq'
    # print(sherlockAndAnagrams(s))
    # s = 'abcd'
    # print ( sherlockAndAnagrams( s ))
    s = 'abba'
    print(sherlockAndAnagrams(s))
    # s = 'cdcd'
    # print ( sherlockAndAnagrams ( s ) )
    # s = 'kkkk'
    # print ( sherlockAndAnagrams ( s ) )
    t2 = time.time ()
    print ( t2 - t1 )


