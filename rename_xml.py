import os

def file_name(path, num, originFileName):
    '''輸入要處理檔案資料夾路徑和要處理數量，將資料夾裡.txt檔名讀出，存入fileNameList裡面回傳'''
    fileNameList = []
    fileNum = 0
    for files in os.listdir(path):
        if fileNum == num:
            break
        if os.path.splitext(files)[1] == '.xml':
            files = files.replace(originFileName,'')
            fileNameList.append(files)
            fileNum += 1
    return fileNameList, fileNum

def renameXML(oldPath, newPath, changeFileNamePart, fileNameList, originFileName):
    for fileName in fileNameList:
        file_oldname = os.path.join(oldPath, fileName+originFileName)
        fileName = fileName.replace('_育全', '')
        changeFileName = fileName+changeFileNamePart+'.xml'
        file_newname_newfile = os.path.join(newPath, changeFileName)
        os.rename(file_oldname, file_newname_newfile)


#執行前先備份檔案
oldPath = r"E:\me\python\lab\AI cup\done_xml\openDeid v2\put"
newPath = r"E:\me\python\lab\AI cup\done_xml\openDeid v2\66133~68301"
num = -1
changeFileNamePart = '_育全'
originFileName = '.xml'


fileNameList, fileNum = file_name(oldPath, num, originFileName)
renameXML(oldPath,newPath,changeFileNamePart,fileNameList, originFileName)
