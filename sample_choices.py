# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:22:57 2022

@author: user
"""

import random 

def count(numbers,uses):
    for i in range(1,11):
        for j in range(1000):
            for k in range(3):
                if numbers[j][k]==i:
                    n=uses.get(i)
                    uses[i]=n+1
    return uses
    

number=[]
use={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
for m in range(1000):
    num=random.sample(range(1,11),3)
    number.append(num)
use=count(number,use)
print("sample 1000次結果",use)
print('--------------------------------------------------------------------------')
number=[]
use={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
for n in range(1000):
    num=random.choices(range(1,11),k=3)
    number.append(num)
use=count(number,use)
print("choice 1000次結果",use)







