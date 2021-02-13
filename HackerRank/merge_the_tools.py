'''ref:
https://www.hackerrank.com/challenges/merge-the-tools/problem'''



def merge_the_tools(string, k):
    for i in range(k):
        seen=[]
        s1=s[0+i*k:i*k+k]
        temp= ''.join(x for x in s1 if not (x in seen or seen.append(x)))
        print(temp)


    # your code goes here



if __name__ == '__main__':

    s='AAABCADDE'
    s = 'AABCAAADA'
    k=3
    l=abs(len(s)/k)
    # print(s[2:5],l)
    for i in range(k):
        seen=[]
        s1=s[0+i*k:i*k+k]
        set_s1=list(set(s1))
        temp= ''.join(x for x in s1 if not (x in seen or seen.append(x)))
        print(temp)


    # merge_the_tools(s,k)