'''ref:https://www.hackerrank.com/challenges/absolute-permutation/problem'''
def absolutePermutation(n, k):

    # print(data)
    # print ( data[k:], data[:k] )
    if k==0:
        return list(x for x in range(1,n+1))
    if (n/k)%2==0:
        f = []
        for i in range(1,n,k*2):
            t = list(range(i,i+k*2))
            # print(t)
            f += t[k:] + t[:k]
            # print(f)
        return f
    return [-1]

def absolutePermutation1(n, k):
    if k ==0:
        print(*(range(1,n+1)))
    elif (n/k)%2!=0.0:
        return[-1]
    else:
        arr = []
        for i in range(1,n,k*2):
            d = list(range(i, i+k*2))
            arr+=d[k:]+d[:k]
        return arr

if __name__ == '__main__':

    n=10
    k=5
    print(absolutePermutation(n, k))

