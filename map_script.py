import cv2
import numpy as np
from coastdef.animate import animate_flood
import coastdef.utils as utils
from coastdef.geo import make_extent_layer

e1 = cv2.getTickCount()

make_extent_layer('test2.tiff', [(5000, 4000)], 14)

animate_flood('test2.tiff', [(5000, 4000)], 0, 80, 1, 8)

# make_extent_layer('test.tiff', [(5, 5)], 37)

# animate_flood('test.tiff', [(5, 5), (650,1050), (1050,650)], 3, 83, 1, 10)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time