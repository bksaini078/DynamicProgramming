'''https://www.hackerrank.com/challenges/the-grid-search/problem'''


import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    index=[]
    location=[]
    for j in range(len(G)-len(P)+1):
        if P[0] in G[j]:
            index.append(G[j].find(P[0]))
            location.append(j)
        print(G[j])
    print(location, index)
    if len(index)==0:
        return 'NO'
    if len(P)==1:
        return 'YES'
    for i in range(len(index)):
        g=G[location[i]+1:location[i]+len(P)]
        p=P[1:]
        print(p,g)
        t = []
        for j in range(len(g)):
            if p[j] in g[j]:
                if index[i]!=g[j].find(p[j]):
                    t=[]
                    break
                else:
                    t.append('YES')
        if len(t)==len(P)-1:
            return 'YES'
    return 'NO'



if __name__ == '__main__':

    # G=['7283455864', '6731158619', '8988242643', '3830589324', '2229505813',
    #    '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
    # P=['9505', '3845', '3530']
    # print(gridSearch(G, P))

    G=['400453592126560', '114213133098692', '474386082879648',
       '522356951189169', '887109450487496', '252802633388782',
       '502771484966748', '075975207693780', '511799789562806',
       '404007454272504', '549043809916080','962410809534811',
       '445893523733995', '768705303299994', '650629270887999']
    P=['99','99']
    print(gridSearch(G, P))





