# USAGE
# python stitch.py --first v8.png --second v7.png 

# import the necessary packages
from picamera import PiCamera
from time import sleep
from datetime import datetime
from pyimagesearch.panorama import Stitcher
from datetime import datetime
import argparse
import imutils
import numpy as np
import cv2

now = datetime.today().strftime("%y-%m-%d %H:%M:%S")

#camera = PiCamera()
#camera.resolution = (2592,1944)
#camera.framerate = 15

#for i in range(2):
#    camera.capture('./images.jpg')
#    sleep(3)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")
ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
#cv2.imwrite("v87.jpg", result)
#cv2.imwrite("v87_matches_1.jpg", vis)

# show the images
#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
#cv2.imshow("Keypoint Matches", vis)
#cv2.imshow("Result", result)


 
#body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
body_cascade = cv2.CascadeClassifier('./resources/haarcascades/haarcascade_mcs_upperbody.xml')
 
#img = cv2.imread('v87_1.jpg')
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
outfile = open('Attendance.txt', 'a')
outfile.write(str(now)+'\n')

 
body = body_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in body:
	cv2.rectangle(result,(x,y),(x+w,y+h),(255,0,0),2)
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
cv2.imwrite("final.jpg", result)

