# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:59:49 2019

@author: bill4
"""

import cv2
import math
import numpy as np
import time


red = (255, 0, 0)

def nearest_neighbor_interpolation(image,angle):
    height, width, channels = image.shape
    anglePi = angle * math.pi / 180.0
    csin = math.sin(anglePi)
    ccos = math.cos(anglePi)
    
    length = math.ceil(height * (csin + ccos))
    #print(width, height, channels)
    iSRotate = create_blank(length, length, channels)
    '''
    print(height)
    print('型態:', type(height))
    print('物件大小:', sys.getsizeof(height))
    print('-'*30)
    '''
    
    nedge = (length - 1) / 2
    ox = -nedge * ccos - nedge * csin + (width - 1) / 2
    oy = nedge * csin - nedge * ccos + (height - 1) / 2
    
    
    for i in range(length):
        for j in range(length):
            x = int(ccos * j + csin * i + ox)
            y = int(-csin * j+ ccos * i + oy)
            #if x>-1 and x<height and y>-1 and y<width:
            if x >-1 and x < height and y > -1 and y < width:
                iSRotate[i,j] = image[y,x]
    
            
    
    return iSRotate            
    




def xvalue(x, width): # column bounding and floor the number
    if x < 0:
        x = 0
    elif x >= width:
        x -= 1
    return math.floor(x)

def yvalue(y, height): # row bounding and floor the number
    if y < 0:
        y = 0
    elif y >= height:
        y -= 1
    return math.floor(y)


def bilinear_interpolation(image,angle): 
    height, width, channels = image.shape
    anglePi = angle * math.pi / 180.0
    csin = math.sin(anglePi)
    ccos = math.cos(anglePi)
    
    length = math.ceil(height * (csin + ccos))
    iSRotate = create_blank(length, length, channels)
    
    # offset
    nedge = (length - 1) / 2
    ox = -nedge * ccos - nedge * csin + (width - 1) / 2
    oy = nedge * csin - nedge * ccos + (height - 1) / 2
    
    for y in range(length):
        for x in range(length):            
            srcy = -x * csin + y * ccos + oy
            srcx = x * ccos + y * csin + ox
            if srcy >=0 and srcy < height and srcx >= 0 and srcx < width:
                u = srcx - int(srcx)
                v = srcy - int(srcy)
                iSRotate[y][x] = ((1 - u) * (1 - v) * image[yvalue(srcy, height)][xvalue(srcx, width)] +
                        u * (1 - v) * image[yvalue(srcy, height)][xvalue(srcx + 1, width)] +
                        (1 - u) * v * image[yvalue(srcy + 1, height)][xvalue(srcx, width)] +
                        u * v * image[yvalue(srcy + 1, height)][xvalue(srcx + 1, width)])

    return iSRotate




def create_blank(width, height, channels):
    image = np.zeros((height, width, channels), np.uint8)

    return image



#image = cv2.imread('C:\\Users\\bill4\\.spyder\\jp.png')
image = cv2.imread('letter.png')
image1 = cv2.imread('scene512.jpg')

tStart = time.time()
iSRotate = nearest_neighbor_interpolation(image,30)
cv2.imwrite('nearest_neighbor_interpolation_letter.jpg', iSRotate)
#cv2.imshow('Display Window', iSRotate)
#cv2.waitKey(0)
tEnd = time.time()

#print("It cost %f sec" % (tEnd - tStart)) #會自動做近位
print(tEnd - tStart) #原型長這樣


tStart = time.time()

iSRotate = bilinear_interpolation(image,30)
cv2.imwrite('bilinear_interpolation_letter.jpg', iSRotate)
#cv2.imshow('Display Window', iSRotate)
#cv2.waitKey(0)
tEnd = time.time()

#print("It cost %f sec" % (tEnd - tStart)) #會自動做近位
print(tEnd - tStart) #原型長這樣

tStart = time.time()
iSRotate = nearest_neighbor_interpolation(image1,30)
cv2.imwrite('nearest_neighbor_interpolation_scene.jpg', iSRotate)
#cv2.imshow('Display Window', iSRotate)
#cv2.waitKey(0)
tEnd = time.time()
#print("It cost %f sec" % (tEnd - tStart)) #會自動做近位
print(tEnd - tStart) #原型長這樣

tStart = time.time()
iSRotate = bilinear_interpolation(image1,30)
cv2.imwrite('bilinear_interpolation_scene.jpg', iSRotate)
#cv2.imshow('Display Window', iSRotate)
#cv2.waitKey(0)
tEnd = time.time()
#print("It cost %f sec" % (tEnd - tStart)) #會自動做近位
print(tEnd - tStart) #原型長這樣
