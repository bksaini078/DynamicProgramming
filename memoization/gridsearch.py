# You have grid of size(m,n), and you can move down and right,
# find the number of ways to reach from top left to bottom right in m*n grid
# but here I will be trying recursive method of solving the problem.

def gridsearch(m,n, memo={}):
    key = str(m)+','+str(n)
    if key in memo.keys():
        return memo[key]
    if m==0 or n==0:
        memo[key]= 0
        return 0
    if m==1 and n==1:
        return 1
    else:
        memo[key]= gridsearch(m-1,n,memo)+gridsearch(m,n-1,memo)
        return memo[key]

if __name__=='__main__':
    m=3
    n=3
    print(gridsearch(m,n))


