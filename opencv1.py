# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:10:57 2022

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

def aidemy_imshow(name,img):
    b, g, r, =cv2.split(img)
    img=cv2.merge([r, g, b])
    plt.title(name)
    plt.imshow(img)
    plt.show()
cv2.imshow = aidemy_imshow

'''
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
print(type(img))
print(img.shape)
cv2.imshow('Sample pic',img)
'''
''' 
#另存照片，照片為(255,255,0)
img=np.array([[(255,255,0) for i in range(256)]for i in range(256)])
cv2.imwrite(r"C:\me\python\photo\sample_2.jpg",img)
cv2.imshow('sample pic2',img)
'''
'''
#漸層圖片
img_size=256
img=np.array([[(x,int((x+y)/2),y) for x in range(img_size)]
              for y in range(img_size)])
cv2.imwrite(r"C:\me\python\photo\sample_3.jpg",img)
cv2.imshow('sample pic3',img)
'''
'''
#裁切圖片
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
print(img.shape)
img_cut=img[0:(img.shape[0]*2//3),0:(img.shape[1]*2//3)]
cv2.imshow('Sample pic',img_cut)
'''
'''
#圖片縮放，翻轉，旋轉
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
img_resize=cv2.resize(img,(img.shape[1]*2,img.shape[0]*3))
cv2.imshow('sample pic',img_resize)
img_flip=cv2.flip(img,-1)
cv2.imshow('sample pic',img_flip)
#aff_matrix設定變換矩陣，中心點，30度，0.8倍，再帶入旋轉，新圖寬高不變
aff_matrix=cv2.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2),
                                   30,0.8)
img_rotate=cv2.warpAffine(img,aff_matrix,(img.shape[1],img.shape[0]))
cv2.imshow('sample pic',img_rotate)
img_rotate1=cv2.rotate(img,0) #0=cv2.ROTATE_90_CLOCKWISE轉90度
cv2.imshow('sample pic',img_rotate1)
'''
'''
#轉換色彩空間
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
img_convert=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
cv2.imshow('sample pic',img_convert)
#負片效果
img_invert=cv2.bitwise_not(img)
cv2.imshow('sample pic',img_invert)
'''
'''
#圖片二值化處裡
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
thr,img_binary=cv2.threshold(img,192,255,cv2.THRESH_TOZERO)
cv2.imshow('sample pic',img_binary)
'''
'''
#套用遮罩
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
mask=cv2.imread(r"C:\me\python\photo\mask.jpg",cv2.IMREAD_GRAYSCALE)
mask=cv2.resize(mask,(img.shape[1],img.shape[0]))
img_masked=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('sample pic',img_masked)
mask=cv2.bitwise_not(mask)#反轉遮罩
img_masked=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('sample pic',img_masked)
'''

#模糊效果
img=cv2.imread(r"C:\me\python\photo\sample.jpg")
img_blur=cv2.GaussianBlur(img,(49,49),0)
cv2.imshow('sample pic',img_blur)
#消除雜訊
img2=cv2.imread(r"C:\me\python\photo\sample2.jpg")
img2_denoised=cv2.fastNlMeansDenoisingColored(img2,h=10)
cv2.imshow('sample pic2',img2)
cv2.imshow('sample pic2',img2_denoised)







































    