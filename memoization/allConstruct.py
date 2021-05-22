"""Write a function countConstruct(target, wordBank) , the function should
return all the ways that target can be constructed using wordBank.
countConstruct(skateboard,[bo,rd,ate,t,ska,boar])-->None"""
def allConstruct(target,wordBank,memo={}):
    result = []
    if target in memo.keys():
        return memo[target]
    if target=='':
        return [[]]
    for i in range(len (wordBank)):
        if target.startswith(wordBank[i]):
            # cannot use replace because single character
            # can be at different places.
            # check example purple with replace
            temp=target[len(wordBank[i]):]
            ways= allConstruct(temp,wordBank,memo)
            if  len(ways)!=0:
                ways[0].insert(0,wordBank[i])
                result.append(ways[0])

    if len(result)!=0:
        memo[target]=result
        return memo[target]
    else:
        return []

if __name__=='__main__':
    print(allConstruct('abcdef', ['abc', 'cd', 'def', 'f', 'abcdef'],{}))
    print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'],{}))
    print(allConstruct('skateboard', ['bo', 'rd', 'ska', 'te', 'ard'],{}))
    print(allConstruct('teacher', ['tch', 'te', 'er', 'ch'],{}))
    print(allConstruct('abaaba', ['ab', 'aba', 'a', 'abaaba'],{}))
