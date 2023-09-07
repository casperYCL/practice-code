import os, openpyxl

class TXTtoExcel():
    def file_name(self, path, num):
        '''輸入要處理檔案資料夾路徑和要處理數量，將資料夾裡.txt檔名讀出，存入fileNameList裡面回傳'''
        fileNameList = []
        fileNum = 0
        for files in os.listdir(path):
            if fileNum == num:
                break
            if os.path.splitext(files)[1] == '.TXT':
                fileNameList.append(files)
                fileNum += 1
        return fileNameList, fileNum

    def readTxtFile(self, path, fileName):
        wordInfoDict = {}
        filePath = path+"\\"+fileName
        with open(filePath) as file:
            for row in file:
                newList = []
                wordList = list(row.split(" "))
                for i in wordList:
                    if i != "":
                        newList.append(int(i))
                wordInfoDict[wordList[0]] = newList
        return wordInfoDict

    def writeExcel(self, wordInfoDict, path, fileName):
        fileName = fileName.replace('.TXT', ".xlsx")
        wb = openpyxl.Workbook()
        ws3 = wb["Sheet"]
        wb.remove(ws3)
        ws1 = wb.create_sheet(fileName)
        sheet = wb[fileName]
        for name, value in wordInfoDict.items():
            for i in range(9):
                sheet.cell(row=int(name)+1, column=i+1, value=value[i])
        outputFilePath = path+"\\"+fileName
        wb.save(outputFilePath)



txtToExcelObj = TXTtoExcel()
path = r"E:\me\python\data\ECG data"
fileNameList, fileNum = txtToExcelObj.file_name(path, -1)
for name in fileNameList:
    wordInfoDict = txtToExcelObj.readTxtFile(path, name)
    txtToExcelObj.writeExcel(wordInfoDict,r"E:\me\python\data\ECG data\Excel", name)
    print(name)