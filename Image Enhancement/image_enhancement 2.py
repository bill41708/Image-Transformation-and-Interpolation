import cv2
import numpy as np

img0 = cv2.imread('dark.jpg')
img1 = cv2.imread('bright.jpg')
img2 = cv2.imread('gray.jpg')
img3 = cv2.imread('normal.jpg')

def gamma_trans(img,gamma):
    #具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    #实现映射用的是Opencv的查表函数
    return cv2.LUT(img,gamma_table)

img0_corrted = gamma_trans(img0, 0.5)
cv2.imwrite('dark_gamma05.jpg',img0_corrted)
'''
cv2.imshow('img0',img0)
cv2.waitKey()
cv2.imshow('gamma_image',img0_corrted)
cv2.waitKey()
'''

img0_corrted = gamma_trans(img0, 2)
cv2.imwrite('dark_gamma2.jpg',img0_corrted)

img1_corrted = gamma_trans(img1, 0.5)
cv2.imwrite('bright_gamma05.jpg',img1_corrted)

img1_corrted = gamma_trans(img1, 2)
cv2.imwrite('bright_gamma2.jpg',img1_corrted)

img2_corrted = gamma_trans(img2, 0.5)
cv2.imwrite('gray_gamma05.jpg',img2_corrted)

img2_corrted = gamma_trans(img2, 2)
cv2.imwrite('gray_gamma2.jpg',img2_corrted)

img3_corrted = gamma_trans(img3, 0.5)
cv2.imwrite('normal_gamma05.jpg',img3_corrted)

img3_corrted = gamma_trans(img3, 2)
cv2.imwrite('normal_gamma2.jpg',img3_corrted)





