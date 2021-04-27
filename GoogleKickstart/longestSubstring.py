n= int(input())
for j in range(n):
    t=int(input())
    string= input()
    count=[1]
    for i in range(1,len(string)):
        if string[i-1]< string[i]:
            count.append(count[i-1]+1)
        else:
            count.append(1)
    print(count)
    print("Case #{}: ".format(j+1),*count)
