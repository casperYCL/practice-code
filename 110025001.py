import pandas as pd

dfex=pd.read_excel("C:\\me\\python\\data\\1AT score.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


print(dfex[(dfex['院系']=='心理系') & (dfex['12-13 Wordpress']>=80)])
print(dfex[(dfex['期中網頁project']>=90) | (dfex['12-13 Wordpress']>=90)])


print(dfex.groupby('院系')['課堂表現'].mean())
print(dfex.groupby('院系')['12-13 Wordpress'].max())
print(dfex.groupby('院系')['12-13 Wordpress'].min())