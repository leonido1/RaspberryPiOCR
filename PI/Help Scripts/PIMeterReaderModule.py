import cv2
import numpy
from time import sleep



class BoundingBox():

      def __init__(self,left,right,top,bottom):

          self.left=left
          self.right=right
          self.top=top
          self.bottom=bottom


      def setLightOn(self):
          self.light=Light['ON']


      def setLightOff(self):
          self.light=Light['OFF']




class Meter():
    meterRead=10



primaryCheckArea=BoundingBox(247,267,137,147)
seconderyCheckArea=BoundingBox(230,250,180,190)


thrashOld=50000

Light={'OFF':0,'ON':1}





def sample():

    primaryCheckArea.setLightOn()
    seconderyCheckArea.setLightOn()

    

    while True:

        cap = cv2.VideoCapture(0)

        ret,currentMeterFrame=cap.read()
        sleep(0.06)
           
        if isChanged(currentMeterFrame):
            Meter.meterRead+=1
            print(Meter.meterRead)
            setCorrectLight(currentMeterFrame)

        cap.release()
         

    

def isChanged(frame):

    if isBoxChanged( frame,primaryCheckArea):
        return True

    if isBoxChanged(frame,seconderyCheckArea):
        return True

    return False
    

def isBoxChanged(img,box):

    lower,upper = 200,255

    img = img[box.top:box.bottom,box.left:box.right]

    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    binary_img=cv2.threshold(img,lower,upper,cv2.THRESH_BINARY)

    sumOfPixels=sum(sum(sum(binary_img)))
 
    lightsOn=sumOfPixels>thrashOld
    
    if lightsOn==True and box.light==Light['OFF']:
        return True

    

    if lightsOn==False and box.light==Light['ON']:
        return True

   
    return False


def setCorrectLight(frame):

  

    if isBoxChanged(frame,primaryCheckArea):

        if primaryCheckArea.light==Light['OFF']:
            primaryCheckArea.light=Light['ON']

        else:
            primaryCheckArea.light=Light['OFF']



    if isBoxChanged(frame,seconderyCheckArea):

        if seconderyCheckArea.light==Light['OFF']:
            seconderyCheckArea.light=Light['ON']

        else:
            seconderyCheckArea.light=Light['OFF']




    
