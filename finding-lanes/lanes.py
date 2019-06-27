import cv2
import numpy as np


image = cv2.imread('test_image.jpg')
#this will retutrn the image as a multi dimentionsla nupy array

lane_image = np.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

cv2.imshow('result', gray)#(window, image)
cv2.waitKey(0)