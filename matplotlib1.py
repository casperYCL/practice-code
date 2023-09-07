# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 23:53:26 2021

@author: user
"""
import random
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d imp
'''
x = np.linspace(0,2*np.pi)
y = np.sin(x)
plt.plot(x,y)
plt.show()
x = np.linspace(0,2*np.pi,num=10)   #數量較少較不平滑
y = np.sin(x)
plt.plot(x,y)
plt.show()
'''
'''
x = np.linspace(0,2*np.pi)
y = np.sin(x)
plt.title('y = sin(x) (0<y<1)',fontsize=15)
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.grid(True,color='red',linestyle=':',linewidth=1,alpha=0.5)
ticks=[0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2]
labels=['0','90','180','270','360']
plt.xticks(ticks,labels)
# plt.ylim(0,1)
plt.plot(x,y)
plt.rcParams['font.sans-serif']='Microsoft JhengHei' #中文微軟正黑體
plt.rcParams['axes.unicode_minus']=False
plt.show()
'''
'''
x=np.linspace(0,2*np.pi)
y1=np.sin(x)
y2=np.cos(x)
plt.title('sin(x) and cos(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
ticks=[0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2]
labels=['0','90','180','270','360']
plt.grid(True)
plt.xticks(ticks,labels)
plt.plot(x,y1,color='cyan',label='y=sin(x)')
plt.plot(x,y2,color='magenta',label='y=cos(x)')
plt.legend()
# plt.legend(['y=sin(x)','y=cos(x)'])   法二
plt.show()
'''
'''
x=np.linspace(0,np.pi*2)
y=np.sin(x)                      #figure建立畫布
plt.figure(figsize=(6,8))
plt.plot(x,y)
plt.show() 
'''
'''
x=np.linspace(0,np.pi*2)
y1=np.sin(x)
y5=np.cos(x)                       #分割畫布
y6=np.tan(x)
fig=plt.figure(figsize=(8,6))
ax1=fig.add_subplot(2,3,1)
plt.grid(True)
ax1=plt.plot(x,y1)
ax5=fig.add_subplot(2,3,5)
plt.grid(True)
ax5=plt.plot(x,y5)
ax6=fig.add_subplot(2,3,6)
plt.grid(True)
ax6=plt.plot(x,y6)
ax3=fig.add_subplot(2,3,3)

plt.show()
'''
'''
x=['a','b','c','d','e']
y=[10,20,15,18,22]
fig=plt.figure(figsize=(8,6))
ax1=fig.add_subplot(1,2,1)
plt.title('pic1')
plt.xlabel('eng1')
plt.ylabel('num1')
ax1.bar(x,y,color='c')


ax2=fig.add_subplot(1,2,2)
plt.title('pic2')
plt.xlabel('eng2')
plt.ylabel('num2')
size=[200,400,300,500,600]
ax2.scatter(x,y,color='orange',s=size)
plt.show()
'''
'''
x=['a','b','c','d','e']
y=[10,20,15,18,22]
plt.figure(figsize=(8,6))
plt.subplot(1,2,1)
plt.title('pic1')
plt.xlabel('eng1')
plt.ylabel('num1')
plt.bar(x,y,color='c')


plt.subplot(1,2,2)
plt.title('pic2')
plt.xlabel('eng2')
plt.ylabel('num2')
size=[200,400,300,500,600]
plt.scatter(x,y,color='orange',s=size)
plt.show()
'''
'''
x=np.linspace(0,np.pi*2)        #subplot_adjust調整間距
y1=np.sin(x)                    #for寫法
y5=np.cos(x)
y6=np.tan(x)
fig=plt.figure(figsize=(8,6))
fig.subplots_adjust(wspace=0.5,hspace=0.75)
for i in range(1,7):
    ax=fig.add_subplot(2,3,i)
    if i==1:
        plt.grid(True)
        ax.plot(x,y1)
    elif i==5:
        plt.grid(True)
        ax.plot(x,y5)
    elif i==6:
        plt.grid(True)
        ax.plot(x,y6)

plt.show()
'''   
'''                         #加上標示，設定刻度
x=np.linspace(0,np.pi*2)
y1=np.sin(x)
y5=np.cos(x)
y6=np.tan(x)
fig=plt.figure(figsize=(8,6))
fig.subplots_adjust(wspace=0.5,hspace=0.75)
ticks=[0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2]
labels=['0','90','180','270','360']
for i in range(1,7):
    ax=fig.add_subplot(2,3,i)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_xticks(ticks)
    # ax.set_yticks(ticks)
    ax.set_xticklabels(labels)
    # ax.set_yticklabels(labels)
    if i==1:
        ax.grid(True)
        ax.set_title('y=sin(x)')
        ax.plot(x,y1)
    elif i==5:
        ax.grid(True)
        ax.set_title('y=cos(x)')
        ax.plot(x,y5)
    elif i==6:
        ax.grid(True)
        ax.set_title('y=tan(x)')
        ax.plot(x,y6)
plt.show()
'''
'''
days=np.arange(1,11)    #折線圖，更改折線樣式顏色寬度
weight=np.array([11,15,18,16,19,16,12,14,17,18])
plt.ylim([0,weight.max()+1])
plt.xlabel('Days')
plt.ylabel('Weight')
plt.plot(days,weight,marker='o',markerfacecolor='blue'
          ,linestyle='--',linewidth=2.5,color='orange')
plt.show()
'''
'''                            #堆疊長條圖
x=np.arange(1,7)
y1=np.random.choice(range(0,50),6)
y2=np.random.choice(range(0,50),6)
labels=['apple','orange','grape','pinapple','kiwifruit','banana']
plt.ylim(0,100)
# plt.bar(x,y,tick_label=labels)
plt.bar(labels,y1)
plt.bar(labels,y2,bottom=y1)
plt.legend(('y1','y2'))
plt.show()
'''
'''
#並排長條圖
width=0.25
labels=['a','b','c','d','e']
x1=[x-width/2 for x in range(len(labels))]
x2=[x+width/2 for x in range(len(labels))]
y1=[2,4,7,8,10]
y2=[3,6,9,4,7]
plt.title('Num')
plt.xlabel('Name')
plt.ylabel('Number')
plt.xticks(range(len(labels)),labels=labels)
plt.bar(x1,y1,width,label='first line')
plt.bar(x2,y2,width,label='second line')
plt.legend()
plt.show()
'''   
'''                 
np.random.seed(0)            
data=np.random.randn(10000)  
plt.hist(data,bins='auto',density=True)   
plt.show()
#直方圖，10000亂數，x軸組距自動產生
#randn隨機得到一個數字，可能是負的或正的，可能大於一或小於一，總之就是隨機
#density=y軸為出現機率
'''
'''
np.random.seed(0)   #累積直方圖
data=np.random.randn(10000)
plt.hist(data,bins='auto',density=True,cumulative=True)
plt.show()
'''
'''
np.random.seed(0)         #隨機直方圖點大小，同大小同顏色
x=np.random.randn(100)    #s=size c=cmap 都給ran參數
y=np.random.randn(100)
ran=np.random.choice(np.arange(100),100)
# plt.scatter(x,y,marker='^',color='orange',s=size)
plt.scatter(x,y,s=ran,c=ran,cmap='viridis')
plt.show()
'''
'''
data=[60,20,10,5,3,2] 
labels=['apple','banana','orange','grape','pinapple','strawberry']
explode=[0,0,0,0.2,0.3,0]
plt.pie(data,labels=labels,autopct='%.2f%%',explode=explode,
        shadow=True,startangle=90,labeldistance=1.1)
plt.show()
#圓餅圖,標籤、趴數、往外推、影子
'''
'''                 
t=np.linspace(-2*np.pi,2*np.pi)    #3D圖 
x,y=np.meshgrid(t,t)
z=np.sin(np.sqrt(x**2 + y**2))
fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(x,y,z)
plt.tight_layout()
plt.show()
'''
'''
t=np.linspace(-5,5,num=50)
x,y=np.meshgrid(t,t)
z=x*y
fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(x,y,z,cmap='viridis')  #繪製曲面，指定色系
plt.show()
#繪製曲面 z=高度 座標有不同高度為曲面
'''
'''
fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
xpos=np.arange(10)
ypos=np.arange(10)
zpos=np.zeros(10)
dx=np.ones(10)
dy=np.ones(10)
dz=np.arange(10)+1
ax.bar3d(xpos,ypos,zpos,dx,dy,dz)
plt.show()    #立體長條圖
'''
'''
fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
x=np.random.randn(1000)
y=np.random.randn(1000)
z=np.random.randn(1000)
ax.scatter3D(x,y,z)
plt.show()  #立體散布圖
'''
'''x=['a','b','c','d','e']
y=[10,20,15,18,22]
y1=[11,12,17,12,22]
plt.figure(figsize=(8,4))
plt.axes([0,0,1,1])
plt.title('pic1')
plt.plot(x,y1)

plt.axes([0.4,0.7,0.2,0.2])
plt.title('pic2')
plt.plot(x,y)

plt.axes([0.05,0.4,0.2,0.2])
plt.title('pic3')
plt.plot(x,y)
plt.show()'''
n = ['  Gene3','  is',' [an]','adaptor','molecule','.','[in]','[the]','[Gene5-mediated]','.']
n[0] = n[0][1:]
print(n)












