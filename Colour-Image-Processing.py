import numpy as np
import cv2

img = cv2.imread("zyuranger2.png")
blr = cv2.GaussianBlur(img, (7,7), 0) #to clear out rough edges
hsv = cv2.cvtColor(blr, cv2.COLOR_BGR2HSV)

inp = input("Colour: ")
if inp == "red":
    lower_r = np.array([0, 82, 82])
    upper_r = np.array([10, 255, 255])
elif inp == "blue":
    lower_r = np.array([100, 30, 30])
    upper_r = np.array([130, 255, 255])
elif inp == "green":
    lower_r = np.array([50, 50, 50])
    upper_r = np.array([85, 255, 255])
elif inp == 'yellow':
    lower_r = np.array([20, 100, 100])
    upper_r = np.array([40, 255, 255])
elif inp == "pink":
    lower_r = np.array([133, 43, 43])
    upper_r = np.array([175, 255, 255])

mask = cv2.inRange(hsv, lower_r, upper_r)
sgmnt = cv2.bitwise_and(img, img, mask=mask)           # segmenting the desired object

cv2.imshow("ori", img)
cv2.imshow("blr", blr)
cv2.imshow("hsv", hsv)
cv2.imshow("masking", mask)
cv2.imshow("segmented", sgmnt)
cv2.waitKey(0)