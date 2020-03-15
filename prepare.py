import cv2
import os
import numpy as np


elemanlar = ["","Şeyma","Cem"]

def yuztespit(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("lbpcascade_frontalface.xml")
    faces = face_cascade.detectMultiScale(gray,1.2,5)
    if (len(faces)==0):
        return None,None
    x,y,w,h = faces[0]
    return gray[y:y+w,x:x+h],faces[0]

def tanimayaHazirlan(klasor_yol):
    klasorler = os.listdir(klasor_yol)
    yuzler = []
    etiketler = []
    for klasor in klasorler:
        if not klasor.startswith("s"):
            continue
        etiket = int(klasor.replace("s",""))
        ozne_klasor_yol = klasor_yol + "/" + klasor
        ozne_img_isimler = os.listdir(ozne_klasor_yol)
        for img_isim in ozne_img_isimler:
            if img_isim.startswith("."):
                continue
            img_yol = ozne_klasor_yol + "/" + img_isim
            img = cv2.imread(img_yol)
            cv2.imshow("Egitilen",img)
            cv2.waitKey(100)
            yuz,rect = yuztespit(img)
            if yuz is not None:
                yuzler.append(yuz)
                etiketler.append(etiket)
            cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
    print(etiketler)
    return yuzler,etiketler


print("Haziriz")
yuzler,etiketler = tanimayaHazirlan(r"D:\edizibrahim\fotolar")
print("Tanınan Yüz",len(yuzler))
print("Tanınan Kişi",len(etiketler))
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(yuzler,np.array(etiketler))
def kare_ciz(img,rect):
    (x,y,w,h) = rect
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

def yazi_yaz(img,yazi,x,y):
    cv2.putText(img,yazi, (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0,255,0),2)

def predict(test_img):
    img = test_img
    yuz,rect = yuztespit(img)
    etiket = face_recognizer.predict(yuz)
    etiket_ic = elemanlar[etiket[0]]
    kare_ciz(img,rect)
    yazi_yaz(img,etiket_ic,rect[0],rect[1]-5)
    cv2.imshow("deneme",test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

test_img = cv2.imread("deneme.jpg")
predict_img = predict(test_img)
test_img = cv2.imread("cem.jpg")
predict_img = predict(test_img)