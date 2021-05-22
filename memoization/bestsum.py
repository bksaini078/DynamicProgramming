'''bestsum(7,[5,3,4,7])-->7
bestsum should return the shortest sum possible from the array'''

def bestsum(n,a):
    short_com= None
    pair=[]
    if n==0:
        return []
    if n<0:
        return None
    for item in a:
        remain= n-item
        value=bestsum(remain, a)
        if value!=None:
            value.append(item)
            short=value
            pair.append(value)
            if short_com==None or (len(short)< len(short_com)):
                short_com=short

    return short_com

if __name__=='__main__':
   print(bestsum(8,[2,2,6,5]))
   # print(bestsum(300,[7,14]))
