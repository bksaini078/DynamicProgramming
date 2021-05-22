'''Write a function canconstruct(target, wordBank) , the function should return a boolean indicating whether or not the
target can be constructed by concatenating elements of the wordbank array. We may reuse the wordbank as many times as needed
canConstruct(skateboard,[bo,rd,ate,t,ska,boar])-->False'''

def canConstruct(target,wordBank):
    table=[False]*(len(target)+1)
    table[0]=True

    for i in range(len(table)):
        if table[i] and i<len(target):
            for word in wordBank:
                if word==target[i:i+len(word)]:
                    table[i+len(word)]=True
    return table[-1]

if __name__=='__main__':
    print ( canConstruct ( 'abcdef', ['abc', 'bac', 'def', 'f'] ) )
    print ( canConstruct ( 'skateboard', ['boa', 'rd', 'sk', 'ate', 'ard'] ) )
    print ( canConstruct ( 'teacher', ['tch', 'te', 'er', 'ch'] ) )
    print ( canConstruct ( 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeee', ['-'] ) )
    print ( canConstruct ( 'abcdef', ['abc', 'cd', 'def', 'f', 'abcdef'] ) )
    print ( canConstruct ( 'purple', ['purp', 'p', 'ur', 'le', 'purpl'] ) )
    print ( canConstruct ( 'skateboard', ['bo', 'rd', 'ska', 'ate', 'ard'] ) )
    print ( canConstruct ( 'teacher', ['tch', 'te', 'er', 'ch']) )
    print ( canConstruct ( 'abaaba', ['ab', 'aba', 'a', 'abaaba'] ) )