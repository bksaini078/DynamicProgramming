'''This one i got in apple residential intern
locations[1,1,1]-->1
range min=max(i-locations[i],1) , max=min(i+locations[i],n)
it should be in range
'''

def foundationActivation(locations):
    n=len(locations)
    foundations=[]
    ran=[1,n]
    l_ran=[]
    for i in range(1,n+1):
        mi=max(i-locations[i-1],1)
        ma=min(i+locations[i-1],n)
        if ran==[mi,ma]:
            return 1
        l_ran.append([mi,ma])
    # print('l_ran-->',l_ran)
    #now checking with the range
    temp_ran=[]
    for i in range(0,len(l_ran)):
        # print('l_ran-->',l_ran)
        count=1
        for j in range(i+1,len(l_ran)):
            # print('foundations-->',foundations)
            # print ( 'l_ran1-->', l_ran,j )
            if l_ran[i][0]>l_ran[j][0]:# or l_ran[i][1]>l_ran[j][1]:
                if l_ran[i][1]<l_ran[j][1]:
                    count+=1
                    # print('count1-->',count)
                    l_ran[i][0]=l_ran[j][0]
                    l_ran[i][1]=l_ran[j][1]
                else:
                    count+=1
                    # print ( 'count2-->', count )
                    l_ran[i][0] = l_ran[j][0]
            if l_ran[i][1]<l_ran[j][1]:
                if l_ran[i][0]>l_ran[j][0]:
                    count+=1
                    l_ran[i][0]=l_ran[j][0]
                    l_ran[i][1]=l_ran[j][1]
                    # print ( 'count3-->', count )
                else:
                    count+=1
                    # print ( 'count4-->', count )
                    l_ran[i][1] = l_ran[j][1]
            # print('count-->',count)
            print(l_ran)
        if ran==[l_ran[i][0],l_ran[i][1]]:
            foundations.append(count)
    return min(foundations)

#much better approach
def foundationActivation1(locations):
    n = len ( locations )
    goal = [True] * n
    foundations=[]
    for i in range(n):
        count=0
        table = [False] * n
        mi_1=max(i-locations[i]+1,1)
        ma_1=min(i+locations[i]+1,n)
        t= [True]*((ma_1-mi_1)+1)
        table[mi_1-1:ma_1]=t
        if goal==table:
            return 1
        else:
            count += 1
            for j in range(n):
                if i==j:
                    continue
                mi_2 = max(j - locations[j]+1, 1)
                ma_2 = min(j + locations[j]+1, n)
                t = [True] * ((ma_2 - mi_2) + 1)
                if ma_2<ma_1 or ma_2>ma_1:
                    table[mi_2 - 1 :ma_2] = t
                    count+=1
                if goal == table :
                    foundations.append(count)

    if len(foundations)==0:
        return None
    else:
        return min(foundations)

if __name__=='__main__':
    locations=[2,0,0,0]
    # print('result-->',foundationActivation(locations))
    print ( 'result-->', foundationActivation1( locations ) )