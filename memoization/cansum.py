'''cansum(7,[4,5,3,7])-->True
cansum(7,[2,4])--> False
write a function that return bool value for array if in array there is possibility of getting sum equal to argument
given in first place'''
def cansum(n,a,memo={},pairs=[]):
    key=n
    if key in memo.keys():
        return memo[key],pairs
    if n < 0:
        return False, None
    if n==0:
        memo[key] = True
        return True, pairs
    for i in range(len(a)):
        remain= n-a[i]
        if cansum(remain,a,memo)[0]==True:
            pairs.append(a[i])
            memo[key]= True
            return memo[key], pairs
    memo[key]= False
    return False, None

if __name__=='__main__':
   print(cansum(7,[4,5,2,6]))
   print(cansum(300,[7,14]))