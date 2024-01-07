import cv2
import numpy as np 
img= cv2.imread(r'E:\multimedia\img\cat.jpg')
cv2.imshow('before',img)
#img=cv2.resize(img,(400,500))p

image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh,bimage1)=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

(thresh,bimage2)=cv2.threshold(image,150,200,cv2.THRESH_BINARY)

#both_image= np.hstack([image,bimage2,bimage2])

cv2.imshow('Black&White_image_width_1st_threshold_value',bimage1)
cv2.waitKey(0)
cv2.imshow('Black&White_image_width_2nd_value',bimage2)
cv2.waitKey(0)
cv2.destroyallWindows()