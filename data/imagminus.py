# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:22:09 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from skimage import measure

hduA1 = fits.open('M33 A1.fts')
imagedataA1 = hduA1[0].data

hduA2 = fits.open('M33 A2.fts')
imagedataA2 = hduA2[0].data



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

    matdata = (imagedata-Imin)/(Imax-Imin)
    min0data = np.where(matdata < 0,0,matdata)
    min1data = np.where(min0data < 1,min0data*255,255)

    return np.uint8(min1data)



'''
plt.figure(1)
plt.imshow(resultA1, cmap='gray')

plt.figure(2)
plt.imshow(resultA2, cmap='gray')
'''


 
def qiuzuobiao(img):
    resultA = img
    flattenA1 = resultA.flatten()
    n, bins, patches = plt.hist(flattenA1, bins=256, density=1, facecolor='green', alpha=0.75)

    maxn = np.max(n)
    yuzhi = np.where(n == maxn)
    threhold = int(yuzhi[0])+40

    erzhiA1 = (resultA >= threhold)*1.0
    filterA1 = signal.medfilt(erzhiA1,(3,3)) #二维中值滤波

    labels = measure.label(filterA1,connectivity = 2) #8 连通区域标记
    print('regions number:',labels.max()+1) #显示连通区域块数(从 0 开始标

    regionnum = labels.max()+1

    hang,lie = resultA.shape
    plotx = np.zeros(regionnum,dtype = np.uint)
    ploty = np.zeros(regionnum,dtype = np.uint)

    for k in range(regionnum):
        sumx = 0
        sumy = 0
        area = 0
        for i in range(hang):
            for j in range(lie):
                if (labels[i][j] == k):
                    sumx = sumx+i
                    sumy = sumy+j
                    area = area+1
        plotx[k] = int(sumx/area)
        ploty[k] = int(sumy/area)
    return plotx,ploty,regionnum
    
 
    
resultA1 = whadjustimage(imagedataA1)
A1plotx,A1ploty,A1regionnum = qiuzuobiao(resultA1)  

plt.figure(1)
plt.imshow(resultA1, cmap='gray')  

for i in range(A1regionnum):
    plt.plot(A1ploty[i],A1plotx[i],'*')
    
plt.show()

resultA2 = whadjustimage(imagedataA2)
plt.figure(2)
plt.imshow(resultA1, cmap='gray')  


