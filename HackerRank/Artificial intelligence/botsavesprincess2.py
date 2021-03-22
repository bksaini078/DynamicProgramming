'''ref: https://www.hackerrank.com/challenges/saveprincess2?hr_b=1'''

import sys


def next_move(posr, posc, board):
    print(board[0])
    nearby=[0,0]
    dif=324567
    for i in range(5):
      for j in range(5):
          if board[i][j]=='d':
              print ( i,j,board[i][j] )
              if dif>(abs(i-posr)+abs(j-posc)):
                  print ( i, j, board[i][j] )
                  dif= (i-posr)+(j-posc)
                  nearby[0]=i
                  nearby[1]=j
    print(nearby)
    diff= nearby[0]-posr,nearby[1]-posc
    if diff[0]==0 and diff[1]==0:
      print('CLEAN')
    if abs(diff[0])<=abs(diff[1]) or diff[1]==0:
        # pos_m[0] = pos_m[0] + 1
        if diff[0]<0:
            posr = posr - 1
            print('UP')
        if diff[0]>0:
            posr = posr + 1
            print('DOWN')
    if abs(diff[0])>abs(diff[1]) or diff[0]==0:
        # pos_m[1] = pos_m[1] + 1
        if diff[1]<0:
            posc = posc - 1
            print('LEFT')
        if diff[1]>0:
            posc = posc + 1
            print('RIGHT')


# Tail starts here

if __name__ == "__main__" :
    # pos = [int ( i ) for i in input ().strip ().split ()]
    # board = [[j for j in input ().strip ()] for i in range ( 5 )]
    # pos=[0,0]
    # board = ['bd---', '-d---', '---d-', '---d-', '--d-d']
    # next_move ( pos[0], pos[1], board )
    # pos = [0, 1]
    # next_move ( pos[0], pos[1], board )
    x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
    xy= [i*j for i, j in zip(x,y)]
    print(xy)


#
# if __name__=='__main__':
#     # m = int ( input () )
#     # grid = []
#     # for i in range ( 0, m ) :
#     #     grid.append ( input ().rstrip().strip () )
#     n=5
#     r=2
#     c=3
#     grid=['bd---','-d---','---d-','---d-','--d-d']
#     next_move(pos[0], pos[1], board)

  




