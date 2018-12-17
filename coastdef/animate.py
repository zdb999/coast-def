import cv2
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
from cv2 import VideoWriter
from PIL import ImageFont, ImageDraw, Image
import utils
import geo
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


def animate_flood(dem_path, water_points, low, high, step, duration):

  # Open DEM layer

  raster, img, projection, transform = utils.import_dem(dem_path)

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
      frame[:,:,1] = geo.flood_extent(img, points, low + i*step)
      if i == 0:
        frame[:,:,2] = geo.flood_extent(img, points, low + i*step)

      out_str = str(i/10.) + " ft"
      text_frame = add_text_overlay(frame, out_str, (4500,3500), 400, "./fonts/Vera.ttf", (255,255,255))
      # cv2.putText(frame,'Water flooding',(300,300), font, 50,(255,255,255),2,lineType=3)
      # cv2.circle(text_frame,(5000, 4000), 63, (0,0,255), -1)
      video.write(text_frame)
      frame[:,:,2] = frame[:,:,1]
  video.release()
