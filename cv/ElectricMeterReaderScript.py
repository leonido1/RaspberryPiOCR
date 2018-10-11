import cv2
import numpy



Light={"Off":0,"On":1}
threashold=100000


class Meter():
  meterReading=1700

def Main():

  cap = cv2.VideoCapture(0)

  while True:

    ret,frame=cap.read()
  
