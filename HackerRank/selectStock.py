'''This one i got in apple residential intern
saving =250
currentValue=[175,133,109,210,97]
  futureValue=[200,125,128,228,233]
  should return maximum profit
it should be in range
'''
def selectStock(savings,currentValue,futureValue):
    profit=[]
    for i in range(len(currentValue)):
        sum_current = currentValue[i]
        sum_future = futureValue[i]
        if sum_current <= savings :
            profit.append(sum_future - sum_current)
        for j in range(len(currentValue)):
            if i==j:
                continue
            sum_current+=currentValue[j]
            sum_future +=futureValue[j]
            print(i,j,sum_current,sum_future)
            if sum_current <=savings and max(profit)<(sum_future-sum_current) :
                profit.append(sum_future-sum_current)
                print ( 'profit-->', profit )
            else:
                sum_current-=currentValue[j]
                sum_future-=futureValue[j]

    return max(profit)

if __name__=='__main__':
    savings=250
    currentValue=[175,133,109,210,97]
    futureValue=[200,125,128,228,206]
    print(selectStock(savings,currentValue,futureValue))