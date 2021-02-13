'''
finding anagram in the dictionary
example:
dictionary=['hack', a,'rank','khac','ackh','kran','rankhacker','a','ab','ba','stairs','raits']
query=['a','nark','bs','hack','stair']
--> [2,2,0,3,1]
'''
def stringAnagram(dictionary,query):
    arr=[]
    #length must be same
    # must have same number of character
    for que in query:
        i=0
        for word in dictionary:
            if len(que)== len(word):
                if sorted(list(que))==sorted(list(word)):
                    i+=1
        arr.append(i)
    return arr
if __name__=='__main__':
    dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
    query = ['a', 'nark', 'bs', 'hack', 'stair']
    # print(sorted(list(query[1]))==sorted(list(dictionary[2])))
    print(stringAnagram(dictionary,query))
