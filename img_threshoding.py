import cv2
import numpy as np

image=cv2.imread("images\\flower 2024-09-24.jpg",cv2.IMREAD_GRAYSCALE)
th, dst = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
cv2.namedWindow("threshold",cv2.WINDOW_KEEPRATIO)
cv2.imshow("threshold", dst)
cv2.waitKey(0)