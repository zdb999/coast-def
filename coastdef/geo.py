import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
from cv2 import VideoWriter
from PIL import ImageFont, ImageDraw, Image
import coastdef.utils as utils


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


def flood_extent(dem, points, height):

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
  # Keep track of the contours contours found

  water_cnts = []

  for point in points:

    found_cnt_count = 0

    for i, c in enumerate(contours):

      c[:,0,:] = c[:,0,:] -2 # Undo the shift that occured with dummy

      if cv2.pointPolygonTest(c, point, False) > 0: 
        area = cv2.contourArea(c)
        if found_cnt_count == 0: # First contour with point inside
          cnt = c
          found_cnt_count += 1
          index = i
          min_size_so_far = area
        elif found_cnt_count > 0 and  area < min_size_so_far: # Challenger
          min_size_so_far = area
          cnt = c
          found_cnt_count += 1
          index = i

    if found_cnt_count > 1:
      water_cnts.append(cnt)

  # Generate output

  out = np.full((h,w), 255, np.uint8)
  cv2.fillPoly(out, water_cnts, (0))

  # Take into account the possiblity of islands

  out = cv2.bitwise_or(thresh.astype(np.uint8), out)

  return out


def make_extent_layer(dem_path, water_points, height, out_path = "flood_extent"):

  # Open DEM layer

  raster, img, projection, transform = utils.import_dem(dem_path)

  # TODO: implement water points, change this

  points = water_points

  # Get xy coorinates

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
