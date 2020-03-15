import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("cikti.avi",fourcc,25.0,(640,480))

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((15,15),np.float32)/225
    print(kernel)
    efekt1 = cv2.filter2D(img,-1,kernel)
    efekt2 = cv2.GaussianBlur(img,(15,15),2)
    efekt3 = cv2.medianBlur(img,15,2)
    # cv2.line(img,(10,10),(100,100),(60,60,60),10)
    # cv2.rectangle(img,(10,10),(100,100),(20,60,60),5)
    # cv2.circle(img,(60,120),30,(254,254,254),1)
   
    # font = cv2.FONT_HERSHEY_COMPLEX
    # cv2.putText(img,"12345678910",(10,200),font,1,(0,0,0),2,cv2.LINE_AA)
    # out.write(img)
    cv2.imshow("frame",efekt1)
    cv2.imshow("frame2",efekt2)
    cv2.imshow("frame3",efekt3)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()