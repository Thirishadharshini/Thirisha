# import cv2
# import numpy as np


# image = cv2.imread("C:\\office works\\ln.png") 
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)
# print(image.shape)

# edges = cv2.Canny(gray, 50, 150)
# cv2.imshow("edge",edges)
# # cv2.waitKey(0)
# # Detect lines using Hough Transform
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=100)
# print(lines)
# print(len(lines))
# # print(lines[0][0][0])
# # print(lines[0][0][1])
# # print(lines[1][0][0])
# # print(lines[1])
# for i in lines:
#     # print(i[0][0])
#     # print(len(i))
#     x11,y11,x12,y12=i[0]
#     print(x11,y11,x12,y12)
#     len=x12-x11
#     center=x11+int(len/2)
#     print(center)
#     row=y11
   
#     for j in range(6, center):
#         src_px_back=(center-j,y11)
#         dst_px_back=(center-j,row+1)
#         # image[src_px_back[1], src_px_back[0]]=(255,255,255)
#         # print(src_px_back,dst_px_back)
#         image[dst_px_back[1], dst_px_back[0]] = (0,0,0)#image[src_px_back[1], src_px_back[0]]
#         src_px_front=(center+j,y11)
#         dst_px_front=(center+j,row+1)
       
#         # print(src_px_front,dst_px_front)
#         image[dst_px_front[1],dst_px_front[0]]=(0,0,0)# image[src_px_front[1], src_px_front[0]]
#         # print(row)
#         row+=1
          
        
# cv2.namedWindow("op",cv2.WINDOW_KEEPRATIO)
# cv2.imshow("op",image)
# cv2.waitKey(0)

   
# import necessary libraries 

import cv2 
import numpy as np 

# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)

while True:
	
	ret, frame = cap.read()

	# Locate points of the documents
	# or object which you want to transform
	pts1 = np.float32([[0, 260], [640, 260],
					[0, 400], [640, 400]])
	pts2 = np.float32([[0, 0], [400, 0],
					[0, 640], [400, 640]])
	
	# Apply Perspective Transform Algorithm
	matrix = cv2.getPerspectiveTransform(pts1, pts2)
	result = cv2.warpPerspective(frame, matrix, (500, 600))
	
	# Wrap the transformed image
	cv2.imshow('frame', frame) # Initial Capture
	cv2.imshow('frame1', result) # Transformed Capture

	if cv2.waitKey(24) == 27:
		break

cap.release()
cv2.destroyAllWindows()
