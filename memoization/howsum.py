'''howsum(targetSum, numbers)--> combination in numbers array whose sum is equal to targetSum'''
def howsum(n,a,memo={}):
    key=n
    if key in memo.keys():
        return memo[key]
    if n < 0:
        return None
    if n==0:
        return []
    for item in a:
        remain= n-item
        value=howsum(remain,a,memo)
        # print(item)
        if value!=None:
            value.append(item)
            memo[key]=value
            return memo[key]
    memo[key]=None
    return None
if __name__=='__main__':
   print(howsum(8,[4,2,4,2,4,5]))
   print(howsum(300,[7,14]))
