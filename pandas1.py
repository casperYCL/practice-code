# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:51:41 2022

@author: user
"""
import numpy as np
import pandas as pd
from numpy import nan
import random
'''
idx=['banana','apple','guava','orange']
data=[1,4,3,2]
series=pd.Series(data,index=idx)
print(series)
print(series.shape)
series=pd.Series(data) #沒設定index從0開始排
print(series)
print(series.shape)
print('-----------------------')
fruits={'orange':2,'banana':3,'grape':1,'peach':5}
print(pd.Series(fruits))
fruits_series=pd.Series(fruits)
print('-----------------------')
print(fruits_series[0:2])
print('-----------------------')
print(fruits_series[['banana','peach']])
print('-----------------------')
print(fruits_series.index)
print(fruits_series.values)
'''
'''
idx=['banana','apple','guava','orange']
data=[1,4,3,2]
series=pd.Series(data,index=idx)
print(series)
print('----------------')
pinapple=pd.Series([12],index=["pinapple"])
#pinapple=pd.Series({"pinapple":12})另一種寫法
series=series.append(pinapple)
print(series)
print('----------------')
series=series.drop("banana")
print(series)
'''
'''
idx=['apple','banana','grape','pinapple','orange']
data=[4,6,0,1,9]
series=pd.Series(data,index=idx)
print(series)
print('-------------------')
condition=[True,True,False,False,False]
print(series[condition])
print('-------------------')
print(series[series>=4][series<9])
print('-------------------')
print(series.sort_index())
print('-------------------')
print(series.sort_values())
print('-------------------')
print(series.sort_values(ascending=False))  #倒過來排
'''
'''抓csv檔
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# df=pd.read_csv(url,header=None)
# df.columns=['sepal length','sepal width','petal length','petal width','class']

col_names=['sepal length','sepal width','petal length','petal width','class']
df=pd.read_csv(url,names=col_names,header=None)
print(df)
'''
'''創造csv檔儲存
data={'city':['Nagano','Sydney','Salt Lake City','Athens',
              'Torino','Beijing','Vancouver','London',
              'Sochi','Rio de Janeiro'],
      'year':[1999,2000,2002,2004,2006,2008,2010,2012,2014,2016],
      'season':['winter','summer','winter','summer','winter','summer',
                'winter','summer','winter','summer']}
df=pd.DataFrame(data)
df.to_csv('C:/me/python/data/olympics.csv')
'''
'''
np.random.seed(0)
sample_df=pd.DataFrame(np.random.rand(8,4))
sample_df.iloc[1,0]=nan
sample_df.iloc[2,2]=nan
sample_df.iloc[6,1]=nan
sample_df.iloc[5:,3]=nan
print(sample_df)
print('--------------------------------------------------')
sample_df_dropped=sample_df.dropna()
print(sample_df_dropped)
print('--------------------------------------------------')
sample_df_dropped2=sample_df[[0,1,2]].dropna()
print(sample_df_dropped2)
print('--------------------------------------------------')#補0
sample_df_fill=sample_df.fillna(0)
print(sample_df_fill)
print('--------------------------------------------------')#補上一格值
sample_df_fill2=sample_df.fillna(method='ffill')
print(sample_df_fill2)
print('--------------------------------------------------')#補下一格值
sample_df_fill3=sample_df.fillna(method='bfill')
print(sample_df_fill3)
print('--------------------------------------------------')
sample_df_fill4=sample_df.fillna(sample_df.mean())#補平均值
print(sample_df_fill4)
'''
'''
dupli_df=pd.DataFrame({'col1':[1,1,2,3,4,4,5,5],
                      'col2':['a','b','b','b','c','c','b','b']})
print(dupli_df)
print('---------------')
print(dupli_df.duplicated())
print('---------------')
print(dupli_df.drop_duplicates())
'''
'''
people_data={'ID':[100,101,102,103,104,
                   106,108,110,111,113],
             'birth_year':[1990,1989,1992,1997,1982,
                           1991,1988,1990,1995,1981],
             'name':['Hiroshi','Akiko','yuki','Satoru','Steeve',
                     'Mituru','Aoi','Tarou','Suguru','Mitsuo'],
             'city':['東京','大阪','京都','札幌','東京',
                     '東京','大阪','京都','札幌','東京']}
people_df=pd.DataFrame(people_data)
print(people_df)
print('---------------------------------------')
city_map={'東京':'關東',
          '札幌':'北海道',
          '大阪':'關西',
          '京都':'關西'}
people_df['region']=people_df['city'].map(city_map)
print(people_df)
print('---------------------------------------')         
birth_year_cut=pd.cut(people_df['birth_year'],4) 
print(birth_year_cut)          
print('---------------------------------------')
birth_year_bins=[1980,1985,1990,1995,2000]       #自訂區間  
birth_year_cut=pd.cut(people_df['birth_year'],birth_year_bins) 
print(birth_year_cut)
print('---------------------------------------')
print(pd.value_counts(birth_year_cut))  #區間內數據筆數
print('---------------------------------------')
birth_year_bins_labels=['born in 81~85',   #自訂名稱
                        'born in 86~90',
                        'born in 91~95',
                        'born in 96~2000']
birth_year_cut=pd.cut(people_df['birth_year'],birth_year_bins,
                     labels=birth_year_bins_labels)
print(pd.value_counts(birth_year_cut))
print('---------------------------------------')
people_df['birth_year_bin']=birth_year_cut
print(people_df)
'''
'''
np.random.seed(0)
columns=['apple','banana','orange','strawberry','mango']
df=pd.DataFrame()
for column in columns:
    df[column]=np.random.choice(range(1,11),10)
df.index=[i for i in range(1,11)]
print(df)
df_head=df.head(3)
df_tail=df.tail()
print(df_head)
print(df_tail)

double_df=df*2
square_df=df**2
sqrt_df=np.sqrt(df)
print('-----------------------------------------------------------')
print(double_df)
print('-----------------------------------------------------------')
print(square_df)
print('-----------------------------------------------------------')
print(sqrt_df)
'''
'''
np.random.seed(0)
columns=['apple','orange','banana','grape','pinapple']
df = pd.DataFrame()
for column in columns:
    df[column]=np.random.choice(range(1,11),10)
df.index = [i for i in range(1,11)]
print(df)
print('-----------------------------------------------------------')
print(df.describe())   #個數、平均、標準差、最小值、25%、50%、75%、最大值
df_des=df.describe().loc[['mean','max','25%']]
print(df_des)
print('-----------------------------------------------------------')
df_diff0 = df.diff(-2,axis=0)
df_diff1 = df.diff(3,axis=1)
print(df_diff0)
print(df_diff1)
'''
'''
prefecture_df=pd.DataFrame([['Tokyo',2190,13636,'Kanto'],
                ['Kanagawa',2415,9145,'Kanto'],
                ['Osaka',1904,9837,'Kinki'],
                ['Kyoto',4610,2605,'Kinki'],
                ['Aichi',5172,7505,'Chubu']],
               columns=['Prefecture','Area',
                        'Population','Region'])
print(prefecture_df)
groups_region=prefecture_df.groupby('Region')
mean_df=groups_region.mean()
print(mean_df)
'''
'''
random.seed(0)
data={'apple':[],'orange':[],'banana':[],'grape':[],'pinapple':[]}
for name in data.keys():
    data[name]=np.random.choice(range(1,11),10)
df=pd.DataFrame(data)
print(df)
'''





