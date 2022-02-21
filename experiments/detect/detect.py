import cv2
import numpy as np


image = cv2.imread("page0.jpg")                
# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define  color range
#light_blue = np.array([110,50,50])
#dark_blue = np.array([130,255,255])

#light_white = (0, 0, 200)
#dark_white = (145, 60, 255)

#lower_gray = np.array([0, 0, 0])
#upper_gray = np.array([255, 10, 255])

light_yelloy = np.array([22, 93, 0])
dark_yellow = np.array([45, 255, 255])

# Threshold the HSV image to get chosen colors
mask = cv2.inRange(hsv, light_yelloy, dark_yellow)


# Bitwise-AND mask and original image
output = cv2.bitwise_and(image,image, mask= mask)
    
cv2.imshow("Color Detected", np.hstack((image,output)))
cv2.waitKey(0)
cv2.destroyAllWindows()