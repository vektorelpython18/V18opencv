import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread("sayfa.jpg",cv2.IMREAD_COLOR)
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold = cv2.threshold(gri,12,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('ilkresim',img)
cv2.imshow("eşik1",gri)
cv2.imshow("eşik2",th)
cv2.waitKey(0)
cv2.destroyAllWindows()