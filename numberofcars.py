import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im=cv2.imread('traffic.jpg')
bbox, label, conf=cv.detect_common_objects(im)
oimage=draw_bbox(im,bbox,label,conf)
plt.imshow(oimage)
plt.show()
print("Number of cars in image: "+str(label.count('car')))
