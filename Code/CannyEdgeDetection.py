# Marquette Brachial FMD Automated Calculator
#
# This program uses a dual doppler flow and vessel ultrasound image
# of the Brachial artery to detect FMD (Flow Modulated Dilation). FMD detects
# the change in shear stress on the artery and indicates the cardiac health
# of an individual.
#
# Main.py is the intended startup executable for Marquette FMD Calculator

# !!!!!!!!! This current version will not support complex GUI, only hardcoded
# !!!!!!!!! image paths and local outputs until imaging process is consistent and
# !!!!!!!!! can be pushed to actual user case tests
#
# last edit: Daniel Whipple 9/23/2019
# https://blog.sicara.com/opencv-edge-detection-tutorial-7c3303f10788

import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt
import time

# Trying some simple image processing with the artery .avi files
# this file path won't work on your computer id its not the same
print("Opening .avi file")
artery_vid = cv2.VideoCapture('C:\\Git\\FMD_Senior_Design\\Sample_Images\\2017Dec08 Study__[0001464]\\14.05.25 hrs '
                              '__[0011697].avi')
if artery_vid.isOpened() == False:
    print("Couldn't open the .avi file")
    sys.exit()

## stages of edge detection (CANNY EDGE DETECTION)
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html#canny
#1 noise reduction (i used gaussian filter)
#2 detect edge gradient (usin sobel kernal)
#3 generate binary image by removing non max pixels
#4 hysteresis thresholding, detect true edges

print("Filtering the image")
# capture video
ret, frame = artery_vid.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 20, 30)
edges_high_thresh = cv2.Canny(gray, 60, 120)
images = np.hstack((gray, edges, edges_high_thresh))
cv2.imshow('Frame', images)
cv2.waitKey(0) # close windows if any key is pressed
# artery_vid.release()
cv2.destroyAllWindows()

print("Filtered Image Wiped")