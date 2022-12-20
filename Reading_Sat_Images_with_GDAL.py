# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:50:10 2022

@author: oo_wa
"""

from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

def scaleMinMax(x):
    return(x - np.min(x)/(np.max(x))-np.min(x))

images_dir='dset-s2/dset-s2/tra_scene/'
masks_dir='dset-s2/dset-s2/tra_truth/'

ds = gdal.Open(images_dir+'S2A_L2A_20190125_N0211_R034_6Bands_S1.tif')
#mask1 = gdal.open(masks_dir+'S2A_L2A_20190125_N0211_R034_S1_Truth.tif')

#bands
r = ds.GetRasterBand(4).ReadAsArray() #red band
g = ds.GetRasterBand(3).ReadAsArray()
b = ds.GetRasterBand(2).ReadAsArray()

any1 = ds.GetRasterBand(1).ReadAsArray()
any2 = ds.GetRasterBand(5).ReadAsArray()
any3 = ds.GetRasterBand(6).ReadAsArray()

#r = scaleMinMax(r)
#g = scaleMinMax(g)
#b = scaleMinMax(b)

ds = None

rgb=np.dstack((r,g,b))

plt.figure()
plt.imshow(rgb)
plt.show()