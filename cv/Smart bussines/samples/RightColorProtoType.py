import cv2
import numpy

Thresold=45000

top=150
bottom=100

img=cv2.imread("/home/pi/Desktop/frame_cropped.jpg")

img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)



img_binary=cv2.threshold(img,bottom,top,cv2.THRESH_BINARY)

print(sum(sum(sum(img_binary))))

cv2.imwrite("/home/pi/Desktop/frame_binary.jpg",img )         
