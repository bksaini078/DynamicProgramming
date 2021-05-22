if __name__=='__main__':
    input=int(input('Enter number : '))
    # input=6
    table=[0]*(input+1)
    table[1]=1
    for i in range(len(table)-1):
        table[i+1]+=table[i]
        if i!=(len(table)-2):
            table[i+2]+=table[i]
    print(table[-1])
