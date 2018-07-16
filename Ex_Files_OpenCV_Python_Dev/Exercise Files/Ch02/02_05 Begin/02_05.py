import numpy as np
import cv2

colour = cv2.imread("butterfly.jpg", 1)

grey =  cv2.cvtColor(colour, cv2.COLOR_RGB2GRAY)
cv2.imwrite("grey.jpg", grey)

b = colour[:,:,0]
g = colour[:,:,1]
r = colour[:,:,2]

rgba = cv2.merge((b, g, r, g))
cv2.imwrite("rgba.png", rgba)
