# ----------------Artery Detection Prototype--------------------------
# This program takes .avi ultrasound files and contours each frame based on otsu thresholding. To progress to the next frame
# the spacebar will clear the current image and generate the next frame.
# This file assumes the .avi files are 640x480 and match the cropped range of the sample image.
#
# copyright Marquette University

import cv2
import numpy
from FileSupport import *

# ------------------Functions-----------------------------------
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONBLCLK:
        cv2.circle(artery_im, (x, y), 100, RED, -1)
        mouseX,mouseY = x,y
        print(x)
        print(y)
        click_true = True

# ------------------ Variables ----------------------
global click_true
click_true = False
# file vars ------
image_file_name = '14.05.25 hrs __[0011697].avi'  # this will be given through some file selection of the user
# image_file_name = '14.13.37 hrs __[0011703].avi' # different .avi file to test
# image_file_name = '14.05.51 hrs __[0011699].avi'
temp_image_file_path = ReturnTempImagePath()  # gives file path for .avi files to be stored
# image vars -------
sample_start_row = 144  # measurements are based off the 640x480 sample image
sample_end_row = 408
sample_start_col = 159
sample_end_col = 518
# colors --------
RED = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# -------------------Code-------------------------------
# Pull image =======================================================
print("Getting image from ", image_file_name, "\n")
artery_vid = cv2.VideoCapture(ReturnImagePath(image_file_name))

if not artery_vid.isOpened():
    print("Couldn't open file")
    sys.exit()
success, artery_im = artery_vid.read()

# Process and contour each .avi frame ===============================
i_frame = 0
while success:
    # saves the current frame. Not necessary but may be used in final product
    artery_im = artery_im[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
    # cv2.imwrite(temp_image_file_path + "frame%i.jpg" % i_frame, artery_im)

    # wait for user to click
    cv2.setMouseCallback("Pre Processing", draw_circle)

    cv2.imshow("Pre Processing", artery_im)

    # Convert image to grayscale
    artery_im = cv2.imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
    # Perform Threshold
    otsu_hierarchy, otsu_threshold = cv2.threshold(artery_im, 0, 255, cv2.THRESH_OTSU)
    # Find contours (edges)
    otsu_contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # TREE vs EXTERNAL & SIMPLE vs NONE
    # Convert image to color so contours can be printed in color
    artery_im = cv2.cvtColor(artery_im, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Image with Otsu Thresholding", otsu_threshold)
    # --------intensive detection----------------

    # wait until a key is pressed, then delete current images and generate next frame
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image %i Complete" % i_frame, "\n")
    i_frame += 1
    success, artery_im = artery_vid.read()