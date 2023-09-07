# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 11:30:59 2021

@author: user
"""

class Banks():
    bankname='Taipei Bank'
    def __init__(self,uname,money):        
        self.name=uname
        self.balance=money
    def get_balance(self):
        return self.balance
    
hugbank=Banks('hug',100)
print(hugbank.name.title(),hugbank.get_balance())




