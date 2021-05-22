'''
Python reverse words and Swap cases
example:
rUns dOg--> DoG RuNS
aWeSOME is coDing--> COdING is AwEsome
'''
def reverse_words_order_and_swap_cases(sentence):
    answer=''
    splited= sentence.split(' ')
    print(splited)
    for i in range(len(splited)-1,-1,-1):
        answer=answer+splited[i].swapcase()+' '
    return answer[:-1]

if __name__=='__main__':
    sentence='aWeSOME is coDing'
    print(reverse_words_order_and_swap_cases(sentence))