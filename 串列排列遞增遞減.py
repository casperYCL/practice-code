# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:33:29 2022

@author: user
"""

time=int(input('數字數量='))
numlist=[]
uplist=[]
conti=True
      
for i in range(1,time+1):
    num=int(input(f"請輸入第{i}個數字:"))
    numlist.append(num)

while conti==True: 
    arr=input("(o)原數序列、(a)遞增序列、(q)遞減序列?")
    if arr=='o':
        for j in range(time):
            print(f"第{j+1}個數為{numlist[j]}")
        yn=input('是否繼續(y/n)')
    elif arr=='a':
        uplist=sorted(numlist)
        for j in range(time):
            print(f"第{j+1}個數為{uplist[j]}")
        yn=input('是否繼續(y/n)')
    else :
        uplist=sorted(numlist)
        uplist=uplist[::-1]
        for j in range(time):
            print(f"第{j+1}個數為{uplist[j]}")
        yn=input('是否繼續(y/n)?')
    
    if yn=='n':
        conti=False


































