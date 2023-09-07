# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:52:08 2022

@author: user
"""

import numpy as np
import pandas as pd
import random
'''
#作法一
index=['apple','banana','orange','strawberry','grape']
data1=[5,32,9,40,6]
data2=[4,10,5,62,99]
series1=pd.Series(data1,index=index)
series2=pd.Series(data2,index=index)
df=pd.DataFrame([series1,series2])
print(df)
print('---------------------')
#作法二
data={'fruits':['apple','banana','orange','strawberry','grape'],
      'time':[4,3,8,0,9],
      'year':[2001,2004,2000,2009,2006]}
df1=pd.DataFrame(data)
print(df1)
print('---------------------')
#作法三
order_df=pd.DataFrame([[3,6,0,9,6],
                       [10,35,49,66,35],
                       [49,6,0,19,5]],
                      columns=['apple','banana','orange','strawberry','grape'])
print(order_df)
'''
'''
index=['apple','banana','orange','srrawberry','grape']
data1=[3,65,3,7,6]
data2=[6,10,3,8,56]
series1=pd.Series(data1,index=index)
series2=pd.Series(data2,index=index)
df=pd.DataFrame([series1,series2])
print(df)
print('-------------------------')
df.index=[3,4]
print(df)
print('-------------------------')
df.columns=['A','B',"C",'D','E']
index1=['A','B',"C",'D','E']
print(df)
print('-------------------------')
data3=[5,6,9,4,1]
series3=pd.Series(data3,index=index1)
df=df.append(series3,ignore_index=True)
print(df)
print('-------------------------')
data4=[12,26,53,55,99,0]
index1.append('pinapple')
series4=pd.Series(data4,index=index1)
df=df.append(series4,ignore_index=True)
print(df)
'''
'''
data={'fruits':['apple','banana','orange','strawberry','grape'],
      'years':[2003,1994,2013,2022,2020],
      'time':[2,6,8,3,10]}
df=pd.DataFrame(data)
print(df)
print('---------------------------------------------')
df['price']=[194,499,204,190,448]
print(df)
print('---------------------------------------------')
new_column=pd.Series([29,348,599,3030,10],index=[0,1,2,3,4])
df['column']=new_column
print(df)
print('---------------------------------------------')
new_column=pd.Series([29,348,599,3030,10],index=[0,1,2,6,7])
df['column']=new_column
print(df)
'''
'''
data={'fruits':['apple','banana','orange','grape'],
      'year':[2003,1995,2020,2021],
      'time':[5,7,20,19]}
df=pd.DataFrame(data)
print(df)
print('--------------------------')
df_loc=df.loc[[2,3],['year','time']]
print(df_loc)
'''
'''
np.random.seed(0)
df=pd.DataFrame()
columns=['apple','orange','banana','strawberry','kiwifruit']
for column in columns:
    df[column]=np.random.choice(range(1,11),10)
print(df)
print('---------------------------------------------------------')
df_loc=df.loc[[4,6,8,9],['apple','banana']]
print(df_loc)
print('---------------------------------------------------------')
df_iloc=df.iloc[[3,5,6,7],[1,2,3]]
print(df_iloc)
'''
'''
data={'fruits':['apple','orange','banana','pinapple'],
                'years':[2002,1998,2020,2030],
                'monry':[299,300,499,500]}
df=pd.DataFrame(data)
print(df)
print('------------------------------------')
df_1=df.drop([1,2])  #axis=0
print(df_1)
print('------------------------------------')
df_2=df.drop('years',axis=1)
print(df_2)
'''
'''
df=pd.DataFrame()
columns=['lexus','ford','tesla','luxgen']
for column in columns:
    df[column]=np.random.choice(range(1,10),8)
print(df)
print('-----------------------------')
#df_drop=df.drop([0,2,4,6])
df_drop=df.drop(np.arange(0,8,2))
print(df_drop)
print('-----------------------------')
df_drop=df_drop.drop('ford',axis=1)
print(df_drop)
'''
'''
data={'car':['lexus','honda','tesla','luxgen','lanbojini'],
      'years':[2002,2020,2013,2015,1997],
      'time':[20,34,9,20,109]}
df=pd.DataFrame(data)
print(df)
print('-----------------------------')
df_sort=df.sort_values(by=['time','years'],ascending=True) #先依time排序，time相同比years
print(df_sort)
print('-----------------------------')
print(df.index%2==0)
print(df[df.index%2==0])
print('-----------------------------')
# df=df[df['years']>=2010]
# df=df[df['time']<=30]
df=df.loc[df['years']>=2010][df['time']<=30]
print(df)
'''
'''
def make_random_df(index,columns,seed):
    np.random.seed(seed)
    df=pd.DataFrame()
    for column in columns:
        df[column]=np.random.choice(range(1,101),len(index))
    df.index=index
    return df
columns=['apple','banana','orange']
df_data1=make_random_df(range(1,5),columns,0)
df_data2=make_random_df(range(1,5),columns,1)
print(df_data1)
print(df_data2)
print('串接----------------------------')
df0=pd.concat([df_data1,df_data2],axis=0)#上下串接
print(df0)
print('-------------------------------')
df1=pd.concat([df_data1,df_data2],axis=1)#左右串接
print(df1)
'''
'''
def make_random_df(index,columns,seed):
    np.random.seed(seed)
    df=pd.DataFrame()
    for column in columns:
        df[column]=np.random.choice(range(1,101),len(index))
    df.index=index
    return df
columns1=['apple','banana','orange']
columns2=['grape','pinapple','strawberry']
df_data1=make_random_df(range(1,5),columns1,0)
df_data2=make_random_df(np.arange(1,8,2),columns2,1)
print(df_data1)
print(df_data2)
print('串接----------------------------')
df0=pd.concat([df_data1,df_data2],axis=0)
print(df0)
print('----------------------------')
df1=pd.concat([df_data1,df_data2],axis=1)
print(df1)
'''
'''
def make_random_df(index,columns,seed):
    np.random.seed(seed)
    df=pd.DataFrame()
    for column in columns:
        df[column]=np.random.choice(range(1,101),len(index))
    df.index=index
    return df

columns1=['luxgen','ford','lanbojini']
columns2=['lexus','lanbojini','bmw']
df1=make_random_df(range(1,5),columns1,1)
df2=make_random_df(range(1,5),columns2,2)
df=pd.concat([df1,df2],axis=1,keys=['x','y'])
print(df)
print('----------------------------')
pd_luxgen=df['x','luxgen']    
print(pd_luxgen)
print('----------------------------')
pd_lanbojini=df['x','lanbojini']    
print(pd_lanbojini)
print('----------------------------')
pd_lanbojini=df['y','lanbojini']    
print(pd_lanbojini)
'''
'''
data1={'car':['honda','lanbojini','porsche','bmw'],
       'year':[1998,2022,2014,2019],
       'amount':[6,7,30,28]}
df1=pd.DataFrame(data1)
data2={'car':['honda','lanbojini','porsche','tesla'],
       'year':[1998,2022,2014,2020],
       'price':[200,345,166,109]}
df2=pd.DataFrame(data2)
print(df1)
print('-----------------------------')
print(df2)
print('交集合併-----------------------------')
df=pd.merge(df1,df2,on='car',how='inner')
print(df)
print('聯集合併-----------------------------')
df=pd.merge(df1,df2,on='car',how='outer')
print(df)
'''
'''
order_df=pd.DataFrame([[1000,2526,103],
                       [1001,4352,101],
                       [1002,342,101]],
                      columns=['id','item_id','customer_id'])
customer_df=pd.DataFrame([[101,'Tenaka'],
                         [102,'Suzuki'],
                         [103,'Kato']],
                         columns=['id','name'],)
print(order_df)
print('---------------------------------------------')
print(customer_df)
print('---------------------------------------------')
df=pd.merge(order_df,customer_df,left_on='customer_id',right_on='id',how='inner')
print(df)
'''
'''
order_df=pd.DataFrame([[1000,2526,103],
                       [1001,4352,101],
                       [1002,342,101]],
                      columns=['id','item_id','customer_id'])
customer_df=pd.DataFrame([['Tenaka'],
                         ['Suzuki'],
                         ['Kato']],
                         columns=['name'],)
customer_df.index=[103,101,102]
print(order_df)
print('---------------------------------------------')
print(customer_df)
print('---------------------------------------------')
df1=pd.merge(order_df,customer_df,left_on='customer_id',right_index=True,how='inner')
print(df1)
'''

index=['電鍋','電子鍋','氣炸鍋','蒸烤爐']
data={'單價':[1500,2000,3000,4000],
                 '重量':[3.0,2.5,2.0,5.0],
                 '銷量':[100,20,80,10],
                 '評等':[4.9,4.6,3.9,4.5]}
df=pd.DataFrame(data,columns=['單價','重量','銷量','評等'],
                index=index)
df=df.drop('電子鍋')
print(df)
df.to_csv(r'E:\me\python\df.csv', encoding='utf_8_sig')





    
    
    
    
    
    
    
    
    
    
    
    

