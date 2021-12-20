#RIVERA VARGAS JUAN


import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('ojo.jpg',0)

#blur
blurred_2 = cv2.blur(img1,(15,15))
#gaussian_blur
Gaussian_blurred_1 = cv2.GaussianBlur(img1,(25,25),0)

titles = ['Original','Blur','Gaussian Blur']
images = [img1,blurred_2,Gaussian_blurred_1]
miArray = np.arange(3)
for i in miArray:
  plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()