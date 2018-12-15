import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
from cv2 import VideoWriter
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

def flood_extent(dem, points, height, out_name="flood_extent"):

	# Get DEM data, initalize outputs
	h,w = np.shape(dem)

	ret,thresh = cv2.threshold(dem,height,255,cv2.THRESH_BINARY)

	# We don't use ret, so let's delete it so it can be cleaned
	# if we are close to running out of memeory

	del ret

	# Find contours. Open CV's countours identifier doesnt identify
	# edges, so we copy the image into a h+4,w+4 dummy canvas and create 
	# lines between the DEM and the artificial edge of the image. Open CV
	# can then recognze those contours. It;s hackish, but it works.

	thresh = thresh.astype(np.uint8)
	dummy = np.zeros((h+4, w+4), np.uint8)
	dummy[2:h+2,2:w+2] = thresh

	thresh

	# Draw those lines

	dummy[1,:] = 255
	dummy[h+1,:] = 255
	dummy[:,1] = 255
	dummy[:,w+1] = 255

	# Find those contours. Having an optimized method here is worth
	# the trouble. At some point we could find the C code for this,
	# modifiy it to allow edge contour completion, and compile it 
	# ourselves. This could save some time and memory

	contours, hierarchy = cv2.findContours(dummy,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	# Enable more garbage collection
	del dummy
	del hierarchy

	# Go through each water point, and see what contours contain it.
	# Keep track of the countour ar

	found_contour = False

	for point in points:
		for i, c in enumerate(contours):
			c[:,0,:] = c[:,0,:] -2 # Undo the shift that occured with dummy
			if cv2.pointPolygonTest(c, point, False) > 0: 
				area = cv2.contourArea(c)
				if not found_contour: # First contour with point inside
					cnt = c
					found_contour = True
					index = i
					min_size_so_far = area
				elif found_contour and  area < min_size_so_far: # Challenger
					min_size_so_far = area
					cnt = c
					index = i

	# Generate output

	out = np.full((h,w), 255, np.uint8)
	cv2.fillPoly(out, [cnt], (0))

	# Take into account the possiblity of islands

	out = cv2.bitwise_or(thresh.astype(np.uint8), out)

	# Return result


	# cv2.imshow('image', out)
	# cv2.waitKey(40)

	return out

	# cv2.destroyAllWindows()

def import_raster(raster_path):

	try:
		raster = gdal.Open(raster_path)
	except:
		 raise Exception('The supplied DEM file path does not point to valid DEM file.')

	try:
		projection = raster.GetProjection()
		transform = raster.GetGeoTransform()
		return (raster, projection, transform)
	except:
		 raise Exception('The supplied DEM file has no GEO data.')


def make_extent_layer(dem_path, water_points, height, out_path = "flood_extent"):

	# Open DEM layer

	raster, projection, transform = import_raster(dem_path)

	# TODO: implement water points, change this

	points = water_points

	# Load numpy version of image and load xy coorinates

	img = np.array(raster.GetRasterBand(1).ReadAsArray())
	h,w = np.shape(img)

	# Make output file
	driver = gdal.GetDriverByName('GTiff')
	outRaster = driver.Create(out_path, w, h, 1, gdal.GDT_Byte)
	outband = outRaster.GetRasterBand(1)
	outRaster.SetGeoTransform(transform)
	outRaster.SetProjection(projection)

	# Find extent and write it to file
	outband.WriteArray(flood_extent(img, points, 10))
	outband.FlushCache()

def animate_flood(dem_path, water_points, low, high, step, duration):

	# Open DEM layer

	raster, projection, transform = import_raster(dem_path)

	# TODO: implement water points, change this

	points = water_points

	# Load numpy version of image and load xy coorinates

	img = np.array(raster.GetRasterBand(1).ReadAsArray())
	h,w = np.shape(img)

	seconds = duration
	FPS = int((high - low) / float(step * duration))


	fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
	video = VideoWriter('./out.avi', fourcc, FPS, (w, h))

	frame = np.full((h,w,3), 255, np.uint8)
	for i in range(FPS*seconds):
	    frame[:,:,1] = flood_extent(img, points, low + i*step)
	    if i == 0:
	    	frame[:,:,2] = flood_extent(img, points, low + i*step)
	    video.write(frame)
	    frame[:,:,2] = frame[:,:,1]
	video.release()

	# for i in range(80):
	# 	flood_extent(img, [(5,5)], i)
	# cv2.destroyAllWindows()
make_extent_layer('test.tiff', [(5,5)], 14)

animate_flood('test.tiff', [(0,0)], 7, 100, 1, 5)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time