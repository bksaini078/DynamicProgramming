
def  fib(n):
    if n>=2:
        # print(n)
        return fib(n-1)+fib(n-2)
    else:
        return n

if __name__ == '__main__':
    n=int(input('please enter the number: '))
    for i in range(n):
        # print(i)
        print(fib(i))


