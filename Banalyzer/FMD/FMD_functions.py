# This is simplified code without gui link
# TODO THIS IS A DEAD FILE


import cv2
import numpy as np
import math
from brachial_ui import UpdateImage
from FileSupport import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time
# note for later. have each fmd iteration have its own class and calss name
# so it can store n_frames, fmd, other info
# ------------------ Variables ----------------------
# file
image_file_name = '14.05.25 hrs __[0011697].avi'
temp_image_file_path = ReturnTempImagePath()
# colors
RED = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
# UI   REOMVE THE CLICK STUFF
im_x, im_y, click_allowed = 164, 150, True


# ------------------Functions-----------------------------------
# left click saves x,y coordinate and right click resets the x,y and allows a re-click
# This saves the in_x and im_y as the xy coordinates of the click. They should be accessible anywhere
def click_event(event, x, y, flags, param):
    global im_x, im_y, click_allowed
    if event == cv2.EVENT_LBUTTONDOWN:
        # allows the user to click again to select the center if true
        click_allowed = False
        print("clicked on [", x, " ", y, "]")
        cv2.circle(image, (x, y), 2, RED, -1)
        cv2.imshow("Pre Processing", image)
        im_x, im_y = x, y
        Populate(image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # reset click
        click_allowed = True

# outputs the difference between two coordinates
# c = [x y]
def coord_dist(c0, c1):
    dx2 = (c0[0] - c1[0]) ** 2
    dy2 = (c0[1] - c1[1]) ** 2
    return math.sqrt(dx2 + dy2)


# boxpoints does lowest corner first, then goes clockwise
# This assumes the centerline we want is longer than the vertical centerline. So this could
# cause bugs if the defined box has artifact or problem causing it to be tall/skinny
def box_centerline(rec):
    # first try any centerline
    c0 = rec[0]  # corner 1 (this one is very bottom corner)
    c1 = rec[1]
    c2 = rec[2]
    c3 = rec[3]
    # xy coord assuming bottom right is c0
    x1 = np.mean([c0[0], c1[0]])
    y1 = np.mean([c0[1], c1[1]])
    x2 = np.mean([c2[0], c3[0]])
    y2 = np.mean([c2[1], c3[1]])
    # xy coord assuming bottom left is c0
    xa = np.mean([c0[0], c3[0]])
    ya = np.mean([c0[1], c3[1]])
    xb = np.mean([c2[0], c1[0]])
    yb = np.mean([c2[1], c1[1]])
    # since the bottom corner is not associated with bottom right/left
    # the longer center line is returned (ASSUMPTION that longer centerline is horizontal)
    if coord_dist([x1, x2], [y1, y2]) > coord_dist([xa, xa], [yb, yb]):
        return np.array([[x1, y1], [x2, y2]])
    return np.array([[xa, ya], [xb, yb]])


# checks for points that are perpendicular to the center-line
# tang is tangent coord [[xa ya] [xb yb]] so two coord
def Tang_Diam_Mean(contour, tang):
    # need to look into why the xa xb are inverse what I thought.
    # probably need to change the box center line function
    xb = tang[0][0]
    yb = tang[0][1]
    xa = tang[1][0]
    ya = tang[1][1]
    # print("xya, xyb [", xa, ":", ya, "] [", xb, ":", yb, "]")
    slope = (ya - yb) / (xa - xb)
    # print("slope: ", slope)
    y_int = ya + xa * slope
    # print("y int: ", y_int)
    tang_slope = -(1 / slope)  # negative reciprocal
    # print("neg recip slope: ", tang_slope)

    # for now imma hardcode 10 points. later should be iterative with left/right buffer width
    # this part finds 10 points on the centerline and uses the tangent to find points on the contour
    n_bins = 10
    length = coord_dist(tang[0], tang[1])
    length_bin = length / (n_bins + 1)
    bin_arr = np.linspace(length_bin, length - length_bin, n_bins)
    # print(bin_arr)
    for x in bin_arr:
        coord = [x, slope * x + y_int]
        # print(coord)
        # dont have this working so return is not important
    return y_int


# populates all of the filtered/detected shape images. This function performs all aspects of their generation
def Populate(img, img_obj):
    # Convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
    # Gaussian smooth (need to investigate if we need)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    # Invert Image
    copy = np.invert(img)  # !!!!!!!!!!!!!!!!!!!!! used to see if quality of image changes
    # Perform Threshold
    _, otsu_threshold = cv2.threshold(copy, 0, 255, cv2.THRESH_OTSU)
    # Find contours (edges)
    otsu_contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)  # TREE vs EXTERNAL & SIMPLE vs NONE
    # Convert image to color so contours can be printed in color
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # If multiple shapes contain coordinate this will break. Need case
    for i_shape in range(len(otsu_contours)):
        # are the coordinates contained within the shape
        if 1 == cv2.pointPolygonTest(otsu_contours[i_shape], (im_x, im_y), False):
            cv2.drawContours(img, otsu_contours, i_shape, GREEN, 1)
            # enclose box around the contour. This could also be used to re crop image and perform thresholding again
            simp_box = cv2.minAreaRect(otsu_contours[i_shape])
            simp_box = cv2.boxPoints(simp_box)
            cv2.drawContours(img, [np.int0(simp_box)], 0, BLUE, 2)
            # cv2.drawContours(img, )
            # print(simp_box)
            center_xy = box_centerline(simp_box)
            # print(center_xy[0])
            # print(center_xy[1])
            dead = Tang_Diam_Mean(otsu_contours, center_xy)
            cv2.circle(img, tuple([0, dead]), 3, RED, 2)
            cv2.line(img, tuple(center_xy[0]), tuple(center_xy[1]), RED, 2)
    OpenCv2QImage(img, img_obj)
    #cv2.imshow("Image with detected contours", img)

# to set up widget class ... https://stackoverflow.com/questions/32226074/display-opencv-window-on-top-of-pyqts-main-window
# should update pyqt5 label
def OpenCv2QImage(opcv_img, image_obj):
    height, width, channel = opcv_img.shape
    bytes_per_line = 3 * width
    pix_img = QtGui.QImage(opcv_img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
    image_obj.setPixmap(QtGui.QPixmap.fromImage(pix_img))
    image_obj.repaint()


# this will run the FMD process once an image has been verified.
def PerformFMD(image_path, image_obj):
    artery_avi = cv2.VideoCapture(image_path)
    if not artery_avi.isOpened():
        print("Couldn't open file")
        # change to a button alert
        return
    success, image = artery_avi.read()

    # Process and contour each .avi frame ===============================
    i_frame = 0
    while success:
        # !!!!!!!!!!!!!!!!!!Delete once cropping method determined!!!!!!!!!!
        sample_start_row = 144  # measurements are based off the 640x480 sample image
        sample_end_row = 408
        sample_start_col = 159
        sample_end_col = 518
        image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # saves the current frame. Not necessary but may be used in final product
        # image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
        cv2.imwrite(temp_image_file_path + "frame%i.jpg" % i_frame, image)

        # !!!!!!!! need to implement a clicking opportunity within the GUI
        # !!!!!!!! the coord should already be saved by user, this func shouldnt happen until
        # the user clicks 'accept' or 'run'

        time.sleep(.01)
        Populate(image, image_obj)

        print("Image %i Complete" % i_frame, "\n")
        i_frame += 1
        success, image = artery_avi.read()
