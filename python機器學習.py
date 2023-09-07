# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
"""
Created on Mon Jan 17 13:58:58 2022

@author: user
"""
'''
animal=['dog','cat','monkey','bird','elephant']
for index,item in enumerate(animal):
    print('item',index,'=',item)
print(list(enumerate(animal)))
'''
'''
index=['a','b','c','d','e']
animal=['dog','cat','monkey','bird','elephant']
print(list(zip(index,animal)))
a=list(zip(index,animal))
for i,j in enumerate(zip(index,animal)):
    print(i,j)
for i,j in zip(index,animal):
    print(i,j)
'''
'''
fruits={
        'apple':'red',
        'banana':'yellow',
        'papaya':'orange'}
for name,color in fruits.items():
    print(name,'is',color)
'''
'''
number=[1,2,3,4,5,2]
print(list(reversed(number)))    
print(number)
number.reverse()
print(number)
print(number.count(2))
text='banana'
print(text.count('n'))
print(number.index(2))
print(number.index(4))
print(text.index('a'))
'''
'''
fruits={
        'apple':1,
        'banana':3,
        'papaya':2}
for  name,num in fruits.items():
    print('{}有{}個'.format(name,num))
print()
for  name,num in fruits.items():
    print(f'{name}有{num}個')  
'''
'''
def mod(a,b):
    q=a*b
    r=a/b
    return q,r
x,y=mod(20,6)
print(x)
print(y)
'''
'''
def sing(name='無名氏',verb='發呆'):
    print('{}請{}'.format(name,verb))
sing('daisy','唱歌')
sing(verb='休息',name='casper')
sing('小華')
sing(verb='跳舞')
sing()
'''
'''
import datetime
now=datetime.datetime.now()
print(now)
print(now.ctime())
'''
'''
class Myproduct:
    def __init__(self,n,p):
        self.name = n
        self.price = p
        
    def summary(self):
        print('{}的折扣價格是{}'.format(self.name,self.price))
    
    def discount(self,rate):
        self.price *= rate
        self.price=int(self.price)
    
book=Myproduct('書',700)
print(book)
print(book.name)
print(book.price)
book.discount(0.5)
book.summary()
'''
'''
import datetime as dt
x=dt.datetime(2022,1,22)
print(x)
x=dt.datetime(year=2022,month=1,day=22)
print(x)
x=dt.datetime(2022,1,22,12,26,55)
print(x)
print()
y=dt.timedelta(hours=1,minutes=5)
print(y)
y=dt.timedelta(days=1,seconds=5)
print(y)
print()
x=dt.datetime(2022,1,22,12,26,55)
print(x) 
y=dt.timedelta(hours=1,minutes=5)
print(y)
print(x+y)    
print(x-y)    
print(x+y*2)  
print()
x=dt.datetime(2022,1,22,12,26,55)
print(x) 
s1=x.strftime('%Y/%m/%d %H-%M-%S')
print(s1)   
s2=x.strftime('%Y年%m月%d日 %H小時%M分鐘%S秒')
print(s2)  
print()
s='2022/01/22 12-26-55'
x=dt.datetime.strptime(s,'%Y/%m/%d %H-%M-%S')   #格式和字串s相同
print(x)    #將時間資料匯入python後是字串型別，轉成datetime方便運算
print(type(x))
'''
'''
import re
sentence='ha_p_py,hi.hi.hi,me/me,t.t'
print(sentence.split(','))
list1=re.split('[_./,]',sentence)
print(list1)
'''
'''
a=[-1,3,-5,0,6,9,-4]
new=list(map(abs,a))
print(a)
print(new)
print()
eng=['dae','rgsdf','htr']
new1=list(map(str.upper,eng))
print(eng)
print(new1)
print()
eng=['dae','e','rgsdf','htr','ef','fhghrt']
new1=list(filter(lambda x: len(x)>=3,eng))
print(eng)
print(new1)
'''
'''
list1=['this','is','a','sentence']
print(list1)
print(sorted(list1,key=len,reverse=False))
print(sorted(list1,key=len,reverse=True))
print()
num=[
     [0,9],
     [1,8],
     [2,7],
     [3,6]]
print(sorted(num))
print(sorted(num,key=lambda x:x[1],reverse=False))
print(sorted(num,key=lambda x:x[1],reverse=True))
'''
'''
a=[1,-3,5,-5,-6,-2,9]
print([abs(x) for x in a])
print([x**2 for x in a])
b=['this','is','a','sentence']
print([s.upper() for s in b])
a=[1,-3,5,-5,-6,-2,9]
print(a)
print([abs(x) for x in a if x>0])
b=['this','is','a','sentence']
print([s.upper() for s in b if len(s)>3])
'''
'''
a=[1,-2,3,4,-5]
b=[9,-8,-7,6,5]
print([[x,y] for x,y in zip(a,b)])
print([x+y for x,y in zip(a,b)])
print([x+y 
       for x,y in zip(a,b)
       if x+y>0])
'''
'''
a=[1,2,3]
b=['A','B']
r=[]
for x in a:
    for y in b:
        r.append([x,y])
print(r)
print([[x,y] for x in a for y in b])

n1=[0,1]
n2=[0,1]
n3=[0,1]
print([x*2**2+y*2**1+z*2**0 for x in n1 for y in n2 for z in n3])        
'''
'''
from collections import defaultdict
lst=['foo','bar','pop','foo','bar','foo']
b=defaultdict(int)
for item in lst:
    b[item]+=1
print(b)

prices=[['grape',500],
        ['banana',150],
        ['guava',200],
        ['banana',400],
        ['grape',600],
        ['banana',100],
        ]
fruits=defaultdict(list)
for name,price in prices:
    fruits[name].append(price)
for name,prices in fruits.items():
    print(name,prices)
'''
'''
from collections import Counter
lst=['foo','bar','pop','foo','bar','foo']
c=Counter(lst)
print(c)
for item,counter in c.items():
    print(item,'出現',counter,'次')
print('出現最多次',c.most_common(1))     #回傳前N個出現最多次的元素 
'''
























