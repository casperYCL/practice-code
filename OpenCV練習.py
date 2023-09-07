import cv2
###這裡多加一行import
import numpy as np
cv2.namedWindow('111')
img=cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)
img_small=cv2.resize(img,(300,100))
cv2.imshow('111',img)
cv2.imshow('111',img_small)
cv2.waitKey(10000)
cv2.imwrite('bbb.jpg',img_small)

cv2.waitKey(10000)
cv2.destroyAllWindows()

