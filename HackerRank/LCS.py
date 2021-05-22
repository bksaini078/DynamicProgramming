'''Longest Common Subsequence Problem
ref:https://www.techiedelight.com/longest-common-subsequence/
'''

def LCSlength_recur(str1,str2):
    '''solution using recursion'''
    len_1= len(str1)
    len_2= len(str2)
    if len_1==0 or len_2==0:
        return 0
    if str1[len_1-1]==str2[len_2-1]:
        return LCSlength_recur(str1[:-1],str2[:-1]) +1
    return max(LCSlength_recur(str1[:-1], str2), LCSlength_recur(str1,str2[:-1]))

def LCSlength_tab(str1,str2):
    '''solution using tabulation'''
    table=[[None]*(len(str1)+1) for i in range(len(str2)+1)]
    table[0][0]=0
    str1=" "+str1
    str2= " "+str2
    #row
    for i in range(len(str2)):
        #column
        for j in range(len(str1)):
            # when char are empty
            if str1[j]==" " or str2[i]== " ":
                table[i][j]=0
            #when char matches
            elif str2[i]==str1[j]:
                table[i][j]= table[i-1][j-1]+1
            # when char does not match
            elif str2[i]!=str1[j]:
                table[i][j]=max(table[i][j-1], table[i-1][j])

    return table[-1][-1]

if __name__ == '__main__':
    A="ABCBDAB"
    B='BDCABA'
    print(LCSlength_recur(A,B))
    print(LCSlength_tab(A,B))
