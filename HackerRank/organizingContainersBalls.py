'''Ref: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem'''

import math
import os
import random
import re
import sys




def organizingContainers(container):

    typeCount= [0]*(len(container[0]))
    containerCapacity= [sum(x) for x in container]
    #logic: typecount == containerCapacity to in order to get possible swap otherwise not possible
    # count type count
    for item in container:
        for j in range(len(item)):
            typeCount[j]+=item[j]
    # now sorting in order to compare both type and capacity
    typeCount.sort()
    containerCapacity.sort()

    return 'Possible' if typeCount==containerCapacity else 'Impossible'



if __name__ == '__main__':
 container=[[1,3,1],[2,1,2],[3,3,3]]
 container = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]


 print(organizingContainers(container))