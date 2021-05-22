'''bestsum(7,[5,3,4,7])-->7
bestsum should return the shortest sum possible from the array'''
def bestSum(target,numarr):
    table= [None]*(target+1)
    table[0]=[]
    for i in range(len(table)):
        if table[i]!=None:
            for num in numarr:
                if i+num<=target:
                    temp=table[i].copy()
                    temp.insert(0,num)
                    if table[i+num]==None or len(table[i+num])>len(temp):
                        table[i+num]=temp
                        # table[i+num].insert(0,num)
                    # print(table)
    return table[-1]




if __name__=='__main__':
    print(bestSum(7,[5,3,4,2]))
    print(bestSum(6,[2,2,2]))
    print(bestSum(7, [4, 5, 2, 7, 6]))
    print(bestSum(300, [7, 14]))
    print(bestSum(100,[1,12,2,4,5,25,50]))
