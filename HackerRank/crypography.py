'''Initially i = 0.
If s[i] is lowercase and the next character s[i+1] is uppercase, swap them, add a '*' after them, and move to i+2.
If s[i] is a number, replace it with 0, place the original number at the start, and move to i+1.
Else, move to i+1.
Stop if i is more than or equal to the string length. Otherwise, go to step 2.
51Pa*0Lp*0e
Sample Output
aP1pL5e'''
from collections import deque
if __name__=='__main__':
    s= '51Pa*0Lp*0e'
    s='pTo*Ta*O'
    d= deque()
    i= 0
    pos=s.count('0')-1
    while i<(len(s)):
        if s[i]=='*':
            d.append(s[i-1])
            d.append(s[i-2])
        if s[i]=='0':
            d.append(s[pos])
            pos-=1
        if (i==len(s)-1) or  ( s[i].islower() and s[i+1]!= '*') :
            d.append(s[i])

        i+=1
    print(''.join(x for x in d))