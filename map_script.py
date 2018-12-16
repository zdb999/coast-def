import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
from cv2 import VideoWriter
from PIL import ImageFont, ImageDraw, Image
gdal.UseExceptions()


def add_text_overlay(image, text, origin, size, font, color):
  # Load image in OpenCV  
    
   # Convert the image to RGB (OpenCV uses BGR)  
   cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
     
   # Pass the image to PIL  
   pil_im = Image.fromarray(cv2_im_rgb)  
     
   draw = ImageDraw.Draw(pil_im)  
   # use a truetype font  
   font = ImageFont.truetype(font, size)  
     
   # Draw the text  
   draw.text(origin, text, font=font, fill=color)  
     
   # Get back the image to OpenCV  
   return cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

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

def import_dem(dem_path):

  raster, projection, transform = import_raster(dem_path)
  img = np.array(raster.GetRasterBand(1).ReadAsArray())
  return raster, img, projection, transform

def import_water_points(shape_path):

  try:
    driver = ogr.GetDriverByName('ESRI Shapefile')
    points_file = driver.Open(shape_path, 0)

  except:
    raise Exception('The supplied water points file path does not point to valid shapefile.')

  try:
    layer = points_file.GetLayer()

  except:
    pass



def make_extent_layer(dem_path, water_points, height, out_path = "flood_extent"):

  # Open DEM layer

  raster, img, projection, transform = import_dem(dem_path)

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

def animate_flood(dem_path, water_points, low, high, step, duration):

  # Open DEM layer

  raster, img, projection, transform = import_dem(dem_path)

  # TODO: implement water points, change this

  points = water_points

  # Define font

  font = cv2.FONT_HERSHEY_SIMPLEX

  # Load numpy version of image and load xy coorinates

  h,w = np.shape(img)

  # Calculate frame rate
  seconds = duration
  FPS = int((high - low) / float(step * duration))

  # Encode and name
  fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
  video = VideoWriter('./out.avi', fourcc, FPS, (w, h))

  frame = np.full((h,w,3), 255, np.uint8)

  # Generate first frame
  frame = np.full((h,w,3), 255, np.uint8)

  # Create and write frames
  for i in range(FPS*seconds):
      frame[:,:,1] = flood_extent(img, points, low + i*step)
      if i == 0:
        frame[:,:,2] = flood_extent(img, points, low + i*step)

      out_str = str(i/10.) + " ft"
      text_frame = add_text_overlay(frame, out_str, (4500,3500), 400, "./fonts/Vera.ttf", (255,255,255))
      # cv2.putText(frame,'Water flooding',(300,300), font, 50,(255,255,255),2,lineType=3)
      # cv2.circle(text_frame,(5000, 4000), 63, (0,0,255), -1)
      video.write(text_frame)
      frame[:,:,2] = frame[:,:,1]
  video.release()

make_extent_layer('test2.tiff', [(5000, 4000)], 14)

animate_flood('test2.tiff', [(5000, 4000)], 7, 67, 1, 2)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time