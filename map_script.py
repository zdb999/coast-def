import cv2
import os
import numpy as np
from coastdef.animate import animate_flood, animate_flood2, animate_flood3
import coastdef.utils as utils
from osgeo import gdal, ogr, osr
from coastdef.geo import make_extent_layer


e1 = cv2.getTickCount()

# make_extent_layer('sample_data/test2.tiff', [(5000, 4000)], 14)

# animate_flood('sample_data/test2.tiff', [(5000, 4000)], 98, 100, 1, 1)

# make_extent_layer('sample_data/test2.tiff', [(5000, 4000)], 14)

animate_flood2('sample_data/SeasideDEMwalls.tif', [(850, 850)], 0, 30, 1, 1)

# animate_flood3('sample_data/test2.tiff', [(5000, 4000)], 98, 100, 1, 1)

# raster = gdal.Open('SeasideDEM.tif')
# b = np.array(raster.GetRasterBand(1).ReadAsArray())
# cv2.imwrite("outDEM.tif", b)
# print np.shape(b)

# Open DEM layer

# raster = gdal.Open('SeasideDEM.tif',gdal.GA_Update)

# outband = raster.GetRasterBand(1)

# stuff = cv2.imread('wallDEM.tif')
# outband.WriteArray(stuff[:,:,1])
# outband.FlushCache()


# animate_flood3('sample_data/SeasideDEM.tif', [(850, 850)], 2018, 2150, 1, 20)

# make_extent_layer('sample_data/test.tiff', [(5, 5)], 37)

# animate_flood('sample_data/test.tiff', [(5, 5), (650,1050), (1050,650)], 3, 83, 1, 10)

# print utils.import_dem('sample_data/Back.tif')
# utils.reproject('sample_data/test2.tiff', 'sample_data/Back3.tif', 'sample_data/dem_cropped.tiff')

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time