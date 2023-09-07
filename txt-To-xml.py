import os
import xml.etree.ElementTree as ET

def file_name(path, num):
    '''輸入要處理檔案資料夾路徑和要處理數量，將資料夾裡.txt檔名讀出，存入fileNameList裡面回傳'''
    fileNameList = []
    fileNum = 0
    for files in os.listdir(path):
        if fileNum == num:
            break
        if os.path.splitext(files)[1] == '.txt':
            fileNameList.append(files)
            fileNum += 1
    return fileNameList, fileNum

def txtToXml(path, changePath, fileNameList,oldPath):
    for fileName in fileNameList:
        usePath = path+"\\"+fileName
        newFileName = fileName.replace(".txt","_育全.xml")
        useChangePath = changePath +"\\"+newFileName
        txt = ""
        with open(usePath,encoding='utf-8') as file:
            for row in file:
                txt = txt+"\n"+row
            tree = ET.parse(oldPath)
            root = tree.getroot()
            sub1 = root.find("TEXT")
            cdata = CDATA(txt)
            #sub1.text = f"<![CDATA[{txt}]]"
            sub1.append(cdata)
            et = ET.ElementTree(sub1)
            et.write(useChangePath, encoding='utf-8', xml_declaration=True)
            #tree.write(useChangePath, encoding='utf-8', xml_declaration=True)

def CDATA(text=None):
    element = ET.Element('![CDATA[')
    element.text = text
    return element

if __name__ == '__main__':
    path = r"E:\me\python\lab\AI cup\undone_txt\EHR-val50"
    changePath = r"E:\me\python\lab\AI cup\done_xml\新增資料夾"
    oldPath = r"E:\me\python\lab\AI cup\done_xml\9.xml"
    fileNameList, fileNum = file_name(path,50)
    txtToXml(path,changePath,fileNameList,oldPath)
    import xml.dom.minidom

    dom = xml.dom.minidom.parse(oldPath)
    root = dom.documentElement
    bb = root.getElementsByTagName('TEXT')
    for b in bb:
        print(b.nodeName)
        print(b.firstChild.data)
    print()
    print()



