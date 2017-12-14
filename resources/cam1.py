from picamera import PiCamera
from time import sleep
from datetime import datetime


camera = PiCamera()
#now = datetime.today().strftime("%m-%d_%H:%M:%S")
camera.resolution = (2592,1944)
camera.framerate = 15

camera.start_preview()
for i in range(2):
    camera.capture('./images%s.jpg'%i)
    sleep(3)
camera.stop_preview()
    
#camera.start_preview()
#sleep(3)

#camera.stop_preview()

# Add text
#from picamera import Picamera, Color
#camera.annotate_background = Color('blue')
#camera.annotate_foreground = Color('yellow')
#camera.annotate_text = "Check"
#camera.annotate_text_size = 100

