# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:51:20 2022

@author: user
"""
import os
def cutfile(name,numbers):
    if os.path.exists(name):
        if os.path.isfile(name):
            file = open(name)
            listfile=[]
            listfile = file.readlines()
            file.close()
            if len(listfile) >= numbers:
                road = os.path.dirname(name)
                basename = os.path.basename(name)
                filename = os.path.splitext(basename)[0]
                usename = road +"\\"+ filename + '-' + str(numbers) + '.txt' 
                # os.mknod(usename)
                usename = open(usename,'w+')
                for i in range(numbers):
                    usename.write(listfile[i]+'\n')
                usename.close()
            else:
                print('行數不足')
            
        else:
            print('此路徑非檔案，請重新輸入')
    else:
        print('檔案不存在')
    
for j in range(3):
    name = input('請輸入檔名路徑:')
    number = int(input('請輸入數字:'))
    cutfile(name,number)
