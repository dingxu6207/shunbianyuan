# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:25:11 2019

@author: dingxu
"""

from astropy.io import fits
import numpy as np
from skimage import io,exposure
import matplotlib.pyplot as plt

hdu = fits.open('E:/shunbianyuan/ldf_download/20190531M31-18object/M31%20A2.fts')
imgdata = hdu[0].data


########################################
##拉伸对比度
rows,cols = imgdata.shape

minimagedata = imgdata.min()
maximagedata = imgdata.max()

for i in range(rows):
    for j in range(cols):
        if (imgdata[i,j] > maximagedata):
            imgdata[i,j] = 255
        elif (imgdata[i,j] < minimagedata):
            imgdata[i,j] = 0
        else:
            imgdata[i,j] = 255*((imgdata[i,j] - minimagedata)/(maximagedata - minimagedata))
            
u8imagedata = np.uint8(imgdata)            
u8imagedata = exposure.adjust_gamma(u8imagedata, 0.3) 

'''
##############################################
##根据直方图进行二值化
reimagedata = u8imagedata
yiweidata=reimagedata.flatten()
n, bins, patches = plt.hist(yiweidata, bins=256,density=0,edgecolor='None',facecolor='red')
plt.show()
'''

############################################
##图像二值化
erzhiimage = np.zeros((rows,cols),dtype = 'uint8')
threshold = 100
erzhiimage = np.where(u8imagedata < threshold, 255, 0)

io.imshow(erzhiimage)
plt.show()
io.imsave('E:/shunbianyuan/M31%20A2.jpg',erzhiimage)