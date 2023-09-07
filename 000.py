import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
'''
df=pd.read_csv('C:\me\python\data\Stores.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#print(df)

dfSales=df.sort_values(by='Store_Sales',ascending=False)
dfArea=df.sort_values(by='Store_Area',ascending=False)
sortDict={}

print(dfArea.head())
print(dfArea.values[1])
print(dfArea.loc[1,'Store_Area'])
print(dfArea.index[dfArea['Store_Area']==dfArea.loc[1,'Store_Area']].tolist(),
                dfArea.index[dfArea['Store_Sales']==dfArea.loc[1,'Store_Sales']].tolist())
for i in range(895):
    sortDict[i]=[dfArea.index[dfArea['Store_Area']==dfArea.loc[i,'Store_Area']].tolist(),
                dfArea.index[dfArea['Store_Sales']==dfArea.loc[i,'Store_Sales']].tolist()]
print(sortDict)
#print(dfArea["Store_ID"].tolist())
plt.xlabel('Store_Area')
plt.ylabel('Store_Sales')
plt.scatter(dfArea["Store_Area"].tolist(),dfArea["Store_Sales"].tolist(),s=20)
plt.show()


print('keys:',df.keys())
print(df.info())
print(df.isnull().sum())



train_x, test_x, train_y, test_y=train_test_split(
           X_train, Y_train ,random_state=41, test_size = 0.1185,shuffle=True)

# 可以看一下這些資料集的維度，驗證沒有切錯
print("原始資料集的維度大小:" , my_data.data.shape)
print("訓練集的維度大小:   " , train_x.shape)
print("測試集的維度大小:   " , test_x.shape)
'''
'''import numpy as np
X = np.array([[1., 0.], [2., 1.], [0., 0.]])
y = np.array([0, 1, 2])

from scipy.sparse import coo_matrix
X_sparse = coo_matrix(X)

from sklearn.utils import resample
X, X_sparse, y = resample(X, X_sparse, y, random_state=123)
print(X)
print(X_sparse)
print(y)
Y= [0, 0, 1, 1, 1, 1, 1, 1, 1]
print(resample(Y, n_samples=9, replace=True, stratify=Y,random_state=123))
print(resample(Y, n_samples=9, replace=False,random_state=123))

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
print(fruits_series.index[0])'''

class aaa():
    def ac(self):
        print('ac')


class bbb(aaa):
    def accc(self):
        self.ac()
        print('accc')


nnn = {'aa':'aa','bb':'bb'}
for i in nnn.values():
    print(i)



bbb = bbb()
bbb.accc()
import cProfile
import pstats
cProfile.run('bbb.accc()', filename="result.out")  # profile pow2(a)，並且將結果寫入 result.out
p = pstats.Stats("result.out")
print(p.strip_dirs().sort_stats("tottime").print_stats())



