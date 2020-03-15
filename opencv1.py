import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread("resim.jpg",cv2.IMREAD_COLOR)
kernel = np.ones((15,15),np.float32)/225
efekt1 = cv2.filter2D(img,-1,kernel)
efekt2 = cv2.GaussianBlur(img,(15,15),2)
efekt3 = cv2.medianBlur(img,15,2)
cv2.imshow("frame",efekt1)
cv2.imshow("frame2",efekt2)
cv2.imshow("frame3",efekt3)
cv2.imshow('ilkresim',img)
cv2.waitKey(0)
cv2.destroyAllWindows()