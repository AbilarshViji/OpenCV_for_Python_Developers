import numpy as np
import cv2

bw  = cv2.imread("detect_blob.png",0)

h, w = bw.shape[0:2]

cv2.imshow("original", bw)

binary = np.zeros([h, w, 1], "uint8")
thresh = 85

for row in range(h):
    for col in range(w):
        if bw[row][col]>thresh:
            binary[row][col] = 255

cv2.imshow("Slow Binary", binary) # faster methods exist

ret, thresh = cv2.threshold(bw, 85, 255, cv2.THRESH_BINARY)
cv2.imshow("CV Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()