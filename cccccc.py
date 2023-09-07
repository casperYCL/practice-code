#-*- coding: UTF-8 -*- 

import cv2
import numpy as np
import os

def get_image(path):
    #獲取圖片
    img=cv2.imread(path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    return img, gray

def Gaussian_Blur(gray):
    # 高斯去噪
    blurred = cv2.GaussianBlur(gray, (9, 9),0)

    return blurred

def Sobel_gradient(blurred):
    # 索比爾算子來計算x、y方向梯度
    gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0)
    gradY = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=0, dy=1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    return gradX, gradY, gradient

def Thresh_and_blur(gradient):

    blurred = cv2.GaussianBlur(gradient, (9, 9),0)
    (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

    return thresh

def image_morphology(thresh):
    # 建立一個橢圓核函數
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    # 執行圖像形態學, 細節直接查文檔，很簡單
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=0)
    closed = cv2.dilate(closed, None, iterations=2)

    return closed

def findcnts_and_box_point(closed):
    # 這裏opencv3返回的是三個參數
    (_, cnts, _) = cv2.findContours(closed.copy()
        #cv2.RETR_EXTERNAL,             #表示只檢測外輪廓
    #cv2.RETR_CCOMP,                #建立兩個等級的輪廓,上一層是邊界
    cv2.RETR_LIST                 #檢測的輪廓不建立等級關係
    #cv2.RETR_TREE,                   #建立一個等級樹結構的輪廓
    cv2.CHAIN_APPROX_NONE           #存儲所有的輪廓點，相鄰的兩個點的像素位置差不超過1
    #cv2.CHAIN_APPROX_SIMPLE,       #例如一個矩形輪廓只需4個點來保存輪廓信息
    #cv2.CHAIN_APPROX_TC89_L1,
    #cv2.CHAIN_APPROX_TC89_KCOS
        )
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    return box

def drawcnts_and_cut(original_img, box):
    # 因爲這個函數有極強的破壞性，所有需要在img.copy()上畫
    # draw a bounding box arounded the detected barcode and display the image
    draw_img = cv2.drawContours(original_img.copy(), [box], -1, (0, 0, 255), 3)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1
    crop_img = original_img[y1:y1+hight, x1:x1+width]

    return draw_img, crop_img
'''
def walk():############批處理
    filename_rgb = r'D:\py_project\My_Project\dataset\trainingData'
    for filename in os.listdir(filename_rgb):              #listdir的參數是文件夾的路徑
        #img_path = r'D:\py_project\My_Project\296.png'
        #save_path = r'D:\py_project\My_Project\296_save.jpg'
        img_path = filename_rgb + ('/%s' % filename)
        save_path = r'D:\py_project\My_Project\dataset\trainingData_process'
        original_img, gray = get_image(img_path)
        blurred = Gaussian_Blur(gray)
        gradX, gradY, gradient = Sobel_gradient(blurred)
        thresh = Thresh_and_blur(gradient)
        closed = image_morphology(thresh)
        box = findcnts_and_box_point(closed)
        draw_img, crop_img = drawcnts_and_cut(original_img,box)



#    cv2.imshow('original_img', original_img)
#    cv2.imshow('blurred', blurred)
#    cv2.imshow('gradX', gradX)
#    cv2.imshow('gradY', gradY)
#    cv2.imshow('final', gradient)
#    cv2.imshow('thresh', thresh)
#    cv2.imshow('closed', closed)
#    cv2.imshow('draw_img', draw_img)
#    cv2.imshow('crop_img', crop_img)
#    cv2.waitKey(20171219)
        file_process_name = save_path + ('\%s' % filename)
        print(file_process_name)
        cv2.imwrite(file_process_name, crop_img)
'''
def walk2():######################單張圖片處理
    img_path = r"C:\me\python\image.jpg"
    save_path = r"C:\me\python\image.jpg"
    original_img, gray = get_image(img_path)
    blurred = Gaussian_Blur(gray)
    gradX, gradY, gradient = Sobel_gradient(blurred)
    thresh = Thresh_and_blur(gradient)
    closed = image_morphology(thresh)
    box = findcnts_and_box_point(closed)
    draw_img, crop_img = drawcnts_and_cut(original_img,box)



#    cv2.imshow('original_img', original_img)
#    cv2.imshow('blurred', blurred)
#    cv2.imshow('gradX', gradX)
#    cv2.imshow('gradY', gradY)
#    cv2.imshow('final', gradient)
#    cv2.imshow('thresh', thresh)
#    cv2.imshow('closed', closed)
#    cv2.imshow('draw_img', draw_img)
#    cv2.imshow('crop_img', crop_img)
#    cv2.waitKey(20171219)
    cv2.imwrite(save_path, crop_img)
walk2()