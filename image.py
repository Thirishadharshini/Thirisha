import cv2

# Read an image
image = cv2.imread('C:\\Users\\User\\OneDrive\\Pictures\\Screenshots\\opencvimage.jpg')
# Display the image
cv2.imshow('Image', image)
print(image.shape)
#write the image
cv2.imwrite('C:\\Users\\User\\OneDrive\\Pictures\\Screenshots\\python_opencv.jpg',image)
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()