# this assumes the files are 640x480 and match the cropped range of the sample image
# import contours as contours
# copyright Marquette University 11/25/2019

import cv2
import numpy

from FileSupport import *

def VerifyContour(contour, min_size):
    # -------- Detect Small Shapes --------
    if cv2.arcLength(otsu_contours[i_shape], True) < min_size: # hardcoded for now obviously
        return False
    else:
        return True

def LargestContourSize(c_arr):
    # finds largest perimiter and returns size
    largest_c = 0
    for i_shape in range(len(c_arr)):
        temp = cv2.arcLength(c_arr[i_shape], True)
        if temp > largest_c:
            largest_c = temp
    return largest_c


# Declared Variables ###########################
# file vars
# image_file_name = '14.05.25 hrs __[0011697].avi'  # this will be given through some file selection of the user
# image_file_name = '14.13.37 hrs __[0011703].avi'
image_file_name = '14.05.51 hrs __[0011699].avi'
temp_image_file_path = ReturnTempImagePath()  # gives file path for .avi files to be stored
# image vars
sample_start_row = 144  # measurements are based off the 640x480 sample image
sample_end_row = 408
sample_start_col = 159
sample_end_col = 518
# colors
RED = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# Pull image ###################################
print("Getting image from ", image_file_name, "\n")

artery_vid = cv2.VideoCapture(ReturnImagePath(image_file_name))
if not artery_vid.isOpened():
    print("Couldn't open file")
    sys.exit()  # some popup for the user that the file couldn't be opened

success, image = artery_vid.read()
i_frame = 0
while success:  # this is where big files might mess up if every frame is saved
    # crop the image before saving it (using user generated values?)
    image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
    cv2.imwrite(temp_image_file_path + "frame%i.jpg" % i_frame, image)

    # -----draw around artery-------
    img = cv2.imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
    light_img = img
    otsu_hierarchy, otsu_threshold = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    otsu_contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # TREE vs EXTERNAL & SIMPLE vs NONE
    light_hierarchy, light_threshold = cv2.threshold(light_img, 35, 255, cv2.THRESH_BINARY)

    #print("n Contours found : ", str(len(otsu_contours)))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # add this line
    intense_img = img;
    light_img = cv2.cvtColor(light_img, cv2.COLOR_GRAY2BGR)  # add this line

    cv2.imshow("Image Without Contours", image)  # contour is also destructive
    cv2.drawContours(img, otsu_contours, -1, GREEN, 1)  # this image should be showing lines around high contrast areas
    cv2.imshow("Image With Otsu Contours", img)
    cv2.imshow("Image with Otsu Thresholding", otsu_threshold)
    # cv2.imshow("Image with Light Thresholding", light_threshold)

    # ==================== Trace Inner Artery
    # try to print child contours in blue over contoured img

    # --------intensive detection----------------
    # min size should prolly be based of some log graph
    min_c_size = LargestContourSize(otsu_contours) * .1

    for i_shape in range(len(otsu_contours)):
        # print(cv2.contourArea(otsu_contours[i_shape]))
        if VerifyContour(otsu_contours[i_shape], min_c_size):
            cv2.drawContours(intense_img, otsu_contours, i_shape, GREEN, 1)
        else:
            cv2.drawContours(intense_img, otsu_contours, i_shape, RED, 1)
        # ignore small shapes
        # estimate line edge of artery

    cv2.imshow("Intense Filtered Shapes", intense_img)
    # ====================

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # ---------------------------------------------

    print("Image %i Complete" % i_frame, "\n")
    i_frame += 1
    success, image = artery_vid.read()
