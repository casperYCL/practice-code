# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:51:10 2022

@author: user
"""

import random as r   #引入Random函式庫，把random稱為r

print('踩地雷遊戲開始。')   #印出遊戲開始

while 1:   #當while 1時，重複執行下面迴圈，直到break跳出迴圈
    num = int(input('請輸入地雷數量：'))  #input讓使用者輸入地雷數量，int轉為整數，存到num變數裡面
    if 0<num<100:   #使用者輸入數字在0到100之內，結束if迴圈，跳到lst那行
        break   #break為跳出迴圈6
    else:
        print('輸入地雷數量錯誤，重新輸入！') #假設使用者輸入超過100或是0負數，跳回num=int(input)那行重新輸入
lst = [0 for x in range(num)]  #做一個串列裡面放num個0，num=[0,0,0,0....0]的意思

while 1:   #當while 1時，重複執行下面迴圈，直到break跳出迴圈
    ans = r.randint(1,100)  #ans為答案變數，r.randint為在1到100內取一個隨機整數，存到ans裡面
    for x in range(num):   #重複迴圈num次，x=1,x=2,x=3....x=num
        while 1:    #當while 1時，重複執行下面迴圈，直到break跳出迴圈
            boom = r.randint(1,100) #boom為炸彈變數，r.randint為在1到100內取一個隨機整數，存到boom裡面
            if boom not in lst: #假如boom這個隨機數字在lst裡面沒有，目的是避免重複的數字
                lst[x] = boom  #將lst的第x個數字改成boom
                break  #跳出第二層這個while迴圈
    if ans not in lst:  #如果ans不在lst裡面，目的是避免答案和炸彈重複
        break  #跳出這個大迴圈

min = 1   #設定最小值變數為1S
max = 100 #設定最大值變數為100

while 1:    #當while 1時，重複執行下面迴圈，直到break跳出迴圈
    usr = int(input('輸入數字：'))  #讓使用者輸入數字，轉成整數格式，存到usr變數裡
    if usr<=min or usr>=max:   #如果使用者輸入數字小於最小值，或是大於最大值，重新輸入
        print('不在範圍內或重複，請重新輸入！')
        continue   #略過下面的if迴圈
    if usr in lst:  #假設輸入數字和lst裡面任何數字重複
        print('踩中地雷了！')
        break    #跳出迴圈
    if usr == ans:   #假設輸入數字和答案相同
        print('答案正確！')
        break  #跳出迴圈
    if usr<ans:   #假設輸入數字小於答案
        min = usr    #最小值改成輸入的數字
        print('數字在%d~%d之間。'%(min,max))  #印出答案在哪兩個數字之間，第一個%d對到的是min，第二個%d對到的是max
    if usr>ans:   #假設輸入數字大於答案
        max = usr   #最大值改成輸入的數字
        print('數字在%d~%d之間。'%(min,max))  #印出答案在哪兩個數字之間，第一個%d對到的是min，第二個%d對到的是max
        
        
        