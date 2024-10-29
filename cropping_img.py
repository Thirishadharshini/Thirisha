import cv2 
import numpy as np

img=cv2.imread('images/flower 2024-09-24.jpg')
img1=img#modifies the og image
img1=img.copy()#does not modify the original image
cv2.imshow("img window",img)
cv2.imshow("img1 window",img1)
img1[100,100]=(0,255,0)
img1[105,100]=(0,255,0)

img1[101,100]=(0,255,0)

img1[102,100]=(0,255,0)

img1[103,100]=(0,255,0)

img1[104,100]=(0,255,0)

img1[105,100]=(0,255,0)

cv2.imshow("img modify window",img)
cv2.imshow("img1 modify window",img1)



print(img.shape)

corp_img=img[600:800,400:600]
cv2.imshow("cropped image",corp_img)
cv2.waitKey(0)