import cv2
import numpy as np

image=cv2.imread("images/opencvimage.jpg")
#using size value
resize_img=cv2.resize(image,(100,100),interpolation=cv2.INTER_LINEAR)
#using scale factor
resize_scale=cv2.resize(image,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_AREA)
cv2.imshow("original img",image)
cv2.imshow("resized img",resize_img)
cv2.imshow("resized img using scale",resize_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()