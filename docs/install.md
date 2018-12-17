# Installing CoastDef

## On a Desktop

To get CoastDef on your personal computer, you can clone the repository by running the command

``git clone https://github.com/zdb999/coast-def.git``

You can then install all of the package's dependencies, located in `requirements.txt`.

`pip install -r coast-def/requirements.txt`

The package is still unreleased, and on some systems you may encounter installation difficulties. We make no claim that your installation will be uneventful. If some dependencies don't install, you can run supplementary commands.

``sudo apt-get install libgdal-dev
apt-get install python-gdal``

To learn more about CoastDef's dependencies, visit our [dependencies page](https://github.com/zdb999/coast-def/network/dependencies).

We have not yet developed a setup to add CoastDef to your Python enviroment varibles. You can either do this manuelly or run your scripts with a in the CoastDef folder. Improving installation will be a major priority once the the core components are all useable.

## Using Google Colab

As shown in [this tutorial](https://colab.research.google.com/drive/1_0oFoE9svyGNdtWJNRWvAowjIsnhreFx), it is currently mutch easier to run CoastDef in a virtual, Cloud-based enviroment. We recoment Google Colab. It's free, easy to use, and facilitates teamwork. Colab is also based on open source [Jupyter notebooks](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

To set up the latest version of CoastDef in Colab, simply copy this script into a Colab code block and run it.

``
import os
import sys
installed = True

try:
  import gdal
  import pymc3
  import coastdef

except:
  installed = False
  !apt-get update >/dev/null
  !apt-get install libgdal-dev -y >/dev/null
  !apt-get install python-gdal -y >/dev/null
  !pip install -r coast-def/requirements.txt > /dev/null
  sys.path.insert(0,'/content/coast-def/')
  
if not os.path.isdir("coast-def"):
  installed = False
  !git clone https://github.com/zdb999/coast-def.git >/dev/null

if installed:
  print "Everything is already installed!"
else:
  print "Install complete!"
``

# GIS Software

 Making full use of this package will require some Geographic Information Systems (GIS) background. Both ArcGIS and QGIS should work fine; if you don't have such software, you can download the open-source QGIS [here](https://qgis.org/en/site/forusers/download.html).  And [here](https://learn.arcgis.com/en/) is a good introductory ArcGIS tutorial, and here is a good QGIS [one](https://docs.qgis.org/2.8/en/docs/gentle_gis_introduction/).
