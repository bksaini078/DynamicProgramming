#!/bin/python3
'''ref:https://www.hackerrank.com/challenges/botcleanr/problem'''

def nextMove(posr, posc, board):
    #finding position of the dirty
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j]=='d':
          posdr=i
          posdc=j
    if posdr-posr==0 and posdc-posc==0:
      print('CLEAN')
    if abs(posdr-posr)>=abs(posdc-posc):
      if posdr-posr>0 :
        print('DOWN')
      elif posdr-posr<0 :
        print('UP')
    else:
      if posdc-posc>=0 :
        print('RIGHT')
      elif posdc-posc<0 :
        print('LEFT')
    return

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)