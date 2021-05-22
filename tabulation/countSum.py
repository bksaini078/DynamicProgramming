'''howsum(target, numbers)--> total number of ways array whose sum is equal to targetSum'''

def countSum(target,numbers):
    table= [None]*(target+1)
    table[0]=0
    for i in range(len(table)):
        for num in numbers:
            if (i+num)<=target:
                if table[i]!=None:
                    table[i+num]+=1
    return table[target]


if __name__=='__main__':
    print(countSum(4,[1, 2, 3]))
    print(countSum(300,[7, 14]))

