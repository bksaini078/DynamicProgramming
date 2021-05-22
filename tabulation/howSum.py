"""howsum(target,numarr)-->combination of getting target by adding
howSum(7,[5,3,4])-->[4,3]"""

def howSum(target,numarr):
    table=[None]*(target+1)
    table[0]=[]
    for i in range(target-1):
        if table[i] != None :
            for num in numarr:
                    if i+num<=target:
                        table[i+num]=table[i].copy()
                        table[i+num].insert(0,num)



    return table[target]

if __name__=='__main__':
    print(howSum(7,[5,3,4]))
    print(howSum(6,[2,2,2]))
    print(howSum(7, [4, 5, 2, 7, 6]))
    print(howSum(300, [7, 14]))
