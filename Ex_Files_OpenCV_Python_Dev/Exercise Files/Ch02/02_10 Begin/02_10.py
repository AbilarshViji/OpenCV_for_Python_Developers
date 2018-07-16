import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
colour = (255,0,0)
line_width  = -1
radius = 10
point = (0,0)

# click callback
def click(event, x, y, flags, param):
	global canvas, point, colour
	if event == cv2.EVENT_LBUTTONDOWN:
		print("LButton Down")
		colour = (255, 0, 0)
	elif event == cv2.EVENT_MOUSEMOVE:
		print("Mouse Move")
		point = (x, y)
		print(x, y)
	elif event == cv2.EVENT_LBUTTONUP:
		print("LButton Up")
		colour = (255, 255, 0)


# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.circle(canvas, point, radius, colour, line_width)

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	

cv2.destroyAllWindows()