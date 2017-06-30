"""
=============================================
DESQ (Dry Eyes Syndrome Quantifier)
=============================================
AUTHOR: Om Prakash S
Date: 30-06-2017
Engineering the Eye 5
SRUJANA Center for Innovation
---------------------------------------------
Python Code to Detect if a Image contains
Region of Interest in the Lipid surface layer.
----------------------------------------------
The resultant Image contains the Regions which
which contains Interference Pattern.
----------------------------------------------
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

path='img/img1.jpg' #Path to Captured Image

orig = cv2.imread(path) #Original Image = cv2.imread(path,0) #Grayscale Image


blur = cv2.GaussianBlur(gray,(5,5),0)
#th3 containing thresholded Image.
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 

#np.set_printoptions(threshold='nan')

#Replaces all 255s with 1
th3[th3 == 255] = 1

#Add extra column to the Thresholded matrix
th3 = th3[..., None]

#Image Subtraction to retrieve ROI in Original Image
new_image = np.multiply(th3,orig)

#Image after processing in JPG format
cv2.imwrite('img/result/img1_AP.jpg', new_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

#Uncomment Below lines to Print Actual Image and Normal Image

#cv2.imshow("New Image",new_image)
#cv2.imshow("Actual Image",orig)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
