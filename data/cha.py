# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:14:12 2019

@author: dingxu
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hduA1 = fits.open('M33 A1.fts')
imagedataA1 = hduA1[0].data
hang,lie = imagedataA1.shape

hduA2 = fits.open('M33 A2.fts')
imagedataA2 = hduA2[0].data

###显示图像###
def whadjustimage(img):
    imagedata = img
    mean = np.mean(imagedata)
    sigma = np.std(imagedata)
    mindata = np.min(imagedata)
    maxdata = np.max(imagedata)
    Imin = mean - 3*sigma
    Imax = mean + 3*sigma

    if (Imin < mindata):
        Imin = mindata
    else:
        Imin = Imin

    if (Imax > maxdata):
        Imax = maxdata
    else:
        Imax = Imax
        
    for i in range(hang):
        for j in range(lie):
            if (imagedata[i][j] < Imin):
                imagedata[i][j] = 0
            elif (imagedata[i][j] > Imax):
                imagedata[i][j] = 255
            else:
                imagedata[i][j] = 255*(imagedata[i][j]-Imin)/(Imax-Imin)
    return np.uint8(imagedata)

newimage = np.zeros((hang,lie),dtype = np.uint16)
newimage[0:hang-9,0:lie-4] =  imagedataA1[9:hang,4:lie]
minusimage = np.float32(newimage)-np.float32(imagedataA2)


plt.figure(1)    
A1image = whadjustimage(imagedataA1)
plt.imshow(A1image, cmap='gray')

plt.figure(2)    
A2image = whadjustimage(imagedataA2)
plt.imshow(A2image, cmap='gray')

plt.figure(3)    
A3image = whadjustimage(minusimage)
plt.imshow(A3image, cmap='gray')