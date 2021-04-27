# bitwise and operation
'''Given an array [10,7,4,3,2,1] find the number of pairs whos AND result is power of 2 '''
import math
import time
from itertools import combinations,combinations_with_replacement

if __name__=='__main__':
    arr=[3 for i in range(10000)]
    #0.36679816246032715
    count=0
    time1=time.time()
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            op= arr[i]&arr[j]
            if op & (op-1)==0 and op!=0:
                count+=1
    print(count)
    print(time.time()-time1)
    time2= time.time()

    # second method quite faster than before
    count=0
    if max(arr)==min(arr):
        l=len(arr)
        op = max(arr)&min(arr)
        if op & (op - 1) == 0 and op != 0:
            count +=math.comb(len(arr),2)
    else:
        for item in (combinations(arr,2)):
            op= item[1]&item[0]
            if op & (op - 1) == 0 and op != 0:
                count += 1

    print(count)
    print(time.time()-time2)