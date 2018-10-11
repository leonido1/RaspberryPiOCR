import cv2
import numpy

#primary
#x1=247          
#y1=137
#x2=267
#y2=147

#secondary
x1=230          
y1=180
x2=250
y2=190



img = cv2.imread("/home/pi/Desktop/frame.jpg")

img_crop=img[y1:y2,x1:x2]


  
img=cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)


cv2.imwrite("/home/pi/Desktop/frame_cropped.jpg",img_crop)

cv2.imwrite("/home/pi/Desktop/frame.jpg",img)
