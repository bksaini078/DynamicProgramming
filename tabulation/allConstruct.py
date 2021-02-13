"""Write a function countConstruct(target, wordBank) , the function should
return all the ways that target can be constructed using wordBank.
countConstruct(skateboard,[bo,rd,ate,t,ska,boar])-->None"""

def allConstruct(target, wordBank) :
    table=[[]]*(len(target)+1)
    table[0]=[[]]

    for i in range(len(target)):
        if len(table[i])!=0 and i < len(target):
            for word in wordBank:
                if word==target[i:i+len(word)]:
                    subarr=table[i]
                    # print(subarr)
                    # print(table)
                    subarr[0].insert(0,word)
                    # [x.insert(0,word) for x in subarr]
                    table[i+len(word)]=subarr

                    table[i] = [[]]

    return table[-1]


if __name__ == '__main__':
    print ( allConstruct ( 'abcdef', ['abc', 'cd', 'def', 'f', 'abcdef'] ) )
    print ( allConstruct ( 'purple', ['purp', 'p', 'ur', 'le', 'purpl'] ) )
    print ( allConstruct ( 'skateboard', ['bo', 'rd', 'ska', 'ate', 'ard'] ) )
    print ( allConstruct ( 'teacher', ['tch', 'te', 'er', 'ch'] ) )
    print ( allConstruct ( 'abaaba', ['ab', 'aba', 'a', 'abaaba'] ) )