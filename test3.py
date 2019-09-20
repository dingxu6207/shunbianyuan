# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:07:46 2019

@author: dingxu
"""
import numpy as np
from skimage import io
import struct

image = io.imread('starimag.jpg')
hang,lie =  image.shape

filename = 'test.fits'

f = open(filename, "wb")


charsimple = [' ' for i in range(79)]
charsimple[0:8] = 'SIMPLE  ='
charsimple[29] = 'T'
strsimple = ''.join(charsimple)
encodesimple = strsimple.encode('gbk')
f.write(encodesimple)

charbitpix = [' ' for i in range(79)]
charbitpix[0:8] = 'BITPIX  ='
charbitpix[29] = '2'
charbitpix[28] = '3'
charbitpix[27] = '-'
strbitpix = ''.join(charbitpix)
encodebitpix = strbitpix.encode('gbk')
f.write(encodebitpix)


charNAXIS = [' ' for i in range(79)]
charNAXIS[0:8] = 'NAXIS   ='
charNAXIS[29] = '2'
strNAXIS = ''.join(charNAXIS)
encodeNAXIS = strNAXIS.encode('gbk')
f.write(encodeNAXIS)

charNAXIS1 = [' ' for i in range(79)]
charNAXIS1[0:8] = 'NAXIS1  ='
charNAXIS1[29] = '4'
charNAXIS1[28] = '2'
charNAXIS1[27] = '0' 
charNAXIS1[26] = '1'
strNAXIS1 = ''.join(charNAXIS1)
encodeNAXIS1 = strNAXIS1.encode('gbk')
f.write(encodeNAXIS1)


charNAXIS2 = [' ' for i in range(79)]
charNAXIS2[0:8] = 'NAXIS2  ='
charNAXIS2[29] = '4'
charNAXIS2[28] = '2'
charNAXIS2[27] = '0' 
charNAXIS2[26] = '1'
strNAXIS2 = ''.join(charNAXIS2)
encodeNAXIS2 = strNAXIS2.encode('gbk')
f.write(encodeNAXIS2)

charEXTEND = [' ' for i in range(79)]
charEXTEND[0:8] = 'EXTEND  ='
charEXTEND[29] = 'T'
strEXTEND = ''.join(charEXTEND)
encodeEXTEND = strEXTEND.encode('gbk')
f.write(encodeEXTEND)

charEND = [' ' for i in range(79)]
charEND[0:2] = 'END'
strEND = ''.join(charEND)
encodeEND = strEND.encode('gbk')
f.write(encodeEND)

charkong = [' ' for i in range(80)]
strkong = ''.join(charkong)
encodekong = strkong.encode('gbk')
for j in range(29):
    f.write(encodekong)

data = np.zeros((1024,1024),dtype = np.float)
image = image.T
data = image.astype(np.float)

for i in range(1024):
    for j in range(1024):
      bytes = struct.pack('f',data[i][j])
      f.write(bytes)

dcharkong = [' ' for i in range(1856)]
dstrkong = ''.join(dcharkong)
dencodekong = dstrkong.encode('gbk')
f.write(dencodekong)
    
f.close()
