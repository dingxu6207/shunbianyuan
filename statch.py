# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:40:16 2019

@author: dingxu
"""

import cv2 
import numpy as np

MIN_MATCH_COUNT = 4

img1 = cv2.imread('v1.jpg')

img2 = cv2.imread('v2.jpg')

g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()

match = cv2.FlannBasedMatcher(dict(algorithm =2, trees =1), {})

kp1, de1 = sift.detectAndCompute(g1,None)

kp2, de2 = sift.detectAndCompute(g2,None)

m = match.knnMatch(de1, de2, 2)

m = sorted(m,key = lambda x:x[0].distance)

ok = [m1 for (m1, m2) in m if m1.distance < 0.7 * m2.distance]

'''
if len(ok)>MIN_MATCH_COUNT:

    pts0 = np.float32([ kp1[i.queryIdx].pt for i in ok]).reshape(-1,1,2)

    pts1 = np.float32([ kp2[i.trainIdx].pt for i in ok]).reshape(-1,1,2)

    M, mask = cv2.findHomography(pts0,pts1, cv2.RANSAC,5.0)

    h,w = img1.shape[:2]

    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

    dst = cv2.perspectiveTransform(pts,M)

    cv2.polylines(img2,[np.int32(dst)],True,(0,255,0),3, cv2.LINE_AA)

else:

    print( "匹配点的数目不够！ - {}/{}".format(len(ok),MIN_MATCH_COUNT))
'''
    
med = cv2.drawMatches(img1,kp1,img2,kp2,ok,None)

cv2.imwrite('med.jpg',med)
cv2.imshow('0',med)
cv2.waitKey(0)
cv2.destroyAllWindows()
