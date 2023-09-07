import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

def countLoss(data):
    loss = 0
    for i in data:
        for j in i:
            if  pd.isnull(j) == True or j == 'nan' or j == 'na' or j == '' or j == ' ':
                loss+=1
    return loss

def countWeekMean(data,u):
    meanList = []
    for i in data:
        word = i[u]
        if type(word) == int:
            meanList.append(int(word)*7)
        else:
            n = word.find('+')
            front = word[:n]
            back = word[n+1:]
            meanList.append(int(front)*7+int(back))
    mean = round(sum(meanList)/len(meanList))
    return mean, meanList

def countOneZero(data,part):
    numberOne = 0
    numberZero = 0
    for i in data:
        if i[part] == 0:
            numberZero += 1
        elif i[part] == 1:
            numberOne += 1
    return numberOne,numberZero

def countMean(data,u,wrong):
    meanList = []
    numList = []
    for i in range(11):
        numList.append(i)
        numList.append(str(i))
    for i in data:
        word = i[u]
        try:
            if pd.isnull(word) == False and word != 'nan' and word != 'na' and word != '' and word != ' ' and word != '?':
                strWord = str(word)
                if strWord[0] not in numList:
                    continue
                meanList.append(int(word))
        except:
                wrong += 1
    mean = round(sum(meanList)/len(meanList))
    return mean,meanList,wrong

def standard(numberList,mean):
    standardList = []
    for i in numberList:
        standardList.append((i-mean)**2)
    standard = (sum(standardList)/len(standardList))**(1/2)
    var = sum(standardList)/len(standardList)
    return standard,var

def median(numberList):
    if len(numberList)%2 == 0:
        medi = (numberList[len(numberList)//2] + numberList[((len(numberList)//2)+1)])/2
    else:
        medi = numberList[len(numberList)//2]
    return medi


def countMode(numberList):
    result = {}
    for i in numberList:
        result[i] = numberList.count(i)
    for key,value in result.items():
        if value == max(result.values()):
            maxMode = key
    return maxMode







df = pd.read_excel(r"E:\me\python\data\作業一資料(1).xlsx")
data = df.values
loss = countLoss(data)
print('loss',loss)
meanWeek = countWeekMean(data,3)
bgNumberZero,bgNumberOne = countOneZero(data,1)
feverNumberZero,feverNumberOne = countOneZero(data,7)
inflamedNumberZero,inflamedNumberOne = countOneZero(data,8)
aliveNumberZero,aliveNumberOne = countOneZero(data,9)
useCatheterNumberZero,useCatheterNumberOne = countOneZero(data,10)
septicemiaNumberZero,septicemiaNumberOne = countOneZero(data,25)
wrong = 0
numberDict = {}
dfDict = {}
for u in range(1,25):
    usedList = [1,2,7,8,9,10,25]
    dfDict[u] = []
    for j in data:
        dfDict[u].append(j[u])
    if u in usedList:
        continue
    numberDict[u] = []
    if u == 3:
        mean, numberList= countWeekMean(data,u)
    else:
        mean, numberList,wrong= countMean(data,u,wrong)
    stand,var = standard(numberList,mean)
    medi = median(numberList)
    mode = countMode(numberList)
    numberDict[u].append(round(mean))
    numberDict[u].append(round(stand))
    numberDict[u].append(round(medi))
    numberDict[u].append(mode)
    numberDict[u].append(np.percentile(numberList,(25)))
    numberDict[u].append(np.percentile(numberList,(75)))
    numberDict[u].append(max(numberList)-min(numberList))
    numberDict[u].append(round(var))
    if mean == 0 and stand == 1:
        numberDict[u].append('常態分布')
    else:
        numberDict[u].append('非常態分布')
    fig = sm.qqplot(np.array(numberList), line='45')
    plt.show()
df = pd.DataFrame(dfDict)
nn = df.corr()
print('1.缺額',loss)
print('2.異常值',wrong)
print('3.懷孕周數',meanWeek)
print('4.依序6個欄位01數量')
print('4.性別',bgNumberZero,bgNumberOne)
print('4.生產發燒',feverNumberZero,feverNumberOne)
print('4.絨毛炎',inflamedNumberZero,inflamedNumberOne)
print('4.存亡',aliveNumberZero,aliveNumberOne)
print('4.使用導管',useCatheterNumberZero,useCatheterNumberOne)
print('4.敗血症',septicemiaNumberZero,septicemiaNumberOne)
print('5.key為第幾個欄位，19個欄位資訊依序為平均數，標準差，中位數，眾數，25四分衛數，75四分衛數，全距，變異數')
print(numberDict)
print('qq plot')
print('相關係數表格',df.corr())

