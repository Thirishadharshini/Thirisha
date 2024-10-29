import cv2 
import numpy as np

image=cv2.imread('images\\flower 2024-09-24.jpg')

height,width=image.shape[:2]
print(height,width)
center=(width/2,height/2)
rotation_matrix=cv2.getRotationMatrix2D(center,angle=180,scale=0.5)
rotated_img=cv2.warpAffine(image,rotation_matrix,dsize=(width,height))

cv2.imshow("og img",image)
cv2.imshow('rotated img',rotated_img)
cv2.waitKey(0)