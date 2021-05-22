#ref : https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&playlist_slugs%5B%5D=nutanix&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    days=1
    candies=m*w
    max_days = math.ceil(n/(m * w))
    resource=0
    remain=n-candies
    # print(candies,remain)
    while candies<n:
        if candies<p:
                    req_days=math.ceil((p-candies)/(m*w))
                    candies+=req_days*m*w
                    days+=req_days
                    continue
        #buy resource
        resource,candies = divmod(candies , p)
        total= m+w+resource
        half=total//2
        if m>w:
            m=max(m,half)
            w=total- m
        else:
            w=max(w,half)
            m=total-w
        #calculation candies again
        # print ( 'machine' )
        # print(candies,remain)
        # print('weights',m,w)
        # #production
        # print('production')
        candies=candies+m*w
        days+=1
        max_days = min ( max_days, days + math.ceil ( (n - candies) / (m * w) ) )
        # print(candies,days)

    return min(max_days,days)





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # mwpn = input().split()
    #
    # m = int(mwpn[0])
    #
    # w = int(mwpn[1])
    #
    # p = int(mwpn[2])
    #
    # n = int(mwpn[3])
    # m=3
    # w=1
    # p=2
    # n=12
    # result = minimumPasses(m, w, p, n)
    # print(result)
    # m=3
    # w=1
    # p=2
    # n=12
    #
    print(minimumPasses(1, 1, 1, 60))
    print(minimumPasses( 3, 1, 2, 12))
    print(minimumPasses( 5184889632, 5184889632, 20, 10000))
    print(minimumPasses( 1,1,6,45))



    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
