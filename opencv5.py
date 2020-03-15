import cv2
import numpy as np
# from matplotlib import pyplot as plt
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


img = cv2.imread("face4.jpg",cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
yuzler = face_cascade.detectMultiScale(gray,1.2,5)
for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_color = img[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for ex,ey,ew,eh in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),-1)
cv2.imshow("tespit",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


