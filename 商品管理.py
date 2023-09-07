# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:21:22 2022

@author: user
"""
number=0
product={}
print('=======DTC產品管理系統=======')
while True:
    choose=int(input('系統功能-> 1.新增 2.修改 3.刪除 4.查詢 5.產品列表 其他.離開'))
    if choose==1:
        number=input('編號:')
        if number not in product:
            name=input('品名:')
            price=int(input('單價:'))
            product[number]=[name,price]
            print('產品新增成功!')
        else:
            print('已有此產品')
    elif choose==2:
        number=input('編號:')
        if number not in product:
            print('無此產品')
        else:
            name=input('品名:')
            price=int(input('單價:'))
            product[number]=[name,price]
            print('產品修改成功!')
    elif choose==3:
        number=input('編號:')
        if number not in product:
            print('無此產品')
        else:
            del product[number]
            print('產品刪除成功!')
    elif choose==4:
        number=input('編號:')
        if number not in product:
            print('編號   品名   單價')
        else:
            use=product.get(number)
            print('編號   品名   單價')
            print(number,use[0],use[1],sep='\t')
    elif choose==5:
        print('編號','品名','單價')
        for itname,item in product.items():
            print(itname,item[0],item[1],sep='\t')
    else:
        break
        