import cv2
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