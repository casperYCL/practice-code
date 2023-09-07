import xml.etree.ElementTree as etree
import xml.dom.minidom
#~ import cElementTree as etree

def CDATA(text=None):
    element = etree.Element(CDATA)
    element.text = str(text)
    return element

class ElementTreeCDATA(etree.ElementTree):
    def _write(self, file, node, encoding, namespaces):
        if node.tag is CDATA:
            text = node.text.encode(encoding)
            file.write("\n<![CDATA[%s]]>\n" % text)
        else:
            etree.ElementTree._write(self, file, node, encoding, namespaces)






if __name__ == "__main__":
    import sys



    tree = etree.parse(r"E:\me\python\lab\AI cup\done_xml\9.xml")
    root = tree.getroot()



    '''dom = xml.dom.minidom.parse("E:\me\python\lab\AI cup\done_xml\9.xml")
    root = dom.documentElement
    bb = root.getElementsByTagName('TEXT')
    for b in bb:
        print(b.nodeName)
        print(b.firstChild.data)
    print()
    print()'''
    # 從字串中取得並解析 XML 資料
    #root = etree.fromstring('320.txt')
    '''
    print(root.tag)
    print(root.attrib)
    for child in root:
        print(child.tag, child.attrib)
        print(child.text)
    print(root[0].text)
    print('--'*50)
    print(root[0][1].text)'''

    import os

    file_oldname = os.path.join(r"E:\me\python\lab\AI cup\done_xml", "9.xml")
    file_newname_newfile = os.path.join(r"E:\me\python\lab\AI cup\done_xml", "9_育全.xml")

    os.rename(file_oldname, file_newname_newfile)