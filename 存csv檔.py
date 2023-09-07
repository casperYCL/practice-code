# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:10:46 2022

@author: user
"""
'''
import matplotlib.pyplot as plt
x=['a','b','c','d','e']
y=[10,20,15,18,22]
plt.figure(figsize=(8,4))
plt.axes([0,0,0.4,1])
plt.subplots_adjust(wspace=0.5,hspace=0.75)
plt.subplot(2,2,1)
plt.axes(0.5,0.4,1)
plt.title('pic1')
plt.pie(y,labels=x,labeldistance=1.1,autopct='%.2f%%')
plt.subplot(2,2,2)
plt.title('pic2')
plt.plot(x,y)'''


'''
import numpy as np
import sklearn
#from sklearn.model_selection import train_test_split
#print(111)



import pandas as pd
index=['電鍋','電子鍋','氣炸鍋','蒸烤爐']
data={'單價':[1500,2000,3000,4000],
                 '重量':[3.0,2.5,2.0,5.0],
                 '銷量':[100,20,80,10],
                 '評等':[4.9,4.6,3.9,4.5]}
df=pd.DataFrame(data,columns=['單價','重量','銷量','評等'],
                index=index)
df=df.drop('電子鍋')
print(df)
df.to_csv(r'C:\me\python\df.csv', encoding='utf_8_sig')
'''
#進度條tdqm
from time import sleep

temp = 0
total = 1000

for n in range(1000):
    temp += 1
    print('\r' + '[Progress]:[%s%s]%.2f%%;' % (
    '█' * int(temp*20/total), ' ' * (20-int(temp*20/total)),
    float(temp/total*100)), end='')
    sleep(0.01)