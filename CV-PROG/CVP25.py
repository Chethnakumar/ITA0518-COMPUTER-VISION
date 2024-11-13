import cv2
import numpy as np
a = cv2.imread("C:\\Users\\chethna\\Desktop\\Anime pic\\images.jpg")

# Define the Laplacian kernel
Lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Apply convolution using OpenCV filter2D
a1 = cv2.filter2D(a, -1, Lap)

# Convert the result to uint8 (if necessary)
a1_uint8 = np.uint8(a1)

# Display the absolute difference using cv2.imshow (equivalent to imtool)
cv2.imshow("Difference between Original and Filtered (Lap1)", np.abs(a - a1_uint8))

# Define a second Laplacian kernel for edge detection
lap = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# Apply convolution again
a3 = cv2.filter2D(a, -1, lap)

# Convert the result to uint8
a3_uint8 = np.uint8(a3)

# Display the absolute difference using cv2.imshow (equivalent to imtool)
cv2.imshow("Difference between Original and Filtered (Lap2)", np.abs(a + a3_uint8))

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
