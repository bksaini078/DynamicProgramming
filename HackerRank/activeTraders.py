'''
An institutional broker wants to review their book of customers to see which are most active.
Given a list of trased by customer name, determine which customers account 
for at least 5% of the total number of trades. Order the list alphabetically ascenting by name. 
example:
n=23
customers=['Bigcorp','Bigcorp','Acme','Bigcorp','Zork','Zork','Abc','Bigcorp',''Acme'','Bigcorp','Bigcorp',
'Zork','Bigcorp','Zork','Zork','Bigcorp','Acme','Bigcorp','Acme','Bigcorp','Acme','Littlecorp','Nadicorp']
 output-->
 ['Acme','Bigcorp','Zork'] becaues these company have crossed 5% trade
 '''

def mostActive(customers):
    arr=[]
    total_trade= len(customers)
    uni_corp= list(set(customers))
    # arr= filter(lambda s: customers.count(s)/total_trade >=0.05, uni_corp)
    for corp in uni_corp:
        count = customers.count(corp)
        if count/total_trade>=0.05:
            arr.append(corp)
    return sorted(arr)

if __name__=='__main__':
    customers = [ 'Bigcorp', 'Acme', 'Bigcorp', 'Zork', 'Zork', 'Abc', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Bigcorp','Zork', 'Bigcorp', 'Zork', 'Zork', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Acme','Littlecorp', 'Nadicorp','Bigcorp', 'Bigcorp', 'Acme', 'Bigcorp', 'Zork', 'Zork', 'Abc', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Bigcorp','Zork', 'Zork', 'Zork', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Acme','Littlecorp', 'Bigcorp', 'Bigcorp', 'Acme', 'Bigcorp', 'Zork', 'Zork', 'Abc', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Bigcorp','Zork', 'Bigcorp', 'Zork', 'Zork', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Acme','Littlecorp', 'Nadicorp','Bigcorp', 'Bigcorp', 'Acme', 'Bigcorp', 'Zork', 'Zork', 'Abc', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Bigcorp','Zork', 'Bigcorp', 'Zork', 'Zork', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Acme','Littlecorp', 'Nadicorp','Bigcorp', 'Bigcorp', 'Acme', 'Bigcorp', 'Zork', 'Zork', 'Abc', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Bigcorp','Zork', 'Bigcorp', 'Zork', 'Zork', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'Bigcorp',
                 'Acme','Littlecorp', 'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp',
                  'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp',
                  'Nadicorp','Littlecorp', 'Nadicorp','Littlecorp', 'Nadicorp']
    arr=[2,2,3,4,5,6]
    print(mostActive(customers))