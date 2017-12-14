from datetime import datetime
import numpy as np
import cv2

now = datetime.today().strftime("%y-%m-%d_%H:%M:%S")

body_cascade = cv2.CascadeClassifier('./resources/haarcascades/haarcascade_mcs_upperbody.xml')


img = cv2.imread('c3.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
outfile = open('Attendance.txt', 'a')
outfile.write(str(now)+'\n')

body = body_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in body:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	a=[]
	a.append(x)
	a.append(y)
	a.append(x+w)
	a.append(y+h)
	print(a)
	outfile.write(str(a) + '\n')
	
outfile.write('\n')
outfile.close()
#cv2.imshow('img',img)
cv2.imwrite("c3_body.jpg", img)
