"""Write a function countConstruct(target, wordBank) , the function should
return number of ways that target can be constructed using wordBank.
countConstruct(skateboard,[bo,rd,ate,t,ska,boar])-->None"""


def countConstruct(target, wordBank, memo={}) :
    count = 0
    if target in memo.keys () :
        return memo[target]
    if len ( target ) == 0 :
        return 1
    for item in wordBank :
        if target.startswith ( item ) :
            temp = target.replace ( item, '' )
            count += countConstruct ( temp, wordBank, memo )
            memo[temp] = count
    return count


if __name__ == '__main__':
    print ( countConstruct ( 'abcdef', ['abc', 'cd', 'def', 'f', 'abcdef'],{} ) )
    print ( countConstruct ( 'purple', ['purp', 'p', 'ur', 'le', 'purpl'],{} ) )
    print ( countConstruct ( 'skateboard', ['bo', 'rd', 'ska', 'ate', 'ard'],{} ) )
    print ( countConstruct ( 'teacher', ['tch', 'te', 'er', 'ch'],{} ) )
    print ( countConstruct ( 'abaaba', ['ab', 'aba', 'a', 'abaaba'],{} ) )
