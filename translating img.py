import cv2
import numpy as np

image=cv2.imread('images\Animi.jpeg')
resized=cv2.resize(image,dsize=(500,500),interpolation=cv2.INTER_AREA)
height,width=resized.shape[:2]
tx,ty=width/16,height/16
translated_matrix=np.array([[1,0,tx],[0,1,ty]])
translated_img=cv2.warpAffine(resized,translated_matrix,dsize=(width,height))

cv2.imshow('og image',image)
cv2.imshow('translated image',translated_img)
cv2.waitKey(0)
