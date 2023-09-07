# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 00:35:21 2021

@author: user
"""



x=int(input())
y=0
for i in range(1,x+1):
    print(' '*(x-i),end='')
    print('*',end='')
    print(' '*((i-1)*2-1),end='')
    print('*'*y,end='')
    y=1
    print()
for i in range(x-1,0,-1):
    print(' '*(x-i),end='')
    print('*',end='')
    print(' '*((i-1)*2-1),end='')
    if i==1:
        y=0
    print('*'*y,end='')
    print()














