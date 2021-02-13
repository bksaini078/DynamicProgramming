'''
write a function that recieve n records of the laptops battery consumption
and charging events. An events[i] value represents the number of minuste spent charging the
laptop(positive value) or playing a game(a negative value). Every minute, the laptop carges 1% or loses 1% of its energy.
the batterys charge cannot go over 100%. Return the laptops final charge percentage given that the initial
charge is 50%
'''


def gaming_battery(events):
    charge=50
    for i in events:
        charge+=i
        if charge>100:
            charge=100
        if charge<0:
            charge=0
        print(charge)
    return charge

if __name__ == '__main__':
    events=[10,-20,61,-15]
    print(gaming_battery(events))