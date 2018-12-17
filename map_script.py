import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
from cv2 import VideoWriter
from PIL import ImageFont, ImageDraw, Image
from coastdef.animate import animate_flood
import coastdef.utils as utils
from coastdef.geo import make_extent_layer
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


e1 = cv2.getTickCount()



make_extent_layer('test2.tiff', [(5000, 4000)], 14)

animate_flood('test2.tiff', [(5000, 4000)], 7, 12, 1, 2)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time