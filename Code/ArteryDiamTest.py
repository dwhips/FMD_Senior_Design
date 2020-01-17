# ----------------Artery Detection Prototype--------------------------
# This program takes .avi ultrasound files and contours each frame based on otsu thresholding. To progress to the next frame
# the spacebar will clear the current image and generate the next frame.
# This file assumes the .avi files are 640x480 and match the cropped range of the sample image.
#
# copyright Marquette University

import cv2
import numpy
from FileSupport import *

# ------------------ Variables ----------------------
im_x, im_y, click_allowed = 1, 1, True

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

# ------------------Functions-----------------------------------
# Example algorithm for removing non artery shapes that removes small shapes
def VerifyContour(contour, min_size):
    # -------- Detect Small Shapes --------
    if cv2.arcLength(otsu_contours[i_shape], True) < min_size: # hardcoded for now
        return False
    else:
        return True

# Finds the largest perimeter in a contour object
def LargestContourPerim(c_arr):
    # finds largest perimeter and returns size
    largest_c = 0
    for i_shape in range(len(c_arr)):
        temp = cv2.arcLength(c_arr[i_shape], True)
        if temp > largest_c:
            largest_c = temp
    return largest_c

# left click saves x,y coordinate and right click resets the x,y and allows a reclick
def click_event(event, x, y, flags, param):
    global im_x, im_y, click_allowed
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_allowed:
            click_allowed = False # only should allow click once
            print("clicked on [", x, " ", y, "]")
            cv2.circle(image, (x, y), 2, RED, -1)
            cv2.imshow("Pre Processing", image)
            im_x, im_y = x, y
            # call populate fucnt
    if event == cv2.EVENT_RBUTTONDOWN:
        click_allowed = True
        im_x, im_y = -1, -1

def Populate():
    return
# -------------------Code-------------------------------
# Pull image =======================================================
print("Getting image from ", image_file_name, "\n")
artery_vid = cv2.VideoCapture(ReturnImagePath(image_file_name))

if not artery_vid.isOpened():
    print("Couldn't open file")
    sys.exit()
success, image = artery_vid.read()

# Process and contour each .avi frame ===============================
i_frame = 0
while success:
    # saves the current frame. Not necessary but may be used in final product
    image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
    cv2.imwrite(temp_image_file_path + "frame%i.jpg" % i_frame, image)

    cv2.imshow("Pre Processing", image)
    # clickable event. if is redundant, but meant to reduce resource usage
    if (click_allowed):
        cv2.setMouseCallback("Pre Processing", click_event)
    else:
        a = 1
        # call the populate function
        # have wait key after this

    # all this shit should be in the populate filtered image funct. So if the click_allowed is true
    # then populate() is called once image is clicked
    # other wise they will populate automatically as the center hasnt been detected

    # Convert image to grayscale
    img = cv2.imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
    # Invert Image
    img = numpy.invert(img)
    # Perform Threshold
    otsu_hierarchy, otsu_threshold = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    # Find contours (edges)
    otsu_contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # TREE vs EXTERNAL & SIMPLE vs NONE
    # Convert image to color so contours can be printed in color
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    intense_img = img  # to show algorithm removing small shapes

    # Display images
    cv2.drawContours(img, otsu_contours, -1, GREEN, 1)  # draws contours on an image
    cv2.imshow("Image With Otsu Contours", img)
    cv2.imshow("Image with Otsu Thresholding", otsu_threshold)

    # --------intensive detection----------------
    min_c_size = LargestContourPerim(otsu_contours) * .1

    # iterate through contour array and remove small shapes
    for i_shape in range(len(otsu_contours)):
        if VerifyContour(otsu_contours[i_shape], min_c_size):
            cv2.drawContours(intense_img, otsu_contours, i_shape, GREEN, 1)
        else:
            cv2.drawContours(intense_img, otsu_contours, i_shape, RED, 1)

    # Display images
    cv2.imshow("Intense Filtered Shapes", intense_img)

    # ---------Use Coordinate Shape-------------------
    # until the populate func is done, this wont work for the very first images
    detected_img = image
    for i_shape in range(len(otsu_contours)):
        # are the coordinates contained within the shape
        if 1 == cv2.pointPolygonTest(otsu_contours[i_shape], (im_x, im_y), False):
            cv2.drawContours(detected_img, otsu_contours, i_shape, GREEN, 1)
    cv2.imshow("Detected Shape", detected_img)

    # wait until a key is pressed, then delete current images and generate next frame
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image %i Complete" % i_frame, "\n")
    i_frame += 1
    success, image = artery_vid.read()