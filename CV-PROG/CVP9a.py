import cv2 
path = "C:\\Users\\chethna\\Desktop\\Anime pic\\images.jpg" 
src = cv2.imread(path) 
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE) 
cv2.imshow('Image', image) 
cv2.waitKey(0)
