'''
A widget manufacturer is facing unexpectedly hihg demand for its new product.
they would like to satisfy as many customers as possible.
Given a number of widgets available and a list of customer order, what is the maximum number
of orders the manufacturer can fulfull in full
function description:
complete the function filledOrders in the editor below.
the function must return a single integer denoting the maximum possible numer of fulfilled orders.

'''

def order_fillers(order,k):
    if len(order)==0 or k==0:
        return 0
    order.sort()
    max_orders=0
    for item in order:
        if k<=0:
            return max_orders
        if item<=k:
            max_orders+=1
            k-=item
    return max_orders

if __name__=='__main__':

    order=[1,1,3]
    k=3
    print ( order_fillers ( [3, 2, 1], 3 ) )  # Out: 2
    print ( order_fillers ( [3, 2, 1], 1 ) )  # Out: 1
    print ( order_fillers ( [3, 2, 1], 10 ) )  # Out: 3
    print ( order_fillers ( [3, 2, 1], 0 ) )  # Out: 0
    print(order_fillers(order, k))
