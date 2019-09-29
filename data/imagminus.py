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
imagedataA1F = imagedataA1[0:600,0:600]

hduA2 = fits.open('M33 A2.fts')
imagedataA2 = hduA2[0].data
imagedataA2F = imagedataA2[0:600,0:600]
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

    matdata = (imagedata-Imin)/(Imax-Imin)
    min0data = np.where(matdata < 0,0,matdata)
    min1data = np.where(min0data < 1,min0data*255,255)

    return np.uint8(min1data)


###求坐标##
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
    
 
    
resultA1 = whadjustimage(imagedataA1F)
A1plotx,A1ploty,A1regionnum = qiuzuobiao(resultA1)  

plt.figure(1)
plt.imshow(resultA1, cmap='gray')  
fluxA1 = np.zeros(A1regionnum,dtype = np.uint)
listdataA1 = [0 for i in range(A1regionnum)]
for i in range(A1regionnum):
    plt.plot(A1ploty[i],A1plotx[i],'*')
    fluxA1[i] = np.sum(resultA1[A1plotx[i]-6:A1plotx[i]+6,A1ploty[i]-6:A1ploty[i]+6]) 
    listdataA1[i] = (A1plotx[i],A1ploty[i],fluxA1[i] )
listdataA1.sort(key=lambda x:x[2])
plt.show()

plt.figure(2)
resultA2 = whadjustimage(imagedataA2F)
A2plotx,A2ploty,A2regionnum = qiuzuobiao(resultA2)
plt.imshow(resultA2, cmap='gray') 
fluxA2 = np.zeros(A2regionnum,dtype = np.uint)
listdataA2 = [0 for i in range(A2regionnum)]
for i in range(A2regionnum):
    plt.plot(A2ploty[i],A2plotx[i],'*') 
    fluxA2[i] = np.sum(resultA2[A2plotx[i]-6:A2plotx[i]+6,A2ploty[i]-6:A2ploty[i]+6])
    listdataA2[i] = (A2plotx[i],A2ploty[i],fluxA2[i] )
listdataA2.sort(key=lambda x:x[2])    
plt.show()

plt.figure(3)
plt.imshow(resultA1, cmap='gray') 
plt.show()

plt.figure(4)
plt.imshow(resultA2, cmap='gray') 
plt.show()




 


