# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:50:22 2022

@author: user
"""
import numpy as np

print(np.array([1,2,3]))
print(np.arange(5))
print(np.arange(1,10,3))
print('--------------')
print(np.linspace(0,1,5))
print(np.zeros(5))
print(np.ones(5))
print('--------------')
print(np.random.rand(5))
print(np.random.randint(1,10,5))
print(np.random.randint(1,10,(2,5))) #z為亂數的形狀
x=['蘋果','香蕉','葡萄','西瓜']
print(np.random.choice(x,2))

'''
arr1=np.array([1,2,3,4,5])
arr2=arr1
arr2[0]=100
print('arr1',arr1)
print('arr2',arr2)
print('-------------------------------')
arr3=np.array([1,2,3,4,5])
arr4=arr3.copy()
arr4[0]=100
print('arr3',arr3)
print('arr4',arr4)
'''
'''
arr=np.arange(10)
print(arr)
arr[1:6]=1
print(arr)
new_arr=arr<5
print(new_arr)
'''
'''
storage=np.arange(5)
print(storage)
storage+=storage
print(storage)
print('----------------------------')
arr_1=np.array([2,4,6,8,10])
arr_2=np.array([1,3,5,7,9])
print('+',arr_1+arr_2)
print('-',arr_1-arr_2)
print('**3',arr_1**3)
print('/',arr_1//arr_2)
'''
'''
arr=np.array([4,-9,16,25,100,-64])
print(arr)
arr_abs=np.abs(arr)
arr_exp=np.exp(arr)
arr_sqrt=np.sqrt(arr_abs)
print(arr_abs)
print(arr_exp)
print(arr_sqrt)
'''
'''
arr_1=np.array([2,5,7,9,5,2])
arr_2=np.array([2,5,8,3,1])
print(arr_1)
print(arr_2)
print('-------------')
new_arr=np.unique(arr_1)
print(new_arr)
print(arr_2)
print('-------------')
print('聯集',np.union1d(new_arr,arr_2))
print('交集',np.intersect1d(new_arr,arr_2))
print('差集',np.setdiff1d(new_arr,arr_2))
'''
'''
arr=np.array([[1,2,3],
              [4,5,6]])
print(arr.sum())    #全部加總
print(arr.sum(axis=0))      #使用axis計算後，2D變1D，軸數由2變1，會軸數縮減
print(arr.sum(axis=1))
print('--------------------')
arr1=np.array([[[0,1,2],
                [3,4,5]],
               
               [[6,7,8],
               [9,10,11]]])
print(arr1.sum())
print(arr1.sum(axis=0))
print(arr1.sum(axis=1))
print(arr1.sum(axis=2))
print('--------------------')
arr0=np.array([1,2,3])
print(arr0.shape) #1D
print(arr.shape)
print(arr1.shape)
print('--------------------')
print(arr.reshape(3,2))
'''

arr=np.array([[1,2,3],
              [4,5,6]])
print(arr[1,2:])
arr1=np.array([[[0,1,2],
                [3,4,5]],
               
               [[6,7,8],
               [9,10,11]]])
print(arr1[1,1,1:])

'''
arr=np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr[[3,2,1]])
print(arr)
print(arr.transpose(1,0))
print('--------------------')
arr1=np.arange(10).reshape(2,5)
print(arr1.transpose(1,0))
print(arr1.T)
'''
'''
arr=np.array([2,6,2,3,0,-5,3,8,4,9,-5,-3,-7])
print(np.sort(arr))
print(arr)
print('------------')
arr.sort()  #改變原陣列
print(arr)
print('------------')
arr=np.array([2,6,2,3,0,-5,3,8,4,9,-5,-3,-7])    #排列後元素在原陣列位置
print(arr.argsort())
'''
'''
x=np.arange(15).reshape(3,5)   #x=[[0,1,2,3,4],       y=[[0,1,2,3,4]
y=np.arange(5)                 #   [5,6,7,8,9],          [0,1,2,3,4] 
z=x-y                          #   [10,11,12,13,14]]     [0,1,2,3,4]]
print(z)
print('-----------')
arr=np.arange(9).reshape(3,3)
print(np.dot(arr,arr))         #3X3矩陣相乘
'''
'''
a=np.array([[1,2,3,4],[4,5,6,7]])
b=np.array([[2,3,4,5],[4,5,6,7]])
c=np.arange(2,10,2)
d=np.linspace(3,10,8)
e=np.random.randint(10,size=(8,6,2))
print(c)
print('-----------')
print(d)
print('-----------')
print(e)
print('-----------')
print(a*b)
print('-----------')
print(a.T)
'''

