"""A module with useful tools, like file imports and unit coversions."""

# TODO: Other file imports

import os
import sys
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr
gdal.UseExceptions()

# Find the path of the script running the software

sys.argv[0]
real_path = os.path.realpath(sys.argv[0])
real_path = os.path.dirname(os.path.abspath(real_path)) + r"/"

#Set up for unit conversion
# everything is based off meters internally

convert_table = {'m':1}
convert_table['km'] = 0.001
convert_table['cm'] = 100.
convert_table['mm'] = 1000.
convert_table['ft'] = 3.28084
convert_table['feet'] = 3.28084
convert_table['in'] = 39.37008
convert_table['yrd'] = 1.09361
convert_table['yards'] = 1.09361
convert_table['mi'] = 0.00062137121212121
convert_table['miles'] = 0.00062137121212121
convert_table['nmi'] = 0.000539955174946
convert_table['nautical mile'] = 0.000539955174946


def convert_unit(value, from_unit, to_unit):
  """Convert distance units from one unit to another.

  Args:
    value (float or int): The value to be converted.
    from_unit (str): The short name of the value's unit.
    to_unit (str): The short name of the desired unit.

  Returns:
    float: The value in its new units.
  """

  # Check for bad inputs

  assert from_unit in convert_table, "Unfortunately, {} is not a unit we know.".format(from_unit)
  assert to_unit in convert_table, "Unfortunately, {} is not a unit we know.".format(to_unit)
  
  #Convert to meters then to desired unit

  meters = float(value) / convert_table[from_unit]
  return meters * convert_table[to_unit]


def import_dem(dem_path):
  """Import DEM file data

  Args:
    dem_path (.tiff file path): The location of the DEM data.

  Returns:
    gdal dataset:The file's imported dataset object
    numpy array: A numpy-ready representaton of the data values
    gdal projection: The coordinate system of the file
    gdal geo transform: The definition of the image's bounderies
      in the coordinate system of the projection."""

  path = real_path + dem_path

  try:
    raster = gdal.Open(path)

  except:
    raise Exception('The supplied DEM file path does not point to valid DEM file.')
  
  try:
    projection = raster.GetProjection()
    transform = raster.GetGeoTransform()
    img = np.array(raster.GetRasterBand(1).ReadAsArray())
    return raster, img, projection, transform

  except:
     raise Exception('The supplied DEM file has no GEO data.')

# TODO
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
