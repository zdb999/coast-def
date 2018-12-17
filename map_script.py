import cv2
import os
import numpy as np
from coastdef.animate import animate_flood, animate_flood2
import coastdef.utils as utils
from osgeo import gdal, ogr, osr
from coastdef.geo import make_extent_layer

e1 = cv2.getTickCount()

make_extent_layer('test2.tiff', [(5000, 4000)], 14)

# animate_flood('test2.tiff', [(5000, 4000)], 98, 100, 1, 1)

# animate_flood2('test4.tiff', [(850, 850)], 0, 84, 1, 12)

# make_extent_layer('test.tiff', [(5, 5)], 37)

# animate_flood('test.tiff', [(5, 5), (650,1050), (1050,650)], 3, 83, 1, 10)

# from osgeo import ogr, osr
# driver = ogr.GetDriverByName('ESRI Shapefile')
# dataset = driver.Open(r'Walls.shp')
# layer = dataset.GetLayer()
# inSpatialRef = layer.GetSpatialRef()

# from osgeo import gdal, ogr

# # Define pixel_size and NoData value of new raster
# pixel_size = 1
# NoData_value = -9999

# # Filename of input OGR file
# vector_fn = 'Walls.shp'

# # Filename of the raster Tiff that will be created
# raster_fn = 'test2 (copy).tiff'

# # Open the data source and read in the extent
# target_ds = gdal.Open(raster_fn)
# source_ds = ogr.Open(vector_fn)
# source_layer = source_ds.GetLayer()

# # x_min, x_max, y_min, y_max = source_layer.GetExtent()

# # # Create the destination data source
# # x_res = int((x_max - x_min) / pixel_size)
# # y_res = int((y_max - y_min) / pixel_size)
# # target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
# # target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
# # band = target_ds.GetRasterBand(1)
# # band.SetNoDataValue(NoData_value)

# # Rasterize
# gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[40])

# animate_flood(raster_fn, [(5000, 4000)], 0, 80, 10, 8)






# from osgeo import ogr
# import os

# shapefile = "Walls.shp"
# driver = ogr.GetDriverByName("ESRI Shapefile")
# dataSource = driver.Open(shapefile, 0)
# source_layer = dataSource.GetLayer()

# target_ds = gdal.Open("test4.tiff")
# proj = target_ds.GetProjection()
# print proj

# outband = target_ds.GetRasterBand(1)

# gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[70])

# from osgeo import gdal, ogr

# Define pixel_size and NoData value of new raster
pixel_size = .0002
NoData_value = 255

driver = ogr.GetDriverByName('ESRI Shapefile')
# Filename of input OGR file
vector_fn = 'Walls.shp'

# Filename of the raster Tiff that will be created
# raster_fn = 'out.tif'

# # Open the data source and read in the extent
# source_ds = ogr.Open(vector_fn)
# source_layer = source_ds.GetLayer()

# dem_ds = gdal.Open("test4.tiff")
# proj = dem_ds.GetProjection()
# print proj
# h, w = np.shape(np.array(dem_ds.GetRasterBand(1).ReadAsArray()))

# in_sr = source_layer.GetSpatialRef()

# out_sr = osr.SpatialReference()
# out_sr.ImportFromWkt(proj)

# coordTrans = osr.CoordinateTransformation(in_sr, out_sr)

# outputShapefile = r'junk.shp'
# if os.path.exists(outputShapefile):
#     driver.DeleteDataSource(outputShapefile)
# outDataSet = driver.CreateDataSource(outputShapefile)

# for i, feature in enumerate(source_layer):

#   out_layer_name = "out_" + str(i)
#   outLayer = outDataSet.CreateLayer(out_layer_name, geom_type=ogr.wkbLineString)
#   outLayerDefn = outLayer.GetLayerDefn()
#   height = feature.GetField("height")
#   height = int(height*10)
#   # print int(height)
#   geom = feature.GetGeometryRef()
#   geom.Transform(coordTrans)
#   outFeature = ogr.Feature(outLayerDefn)
#   outFeature.SetGeometry(geom)
#   outLayer.CreateFeature(outFeature)
#   gdal.RasterizeLayer(dem_ds, [1], outLayer, burn_values = [height]) #options = ["attributes='new_height'"])
#   outLayer = None
#   dem_ds.FlushCache


# # x_min, x_max, y_min, y_max = source_layer.GetExtent()

# # Create the destination data source
# x_res = int((x_max - x_min) / pixel_size)
# y_res = int((y_max - y_min) / pixel_size)
# target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, w, h, 1, gdal.GDT_UInt32)
# target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
# band = target_ds.GetRasterBand(1)
# band.SetNoDataValue(NoData_value)


# # # Rasterize
# gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values = [200]) #options = ["attributes='new_height'"])


# target_ds = None
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time