# import required libraries
# import cv2
# import numpy as np

# # read the input image
# img = cv2.imread('C:\\office works\\ln.png')
# cv2.resize(img,dsize=(1024,1024))
# # access the image height and width
# print(img.shape)
# rows,cols,_ = img.shape

# # define at three point on input image
# pts1 = np.float32([[18,275],[339,276],[677,275]])

# # define three points corresponding location to output image
# pts2 = np.float32([[85,451],[339,276],[528,451 ]])

# # get the affine transformation Matrix
# M = cv2.getAffineTransform(pts1,pts2)

# # apply affine transformation on the input image
# dst = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow("Affine Transform", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # img=cv2.imread("C:\\office works\\image _19.png",cv2.IMREAD_GRAYSCALE)
# # blur=cv2.GaussianBlur(img,(3,3),0)
# # th,dst=cv2.threshold(blur,200,255,cv2.THRESH_BINARY)
# # cv2.namedWindow("output",cv2.WINDOW_KEEPRATIO)
# # cv2.imshow("output",dst)

# # contours,heirarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# # print(len(contours))
# # for i in range(len(contours)):
# #   print("for")
# #   if  cv2.contourArea(contours[i])>0:
# #      print("if")
# #      cv2.drawContours(img,contours,i,(255,0,0),2)

# # cv2.namedWindow("contour",cv2.WINDOW_KEEPRATIO)
# # cv2.imshow("contour",img)
# # cv2.waitKey(0)
# import cv2
# import numpy as np

# # Load image in grayscale
# img = cv2.imread("C:\\office works\\image _19.png")

# # Check if the image is loaded properly
# if img is None:
#     print("Error: Could not load the image. Check the file path.")
# else:
#     # Apply Gaussian blur
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (3,3), 0)

#     # Apply thresholding
#     _, dst = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

#     # Find contours
#     contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
#     print(f"Total contours found: {len(contours)}")

#     # Draw contours if area is greater than 100
#     for i in range(len(contours)):
#         if cv2.contourArea(contours[i]) > 100:
#             cv2.drawContours(img, contours, i, (255, 0, 0), 2)

#     # Show the thresholded image
#     cv2.imshow("Threshold", dst)

#     # Show the image with contours
#     cv2.imshow("Contours", img)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# import cv2
# import numpy as np

# # Load the image
# image_path = "C:\\office works\\image _19.png"
# img = cv2.imread(image_path)

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply edge detection
# edges = cv2.Canny(gray, 50, 150)

# # Find contours
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Find the largest contour (assuming it's the text region)
# contour = max(contours, key=cv2.contourArea)

# # Get the bounding box
# rect = cv2.minAreaRect(contour)
# box = cv2.boxPoints(rect)
# box = box.astype(int)

# # Order points for transformation
# def order_points(pts):
#     rect = np.zeros((4, 2), dtype="float32")
#     s = pts.sum(axis=1)
#     rect[0] = pts[np.argmin(s)]  # Top-left
#     rect[2] = pts[np.argmax(s)]  # Bottom-right

#     diff = np.diff(pts, axis=1)
#     rect[1] = pts[np.argmin(diff)]  # Top-right
#     rect[3] = pts[np.argmax(diff)]  # Bottom-left
#     return rect

# ordered_box = order_points(box)

# # Define new width and height
# width = int(rect[1][0])
# height = int(rect[1][1])

# # Define destination points for transformation
# dst_pts = np.array([[0, 0], [width-1, 0], [width-1, height-1], [0, height-1]], dtype="float32")

# # Compute perspective transform
# M = cv2.getPerspectiveTransform(ordered_box, dst_pts)
# warped = cv2.warpPerspective(img, M, (width, height))

# # Show results
# cv2.imshow("Warped Text", warped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('C:\\office works\\line.png')

# # Get the dimensions of the image
# height, width = image.shape[:2]

# # Define the source points (corners of the original image)
# src_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# # Define the destination points (where you want the corners to be mapped)
# # Adjust these points to create a curvature effect
# dst_points = np.float32([[0, 0], [width, 50], [50, height], [width-50, height-50]])

# # Get the perspective transformation matrix
# matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# # Apply the warp transformation
# curved_image = cv2.warpPerspective(image, matrix, (width, height))

# # Display the original and transformed images
# cv2.imshow('Original Image', image)
# cv2.imshow('Curved Image', curved_image)

# # Wait for a key press and close the windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np

# # Create a blank image
# img = np.zeros((500, 500, 3), dtype=np.uint8)

# # Define start and end points of the straight line
# start_point = (100, 250)
# end_point = (400, 250)

# # Generate points along the straight line
# num_points = 50
# x_vals = np.linspace(start_point[0], end_point[0], num_points)
# y_vals = np.linspace(start_point[1], end_point[1], num_points)

# # Modify y-values to create a curve (e.g., sine wave)
# y_vals = y_vals + 50 * np.sin(np.linspace(0, np.pi, num_points))

# # Convert points to integer tuples
# curve_points = np.array([np.int32([x, y]) for x, y in zip(x_vals, y_vals)])
# cv2.imshow(" Line", img)
# # Draw the curved line
# cv2.polylines(img, [curve_points], isClosed=False, color=(0, 255, 0), thickness=2)

# # Show image
# cv2.imshow("Curved Line", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Create blank images for both straight and curved lines
img_straight = np.zeros((500, 500, 3), dtype=np.uint8)
img_curved = np.zeros((500, 500, 3), dtype=np.uint8)

# Define start and end points of the straight line
start_point = (100, 250)
end_point = (400, 250)

# Draw the straight line
cv2.line(img_straight, start_point, end_point, (0, 255, 0), thickness=2)

# Generate points along the straight line
num_points = 50  # More points = smoother curve
x_vals = np.linspace(start_point[0], end_point[0], num_points)
y_vals = np.linspace(start_point[1], end_point[1], num_points)

# Modify y-values to create a curve (e.g., sine wave)
y_vals = y_vals + -50* np.sin(np.linspace(0, np.pi, num_points))  # Adjust amplitude as needed

# Convert points to integer tuples
curve_points = np.array([np.int32([x, y]) for x, y in zip(x_vals, y_vals)])

# Draw the curved line
cv2.polylines(img_curved, [curve_points], isClosed=False, color=(0, 255, 0), thickness=2)
cv2.imshow("straight",img_straight)
# Stack images side by side for comparison
combined_image = np.hstack((img_straight, img_curved))

# Show images
cv2.imshow("Straight Line (Left) vs Curved Line (Right)", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
