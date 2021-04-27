def decorator_fucntion(originalFunction):
    func= originalFunction()
    def wrapper():
        print('Executed wrapper function')
        return originalFunction
    return wrapper
def display()
 if __name__=='__main__':
    func1=outer_function('hi')
    func2=outer_function('Bye')
    func1()

