import numpy as np
import cv2

img=cv2.imread("opencv-logo.png", 1)
print(img)
print(type(img))
print(len(img)) # number of rows/pixels
print(len(img[0])) # number of vertical cols/pixels
print(len(img[0][0])) #number of channels (rgb, can include transparency

print(img.shape) #better way to gather this

print(img.dtype) # number of values for displaying colours (r, g, b)

print(img.size) # number of total pixels
