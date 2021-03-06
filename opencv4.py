import cv2 
import numpy as np

cap = cv2.VideoCapture("people-walking.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    fgmask = fgbg.apply(img)
    
    cv2.imshow("video",img)
    cv2.imshow("uygulama",fgmask)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()