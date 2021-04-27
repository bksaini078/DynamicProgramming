from collections import deque
import sys
class Node:
    def __init__(self,val):
        self.root=val
        self.right=None
        self.left=None
        # print('root is ',self.root)
    def display(self):
        print(self.root)
        print(self.right)
        print(self.left)
mini = -sys.maxsize - 1
maxi = sys.maxsize
class solution:
    def isBST(self,root,):
        #code here
        return self.isBSTUtil ( root, mini, maxi )

    def isBSTUtil(self,root,mini,maxi):
        if root is None:

            return 1
        #going in left direction
        if root.root<mini or root.root>maxi:
            print(root.root,mini,maxi)
            return 0
        return solution().isBSTUtil(root.right,root.root+1,maxi) and solution().isBSTUtil(root.left,mini,root.root-1)

def LeftBranchView(root):
    # code here
    if root.left is None :
        q=deque()
        q.append(root.root)
        return q
    else:
        x=LeftBranchView(root.left)
        if len(x)>0:
            x.appendleft(root.root)
            return x

def leftView(root):
    max_level=[0]
    return leftViewUtil(root,max_level,1)

def leftViewUtil(root, max_level, level, arr=None):
    if arr is None :
        arr = []
    if root is None:
        return
    if max_level[0]<level:
        arr.append(root.root)
        max_level[0]=level
        # return arr
    leftViewUtil(root.left,max_level,level+1,arr)
    leftViewUtil(root.right,max_level,level+1,arr)
    return arr

def buildTree(s):
    #checking if s in empy
    if len(s)==0 or s[0]=='N':
        return None
    #takings as list not
    s=list(map(str,s.split(' ')))
    # print(s[0])
    #taking root node
    root=Node(int(s[0]))
    #creating a deque
    q= deque()
    q.append(root)
    #increasing the size
    si=1
    i=1
    while si>0 and i<len(s):
        #taking the root node and then deleting it
        currentnode= q[0]
        # print('CurrentNode:',currentnode.root)
        q.popleft()
        # s to make sure only one node is going to be added
        si-=1
        currentvalue= s[i]
        # print('CurrentValue:',currentvalue)
        #for left node
        if currentvalue!='N':
            currentnode.left=Node(int(currentvalue))
            # print('leftNode', currentnode.left.root)
            q.append(currentnode.left)
            si+=1
        i+=1
        #for right node
        if i>=len(s):
            break
        currentvalue=s[i]
        if currentvalue!='N':
            currentnode.right=Node(int(currentvalue))
            # print ( 'rightNode', currentnode.right.root )
            q.append(currentnode.right)
            si+=1
        i+=1
    return root

if __name__=='__main__':
    s= ['2 2 13 7 10 1 10 5 2 N 14 5 11 5 5 13','1 2 3 4 5 6', '2 3 5 6 84 4 5']
    for item in s:
        root=buildTree(item)
        # print ( root.root )
        # print(solution().isBST(root))
        # print(root.root,root.left.root,root.left.left.root,root.left.left.right.root)
        result=leftView(root)
        for item in result:
            print(item, end=' ')
        print( )
    # print(*((LeftBranchView(root))))

    # print(root.left.display())
    # print ( root.right.display () )

