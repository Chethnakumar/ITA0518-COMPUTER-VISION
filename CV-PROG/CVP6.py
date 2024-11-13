import cv2 
import numpy as np 
cap = cv2.VideoCapture("C:\\Users\\chethna\\Desktop\\Mayumi\\ANI - For edit\\VID-20221017-WA0158.mp4") 
if (cap.isOpened()== False): 
 print("Error opening video file") 
while(cap.isOpened()): 
 ret, frame = cap.read() 
 if ret == True: 
  cv2.imshow('Frame', frame) 
  if cv2.waitKey(10) & 0xFF == ord('q'): 
   break 
 else: 
  break 
cap.release() 
cv2.destroyAllWindows() 
