def hanoi(disk,source,middle,destination):
    if disk==0:
        print('Moving disk %s from %s to %s'%(disk,source,destination))
        return
    hanoi(disk-1,source,destination,middle)
    print('Moving disk %s from %s to %s'%(disk,source,destination))
    hanoi(disk-1,middle,source,destination)
def hanoi_iteration(source,middle,destination):
    target= source
    i=0
    print(source,middle,destination)
    while  destination !=target:
        if i%3==0:
            source-=1
            destination+=1
            print(source,middle,destination)
        if i%3==1 :
            if i%2==0:
                source+=1
                middle-=1
            if i%2==1:
                source-=1
                middle+=1
            print(source,middle,destination)
        if i%3==2:
            if i % 2 == 0 :
                middle += 1
                destination -= 1
            if i % 2 == 1 :
                middle -= 1
                destination += 1
            print(source,middle,destination)
        i+=1


if __name__ == '__main__':
    hanoi_iteration(3,0,0)
