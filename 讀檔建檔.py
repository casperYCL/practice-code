# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:44:36 2022

@author: user
"""
import os
import shutil

# filepath = input("請輸入路徑:")
# if os.path.exists(filepath):
#     if os.path.isdir(filepath):
#         show=os.path.basename(filepath)
#         print(f"請指定{show}絕對路徑")
#     else:
#         size=os.path.getsize(filepath)
#         show=os.path.basename(filepath)
#         print(f"{filepath}底下的{show}大小為{size/1024}kb")

#C:\Users\user\OneDrive\humen.fasta


os.mkdir("C:\\F1")
os.mkdir("C:\\F1\\F2-1")
os.mkdir("C:\\F1\\F2-2")
os.mkdir("C:\\F1\\F2-1\\F3-1")
os.mkdir("C:\\G1")
shutil.move("C:\\F1\\F2-1","C:\\G1")
shutil.copytree("C:\\F1\\F2-2","C:\\G1\\F2-2")

file=open(r"C:\Users\user\OneDrive\桌面\ch09\abc.txt")
listfile=[]
listfile=file.readlines()
for i in range(5,10): 
    print(listfile[i],end='')

    
#獲取當前路徑
import pathlib
print(pathlib.Path(__file__).parent.absolute())



