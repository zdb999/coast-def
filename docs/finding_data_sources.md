
# Finding Data Sources -- Test

This guide is intended to help you find the data you need to get started modelling. It is incomplete, and will always be a work in progress. If you have suggestions about other potential data sources, please create a [Github issue](https://github.com/zdb999/coast-def/issues) or email the project's maintainers at [{{site.email}}](mailto:{{site.email}}).

## Geospatial Data for the Model

### DEM Data

CoastDef needs digital elevation data to simulate flooding conditions. That data must come in a GeoTIFF format; GeoTIFF can be opened by ordinary image views but contaion special metadata about their geographic location. Each pixel represents an an x-y coordinate pair, while the "color" represents the elevation. (Confusingly, this third demension often has a different scale, so you should check the metadata that comes with the file.)

There is free digital elevation data available for just about everywhere in the world. If you have access to it, Esri's catalog has many raster lidar datasets to chose from, with a multitude of sources and resolutions.

However, most DEM data is created by governments, and is posted online for free. it just takes a little searching to find it. The website [GIS Geography](https://gisgeography.com/free-global-dem-data-sources/) has a good primer on some of them.

For US-based analyses, one of the best DEM sources is the National Oceanic and Atmospheric Administration (NOAA) [Data Access Viewer](https://coast.noaa.gov/dataviewer/#/). In addition to their geospatial data collections, NOAA also hosts hundreds of other DEM datasets created by other organizations.

The Data Viewer has a host of tools that make getting the DEM you need easy. You can clip the data to the area you wish to analyze, change the units and projection reference, and fill in measurement holes in the lidar grid. You can also get "land" lidar data, which excludes pixels over water and buildings. Whether you want this last feature depends on your CoastDef data processing workflow.

The examples for this project were downloaded with NOAA's Data Access Viewer, and were drawn from Conneticut's 2016 [Orthophotography and Lidar survey](https://cteco.uconn.edu/data/flight2016/index.htm).

GeoTIFFs are not designed to be directly interpredeted with human eyes, so don't worry if you can't see anything when you open it.


### Water Points

"Water points" are data points which let CoastDef know where bodies of water are, a crucial feature of its flood extent algorithm. That algorithm, `geo.flood_extent`, finds marks pixels as underwater if and only if the are

- under the designated `surge_height`
- connected by a contiguous chain of other underwater pixels directly to a "water point"

The first criterion means that our water will not flood islands or pockets of land which are higher than the water level. The second criterion means that  low-lying areas that are protected by higher land or structures will be safe until those protections are over-toped. This allows us to model walls and other landscape interventions easily; by changing a few DEM pixels along the intervention, we can predict new flood patterns behind it.

Unfortunately, you are going to have to create these points yourself in GIS software, most likely QGIS or ArcGIS. Our introductory guide to GIS can be found [here](install.md).[^1] First, you will need to create a point-based shapefile. Next, you will use GIS to insert your waterpoints. Finally, you will save you changes and import your shapefile into CoastDef.

Valid water points must

- Be within the bounds of your DEM file's geographic extent
- Be located on a permanent body of water

You can input as many water points as you like, and sometimes having multiple points is necessary to define all of your water locations.[^2] However, usually only one valid point is necessary, and extra points just slow CoastDef down.

[^1]: If you are a Python programmer you can also use the free and open-source GDAL](https://www.gdal.org/) for this. we used GDAL to program the geospatial components of our CoastDef.

[^2]: This often happens when the connection between two submerged areas is cut off by the border of the DEM file.

### Property Values 

### Structure Outlines Data

### Wall Data

## Data for Probabilistic Modeling

### Surge Height Distributions

### Sea Level Rise

### Wall Costs

### Social Costs of Flooding

### Risk Aversion

