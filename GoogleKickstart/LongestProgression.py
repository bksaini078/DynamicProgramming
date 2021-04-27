n=int (input ())
for k in range (n):
    t=int (input())
    arr=list(map(int,input().split()))
    # code here
    # if already in order
    diff=0
    maxlen=0
    allow=1
    # if not already sorted
    for i in range(1,len(arr)):
        allow=1
        length=2
        diff=arr[i]-arr[i-1]
        print("***i,i-1***",arr[i],arr[i-1],diff)
        for j in range(i+1,len(arr)):
            print ("j,i",arr[j],arr[i])
            if arr[j]-arr[i]==diff:
                length+=1
                print ('j,diff,len,maxlen',j,diff,length,maxlen)
            else:
                if allow==0:
                    # maxlen=max(maxlen,length)
                    break
                else:
                    allow-=1
                    length+=1
                    print ('Allowed, j,diff,len,maxlen',j,diff,length,maxlen)
                    # maxlen=max(maxlen,length)
            maxlen=max(maxlen,length)
            if maxlen==len(arr):
                break

    print("Case #{}:".format(k+1),maxlen)


