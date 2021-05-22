def countConstruct(target, wordBank) :
    table=[0]*(len(target)+1)
    table[0]=1
    for i in range(len(target)):
        if table[i]:
            for word in wordBank:
                if word==target[i:i+len(word)]:
                    table[i+len(word)]+=1
    return table[-1]


if __name__ == '__main__':
    print ( countConstruct ( 'abcdef', ['abc', 'cd', 'def', 'f', 'abcdef'] ) )
    print ( countConstruct ( 'purple', ['purp', 'p', 'ur', 'le', 'purpl'] ) )
    print ( countConstruct ( 'skateboard', ['bo', 'rd', 'ska', 'ate', 'ard'] ) )
    print ( countConstruct ( 'teacher', ['tch', 'te', 'er', 'ch']) )
    print ( countConstruct ( 'abaaba', ['ab', 'aba', 'a', 'abaaba']) )