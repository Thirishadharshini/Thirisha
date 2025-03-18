import cv2
import numpy as np

# Load the image
image_path = "C:\\office works\\image _19.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Get image dimensions
h, w = image.shape[:2]

# Define center and radius for transformation
center = (w // 2, h // 2)  # Approximate center of the ring
max_radius = min(w, h) // 2  # Maximum radius for unwrapping

# Apply Polar to Cartesian transformation (unwrap the curved text)
unwrapped = cv2.warpPolar(image, (w, h), center, max_radius, cv2.WARP_POLAR_LINEAR)

# Show the straightened text image
cv2.imshow("Straightened Text", unwrapped)
cv2.waitKey(0)
cv2.destroyAllWindows()
