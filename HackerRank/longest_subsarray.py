#given an array of integers, what is the lenght of the longest subarray constaining no
# more than two distinct values such that the distinct values differ by no more than 1 ?
# example= arr=[0,1,2,1,2,3]
# answer is 4 [1,2,1,2]

def longest_subarray(arr):
    #two distinct values
    #difference must be 1 or 0
    if len(arr)<1:
        return arr
    sub_arr=[None]
    for i in range(len(arr)):
        temp=[arr[i]]
        for item in arr[i+1:]:
            if abs(arr[i]-item)>1:
                break
            if abs(arr[i]-item)<=1 :
                #two distinct values
                if not(abs(min(temp)-item)>1) or not(abs(max(temp)-item)>0):
                    temp.append(item)
        if len(sub_arr)<len(temp):
            sub_arr= temp
    return sub_arr
if __name__=='__main__':
    arr=[0,1,3,1,4,4,5,6,5,5,6,6,7,8,9,10]
    print(longest_subarray(arr))

