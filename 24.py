import pandas as pd
import matplotlib.pyplot as plt
'''
technologies = {'Courses':["Spark","PySpark","Python","pandas",None],
                'Fee' :[20000,25000,22000,None,30000],
                'Duration':['30days','40days','35days','None','50days'],
                'Discount':[1000,2300,1200,2000,None]}
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=index_labels)
print(df)
df3=df['Fee'].describe()
df4=df['Discount'].describe()
'''

'''
print('-------------------------------')
print('Fee 50%':,df3.loc['50%'])
print('Discount 75%':,df4.loc['75%'])
'''
'''
print('-------------------------------')
df2100do=df[df['Discount']<2100]
df2100doFee=df2100do['Fee'].mean()
df2100doDis=df2100do['Discount'].mean()
df21000up=df[df['Fee']>21000]
df21000upFee=df21000up['Fee'].mean()
df21000upDis=df21000up['Discount'].mean()
print(df2100do)
print(df21000up)
print('Discount 2100 down,Fee:',df2100doFee)
print('Discount 2100 down,Discount:',df2100doDis)
print('Fee 21000 up,Fee:',df21000upFee)
print('Fee 21000 up,Discount:',df21000upDis)
'''
'''
dfex=pd.read_excel("C:\\me\\python\\data\\1AT score.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(dfex)
dfex80up=dfex[dfex['期中網頁project']>80]
dfex80UpSort=dfex80up.sort_values(by=['12-27 PowerPoint'],ascending=False)
dfex85up=dfex[dfex['期末報告']<85]
df85updes=dfex85up.describe()
print(dfex80UpSort)
print()
print(df85updes.loc['mean'])
'''
'''
technologies = {'Courses':["Spark","PySpark","Python","pandas",None],
                'Fee' :[20000,25000,22000,None,30000],
                'Duration':['30days','40days','35days','None','50days'],
                'Discount':[1000,2300,1200,2000,None]}
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=index_labels)
print(df)
df=df.drop('Courses',axis=1)
df=df.drop('Duration',axis=1)
print(df)
g1=df.plot(kind='pie',subplots=True,figsize=[5,5])
g2=df.plot(kind='barh',subplots=True,figsize=[5,5])
g3=df.plot(kind='barh',figsize=[5,5])
plt.show()
'''

dfex=pd.read_excel("C:\\me\\python\\data\\1AT score.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


print(dfex[(dfex['院系']=='心理系') & (dfex['12-13 Wordpress']>=80)])
print(dfex[(dfex['期中網頁project']>=90) | (dfex['12-13 Wordpress']>=90)])


print(dfex.groupby('院系')['課堂表現'].mean())
print(dfex.groupby('院系')['12-13 Wordpress'].max())
print(dfex.groupby('院系')['12-13 Wordpress'].min())