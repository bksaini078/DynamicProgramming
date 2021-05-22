'''ref: https://www.hackerrank.com/challenges/saveprincess/problem'''

import sys

def displayPathtoPrincess(n, grid) :
    print(grid)
    #finding position of m and p
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='m':
                pos_m= [i,j]
            if grid[i][j]=='p':
                pos_p=[i,j]
    # print(pos_m,pos_p)
    while not(pos_m[0]==pos_p[0] and pos_m[1]== pos_p[1]):
        diff= pos_p[0]-pos_m[0],pos_p[1]-pos_m[1]
        # print(pos_m,pos_p)
        # print('diff',diff)
        if abs(diff[0])<=abs(diff[1]) or diff[1]==0:
            # pos_m[0] = pos_m[0] + 1
            if diff[0]<0:
                pos_m[0] = pos_m[0] - 1
                print('UP')
            if diff[0]>0:
                pos_m[0] = pos_m[0] + 1
                print('DOWN')
        if abs(diff[0])>abs(diff[1]) or diff[0]==0:
            # pos_m[1] = pos_m[1] + 1
            if diff[1]<0:
                pos_m[1] = pos_m[1] - 1
                print('LEFT')
            if diff[1]>0:
                pos_m[1] = pos_m[1] + 1
                print('RIGHT')

    return None

if __name__=='__main__':
    # m = int ( input () )
    # grid = []
    # for i in range ( 0, m ) :
    #     grid.append ( input ().rstrip().strip () )
    m=7
    grid=['-------', '------m', '-------','-------','-------','-------','p------']
    displayPathtoPrincess ( m, grid )






