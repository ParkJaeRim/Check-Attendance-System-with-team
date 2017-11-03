import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=raw_input('Enter your ID')
img = cv2.imread('file name.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
timestr =time.strftime("%Y%m%d-%H%M%S")
imgNum = timestr

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)] 
    #save image 
    cv2.imwrite(str(imgNum) + Id + ".png", cropped) 
    imgNum += str()

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
