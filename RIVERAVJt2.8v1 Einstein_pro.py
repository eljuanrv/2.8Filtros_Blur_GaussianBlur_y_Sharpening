#RIVERA VARGAS JUAN


import cv2
import numpy as np
from matplotlib import pyplot as plt

img2 = cv2.imread('ein.jpg',0)

filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpen_img_2=cv2.filter2D(img2,-1,filter)


titles = ['Original','Sharpening']
images = [img2,sharpen_img_2]
miArray = np.arange(2)
for i in miArray:
  plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()
