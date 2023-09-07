# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:35:42 2022

@author: user
"""
class Student():
    school_name='成功高中'
    def __init__(self,name,s_id,s_class):
        self.name=name
        self.s_id=s_id
        self.s_class=s_class
        self.scoredict={}
        self.s_sum=0
    def addscore(self,classname,score):
        if classname not in self.scoredict:
            if 0<=score<=100:
                self.scoredict[classname]=score
            else:
                print('分數錯誤')
        else:           
            print('已有此課程') 
            
    def delscore(self,classname,score):
        if classname in self.scoredict:
            del self.scoredict[classname]
        else:
            print('無此課程')
            
    def showscore(self):
        print(f'{self.name} 學期分數如下:')
        for key,item in self.scoredict.items():
            print(f"{key}:{item}分")
            
    def calcAverage(self):
        for item in self.scoredict.values():
            self.s_sum+=item
        Average=self.s_sum//len(self.scoredict)
        print(f"{len(self.scoredict)}科總平均是{Average}分")
        
    def printStudentinfo(self):
        print(f"學校:{self.school_name}")    
        print(f"姓名:{self.name}")
        print(f"學號:{self.s_id}")
        print(f"班級:{self.s_class}")
        
    def printbest(self):
        use={}
        ans={}
        for key,item in self.scoredict.items():
            use[key]=item
        for key,item in use.items():
            j=0
            for key1,item1 in use.items():
                if use[key]>=item1:
                    j+=1
            if j==len(use):
                ans[key]=item
        for key,item in ans.items():
            print(f"最高分為{key},分數為{item}分")
            
    def printworst(self):
        use={}
        ans={}
        for key,item in self.scoredict.items():
            use[key]=item
        for key,item in use.items():
            j=0
            for key1,item1 in use.items():
                if use[key]<=item1:
                    j+=1
            if j==len(use):
                ans[key]=item
        for key,item in ans.items():
            print(f"最低分為{key},分數為{item}分")
 
    
  
    
            
casper=Student('casper',110025001,'A')
casper.addscore('English',90)
casper.addscore('Math',65)
casper.addscore('physis',65)
casper.addscore('Chinese',65)
casper.addscore('Science',95)
casper.delscore('Chinese',65)
casper.showscore()

print('--------------------------------------------------')

john=Student('王大明', 1103455, 105)
john.addscore('English', 60)
john.addscore('Chinese', 100)
john.addscore('Math',60)
john.printStudentinfo()
john.printbest()
john.printworst()
john.calcAverage()

     











