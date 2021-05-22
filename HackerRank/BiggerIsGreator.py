'''https://www.hackerrank.com/challenges/bigger-is-greater/problem'''

import math
import os
import random
import re
import sys
import time


def biggerIsGreater(w):
    # print(w)
    w= list(w)
    if '\n' in w:
        w.remove('\n')
    # i = len(w)-1
    for i in range(len(w)-1, -2,-1):
        # print(w[i:],i)
        if i <=0:
            return 'no answer'
        if w[i]>w[i-1]:
            break

    # print(w[i-1],i-1)
    for j in range(len(w)-1,i-1,-1):
        # print(j)
        if w[j]>w[i-1]:
            # print(w[i-1],w[j])
            w[i-1],w[j]=w[j],w[i-1]
            w[i:]= sorted(w[i:])
            break

    return ''.join(w)



if __name__ == '__main__':
    # lgeuvf-->lgevfu
    # dqwrmse-->dqwrsem
    # w= 'acbd'
    f = open('/Users/teetu/Documents/Master_in_Web_science/'
             'DynamicProgramming/DynamicProgramming/input01.txt', 'r')
    fptr=open('/Users/teetu/Documents/Master_in_Web_science'
              '/DynamicProgramming/DynamicProgramming/output_m.txt','w')
    t1= time.time()

    for i in range(100000):
        s=f.readline()
        result = biggerIsGreater(s)
        print(result)
        fptr.write(result +'\n')
    t2=time.time()
    print('time',t2-t1)
    f.close()
    fptr.close()







