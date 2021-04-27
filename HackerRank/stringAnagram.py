'''
finding anagram in the dictionary
example:
dictionary=['hack', a,'rank','khac','ackh','kran','rankhacker','a','ab','ba','stairs','raits']
query=['a','nark','bs','hack','stair']
--> [2,2,0,3,1]
'''
import time
from collections import Counter
def stringAnagram1(dictionary,query):
    time1= time.time()
    arr=[]
    d1= Counter(''.join(sorted(x)) for x in dictionary)
    q1= list(''.join(sorted(x)) for x in query)
    # print(d1)
    for q in q1:
        if q in d1.keys():
            arr.append(d1[q])
        else:
            arr.append(0)
    print(time.time()-time1)
    print(d1.keys(q1))
    return arr

def stringAnagram(dictionary,query):
    time1= time.time()
    arr=[]
    for que in query:
        i=0
        for word in dictionary:
            if sorted(list(que))==sorted(list(word)):
                    i+=1
        arr.append(i)
    print(time.time()-time1)
    return arr
if __name__=='__main__':
    dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
    query = ['a', 'nark', 'bs', 'hack', 'stair']
    # print(sorted(list(query[1]))==sorted(list(dictionary[2])))
    print ( stringAnagram ( dictionary, query ) )
    print(stringAnagram1(dictionary,query))
