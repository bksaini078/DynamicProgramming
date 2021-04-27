''' in string SSRSSRS findout the minimum swap so that all alternative is different like RSRSRSR'''

if __name__=='__main__':
    s= 'SRRSRSRS' #answer is 1
    a=0
    b=0
    ls=list(s)
    for i in range(len(s)-1):
        if i%2==0:
            if s[i]=='S':
                a+=1
            else:
                b+=1
        else:
            if s[i]=='S':
                b+=1
            else:
                a+=1
    print(min(a,b))

