
def TreeConstructor(strArr):
    nodes=[]
    uni_n=[]
    result=True
    for item in strArr:
        s= item.replace('(','').replace(')','')
        x= list(map(int,s.split(',')))
        uni_n.append(x[0])
        uni_n.append(x[1])
        nodes.append(list(map(int,s.split(','))))
        # print(nodes)
        # print(uni_n)
    uni_n=list(set(uni_n))
    lenadj= len(uni_n)
    adj_m=[[0]*lenadj for i in range(lenadj)]
    # print(adj_m)
    for node in nodes:
        adj_m[uni_n.index(node[0])][uni_n.index(node[1])]= 1
    # print(adj_m)
    def sum_arr(*args):
        # print(list(map(sum, zip(*args))))
        return list(map(sum, zip(*args)))
    sumrow_list= [0]*lenadj

    for item in adj_m:
        if sum(item)>1:
            return False
        sumrow_list= sum_arr(item,sumrow_list)
    if max(sumrow_list)>2 or max(sumrow_list)==0:
        return False
    else:
        return True

if __name__=='__main__':
    input_1=["(2,5)","(2,6)"]

    print(TreeConstructor(input_1))
