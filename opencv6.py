import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("cikti.avi",fourcc,25.0,(640,480))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    yuzler = face_cascade.detectMultiScale(gray,1.2,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h,x:x+w]
        roi_gray = gray[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)  

    cv2.imshow("Sonuc",img)  
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()