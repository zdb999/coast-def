import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
from cv2 import VideoWriter
from PIL import ImageFont, ImageDraw, Image
import coastdef.utils as utils
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

  contours, hier = cv2.findContours(dummy,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  # Enable more garbage collection
  del dummy

  # Go through each water point, and see what contours contain it.
  # Keep track of the contours contours found

  water_cnts = []
  water_cnt_indeces = []

  # Get ride of useless dimension

  hier = hier[0,:,:]

  # Undo the shift that occured with dummy. Sadly we can't vectorize this.

  for c in contours:

      c[:,0,:] = c[:,0,:] -2 

  # Check water points

  for point in points:

    found_cnt_count = 0

    for i, c in enumerate(contours):

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
      water_cnt_indeces.append(index)

  # Generate output

  out_img = np.full((h,w), 255, np.uint8)
  cv2.fillPoly(out_img, water_cnts, (0))

  # Take into account the possiblity of islands, lakes on islands, etc

  fixes_todo = []

  # Check each valid water contour for this condition, add fixes for children

  for cnt_index in water_cnt_indeces:

    child = hier[cnt_index][2]

    if child != -1: # Child exists

      # is_island must be true as we are in the top level

      fixes_todo.append((child, True)) #(cnt_index, is_island)

  while fixes_todo != []:

    # find the line in the hierarchy for the cnt, child, sibling find cnt
    cnt_index, is_island = fixes_todo.pop()
    cnt = contours[cnt_index]
    child = hier[cnt_index][2]
    sibling = hier[cnt_index][0]

    # Make adjustment to image

    # Always fill in island

    if is_island:
      cv2.fillPoly(out_img, [cnt], (255))

    # Don't fill in depression unless there is a water point there

    else:
      for point in points:
        if cv2.pointPolygonTest(c, point, False) > 0:
          cv2.fillPoly(out_img, [cnt], (0))

    # Add child to stack

    if child != -1: # Child exists

      child_is_island = not is_island
      fixes_todo.append((child, child_is_island))

    # Add sibiling to stack

    if sibling != -1: # Sibling exists

      fixes_todo.append((sibling, is_island))


  cv2.drawContours(out_img, contours, -1, (255,255,0), 2)

  return out_img


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
