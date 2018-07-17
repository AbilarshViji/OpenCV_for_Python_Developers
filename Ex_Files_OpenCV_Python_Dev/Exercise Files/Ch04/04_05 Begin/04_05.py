import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_frontalface_default.xml"
face_casade = cv2.CascadeClassifier(path)

faces = face_casade.detectMultiScale(grey, scaleFactor=1.08, minNeighbors=5, minSize=(42,42)) #list of all bounding boxes
print(len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()