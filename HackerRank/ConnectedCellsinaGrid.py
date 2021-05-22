'''ref:https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem'''
import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):
    result=[]
    #n * m matrix
    n = len ( matrix )  # row
    m= len(matrix[0]) #column
    # print('n,m->',n,m)
    dict={}
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                if i==0 and j==0:
                    dict[matrix[i][j]] = [i, j]
                    continue
                if i==0 and 0<j<=m-1:
                    matrix[i][j] += matrix[i][j - 1]
                    dict[matrix[i][j]] = [i, j]
                if (0<i<=n-1 and j==0) :
                    matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j + 1] )
                    dict[matrix[i][j]] = [i, j]
                if 0<i<n-1 and j==m-1:
                    matrix[i][j] += max(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
                    dict[matrix[i][j]] = [i, j]
                if 0<i<n-1 and 0<j<m-1:
                    matrix[i][j] += max(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1],
                                          matrix[i][j - 1])
                    dict[matrix[i][j]] = [i, j]
                if i==n-1 and 0<j<m-1:
                    matrix[i][j] += max(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1],
                                          matrix[i][j - 1])
                    dict[matrix[i][j]] = [i, j]
                if i==n-1 and j==m-1:
                    matrix[i][j] += max(matrix[i - 1][j - 1], matrix[i - 1][j],
                                          matrix[i][j - 1])
                    dict[matrix[i][j]] = [i, j]
                print(matrix)

    # result= max([max(x) for x in matrix])
    result= max(dict.keys())
    return result

if __name__ == '__main__':
    # matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1,1,1,1]]
    # result = connectedCell(matrix)
    # print(result)
    # matrix = [[1, 1, 0 ], [1, 0, 0], [1, 0, 1]]
    # result = connectedCell(matrix)
    # print ( result )
    matrix = [[0, 1, 1, 1,1],[1,0, 0, 0, 1],[1, 1, 0,1, 0],[0,1,0,1,1],[0,1,1,1,0]]
    result = connectedCell ( matrix )
    print ( result )

'''
0 1 1 1 1
1 0 0 0 1
1 1 0 1 0
0 1 0 1 1
0 1 1 1 0'''