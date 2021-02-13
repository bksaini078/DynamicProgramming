'''Write a function canconstruct(target, wordBank) , the function should return a boolean indicating whether or not the
target can be constructed by concatenating elements of the wordbank array. We may reuse the wordbank as many times as needed
canConstruct(skateboard,[bo,rd,ate,t,ska,boar])-->False'''

def conConstruct(target, wordBank,memo={}):
    if target in memo.keys():
        return memo[target]
    if len(target)== 0:
        return True
    for item in wordBank:
        if not target.startswith(item):
            continue
        temp= target.replace(item,'')
        if conConstruct(temp,wordBank,memo)==True:
            memo[temp]= True
            return memo[temp]
    memo[target]=False
    return memo[target]
if __name__=='__main__':
    # s=' ' #'abcdef'
    # t=s.replace('a','')
    # print(len(s))
    print(conConstruct('abcdef',['abc','cd','def','f']))
    print(conConstruct('skateboard',['bo','rd','ska','ate','ard']))
    print(conConstruct('teacher',['tch','te','er','ch']))
    print(conConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeee',['-']))
