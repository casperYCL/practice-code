
from PIL import Image
import os,sys

mw = 100
ms = 20

msize = mw*ms

#选一张画布，关键确定画布的大小
toImage = Image.new('RGBA',(2000,2000))

for y in range(1,21):
    for x in range(1,21):
        try:

#选取照片，按照自己想要的样式，依次选取

            fromImage = Image.open(r"C:\Users\user\OneDrive\桌面\大學\素材\法定準備制度.jpg" %str(ms*(y-1)+x))

#粘贴照片，将照片粘贴到设计的位置上

            fromImage = fromImage.resize((100,100),Image.ANTIALIAS)
            toImage.paste(fromImage,((x-1)*mw,(y-1)*mw))
        except IOError:
            pass

toImage.show()
toImage.save('C:\Users\user\OneDrive\桌面"/LX.png')