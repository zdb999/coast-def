import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
import Image, ImageDraw
gdal.UseExceptions()

def world2Pixel(geoMatrix, x, y):
  """
  Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
  the pixel location of a geospatial coordinate
  """
  ulX = geoMatrix[0]
  ulY = geoMatrix[3]
  xDist = geoMatrix[1]
  yDist = geoMatrix[5]
  rtnX = geoMatrix[2]
  rtnY = geoMatrix[4]
  pixel = int((x - ulX) / xDist)
  line = int((ulY - y) / xDist)
  return (pixel, line)

# img = cv2.imread('test.tiff',-1)
raster = gdal.Open('test.tiff')
extent = raster.GetGeoTransform()
img = np.array(raster.GetRasterBand(1).ReadAsArray())
print extent

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
e1 = cv2.getTickCount()

h,w = np.shape(img)
base2 = np.full((h,w,3), 255, np.uint8)
base3 = np.full((h,w,3), 255, np.uint8)
base = np.full((h,w), 255, np.uint8)


ret,thresh = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

out = thresh.astype(np.uint8)
dummy = np.zeros((h+4, w+4), np.uint8)
dummy[2:h+2,2:w+2] = out
dummy[1,:] = 255
dummy[h+1,:] = 255
dummy[:,1] = 255
dummy[:,w+1] = 255
contours, hierarchy = cv2.findContours(dummy,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

found_contour = False
for i, c in enumerate(contours):
	c[:,0,:] = c[:,0,:] -2
	if cv2.pointPolygonTest(c, (5,5), False) > 0:
		area = cv2.contourArea(c)
		if not found_contour:
			cnt = c
			found_contour = True
			index = i
			min_size_so_far = area
		elif found_contour and  area < min_size_so_far:
			min_size_so_far = area
			cnt = c
			index = i

cv2.fillPoly(base, [cnt], (0))
cv2.imshow('image', cv2.bitwise_or(thresh.astype(np.uint8), base))#cv2.addWeighted(base3,1.0,base2,0.0,0))
cv2.waitKey(2000)
cv2.destroyAllWindows()
# base_blah = np.full((h,w,3), 255, np.uint8)
# cv2.fillPoly(base_blah, [cnt_blah], (255,0,0))
# cv2.imshow('image',base_blah)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
cv2.imshow('image',np.array())
cv2.waitKey(2000)
cv2.destroyAllWindows()
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time