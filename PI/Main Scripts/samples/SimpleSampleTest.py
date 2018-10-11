import cv2
import numpy


isOn=True
thresold=70000

count=0

x1=384          
y1=200
x2=396
y2=220
top=255
bottom=127


def startSample():

    

    while True:

        cap=cv2.VideoCapture(0)
        ret,img=cap.read()

       
        if isChanged(img)==True:
            print("changed")
 
        cap.release()






def isChanged(img):


    global isOn
    global count
     
    img_crop=img[y1:y2,x1:x2]

    img_crop=cv2.cvtColor(img_crop,cv2.COLOR_RGB2GRAY)

    img_binary=cv2.threshold(img_crop,bottom,top,cv2.THRESH_BINARY)


    #if count%1==0:
    #    print(sum(sum(sum(img_binary))))
    #    count+=1

    if (thresold>sum(sum(sum(img_binary)))) and isOn==True:
        isOn=False
        return True

    elif (thresold<sum(sum(sum(img_binary)))) and isOn==False:
        isOn=True
        return True


    return False  

        
