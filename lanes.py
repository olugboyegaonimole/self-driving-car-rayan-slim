import cv2

import numpy as np

import matplotlib.pyplot as plt




def canny(image):
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


	#reduce noise and smoothen image to prevent detection of false edges, use a gaussian filter
	#value of every fixel = avg of every pixel around it
	#convolve the image using a 5x5 kernel
	#apply a gaussian blur
	blur = cv2.GaussianBlur(gray, (5,5), 0)


	#perform a derivative on our function in both x and y directions
	#this function thereby measures the change in intensity of our pixel intensity 
	#trace the strong gradients as a series of white pixels
	#if the gradient is higher than the high threshold it is accepted as an edge
	#if lower than the low, it is rejected
	#if btw high and low it is accepted as an edge if close to an edge
	#measures the regions of most rapid change
	canny = cv2.Canny(blur, 50, 150)

	return canny


def region_of_interest(image):
	height = image.shape[0]
	polygons = np.array([
	[(200, height), (1100, height), (550, 250)]
	])
	mask = np.zeros_like(image)
	cv2.fillPoly(mask, polygons, 255)
	return mask


image = cv2.imread('test_image.jpg')#this will retutrn the image as a multi dimentionsla nupy array

lane_image = np.copy(image)

canny = canny(lane_image)

cv2.imshow('result', region_of_interest(canny))#(window, image)

#plt.imshow(canny)

cv2.waitKey(0)#displays the image for a specified amount of milliseconds, displays the result inthe window until you press any key on your keyboard

#plt.show()