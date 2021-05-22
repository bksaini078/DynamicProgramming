'''cansum(7,[4,5,3,7])-->True
cansum(7,[2,4])--> False
write a function that return bool value for array if in array
there is possibility of getting sum equal to argument
given in first place'''
def cansum(n,a):
    table=[False]*(n+1)
    table[0]=True
    for i in range(n+1):
        if table[i]:
            for item in a:
                if i+item<len(table):
                    table[i+item]=True

    return table

if __name__=='__main__':
   print(cansum(7,[4,5,2,7,6]))
   print(cansum(300,[7,14]))