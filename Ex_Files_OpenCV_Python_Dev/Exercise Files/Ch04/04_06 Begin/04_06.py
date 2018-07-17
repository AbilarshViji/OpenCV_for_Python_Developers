import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_eye.xml"
eye_casade = cv2.CascadeClassifier(path)

eyes = eye_casade.detectMultiScale(grey, scaleFactor=1.01, minNeighbors=30, minSize=(8,8), maxSize=(40,40))
print(eyes)

for (x,y,w,h) in eyes:
    xc = (x + x + w) / 2
    yc = (y + y + h) / 2
    radius = w / 2
    cv2.circle(img, (int(xc), int(yc)), int(radius), (255, 0, 0), 2)

cv2.imshow("Eyes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

