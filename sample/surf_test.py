#! /usr/bin/python
# -*- encoding: utf-8 -*-


import cv
from sys import *
'''
引数に画像のパスを指定するとsurfを表示します。
'''
im =  cv.LoadImageM(argv[1] , cv.CV_LOAD_IMAGE_GRAYSCALE)
(keypoints , descriptors) = cv.ExtractSURF(im,
                                           None,
                                           cv.CreateMemStorage(),
                                           (1 , 500, 3, 4))

for ((x , y) , laplacian , size , dir , hessian) in keypoints:
    cv.Circle(im, (int(x),int(y)),
              int(hessian/1000),
              cv.RGB(255 , 255 , 255),
              1,
              cv.CV_AA , 0)

cv.SaveImage("face_detected.jpg", im)
#cv.ShowImage("aaa",im)
