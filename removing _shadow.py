import cv2
import numpy as np 

image=cv2.imread("images\img.jpg")
hsv=cv2.cvtColor(image,code=cv2.COLOR_BGR2HSV)
print(image.shape)
height,width,channels=image.shape
# for i in range(height):
#     for j in range(width):
#         h = hsv[i,j, 0]
#         s = hsv[i,j, 1]
#         v = hsv[i,j, 2]
#         if s<45 and v>50:
#             hsv[i,j,1]=0
#             hsv[i,j,2]=255


mask = (hsv[:, :, 1] < 45) & (hsv[:, :, 2] > 50)
hsv[mask, 1] = 0
hsv[mask, 2] = 255

result_img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.namedWindow("result image",cv2.WINDOW_FULLSCREEN)
cv2.imshow("result image",result_img)
cv2.imwrite("images\\result_img_mask.jpg",result_img)
cv2.waitKey(0)
print("completed")