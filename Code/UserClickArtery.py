# This is simplified code without gui link

import cv2
import numpy as np
from FileSupport import *

# ------------------ Variables ----------------------
# file
image_file_name = '14.05.25 hrs __[0011697].avi'
temp_image_file_path = ReturnTempImagePath()
# colors
RED = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
# UI
im_x, im_y, click_allowed = 1, 1, True


# ------------------Functions-----------------------------------
# left click saves x,y coordinate and right click resets the x,y and allows a reclick
def click_event(event, x, y, flags, param):
    global im_x, im_y, click_allowed
    if event == cv2.EVENT_LBUTTONDOWN:
        click_allowed = False
        print("clicked on [", x, " ", y, "]")
        cv2.circle(image, (x, y), 2, RED, -1)
        cv2.imshow("Pre Processing", image)
        im_x, im_y = x, y
        Populate(image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        click_allowed = True


# populates all of the filtered/detected shape images. This function performs all aspects of their generation
def Populate(img):
    # Convert image to grayscale
    img = cv2.imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
    # Gaussian smooth (need to investigate if we need)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    # Invert Image
    img = np.invert(img)  # !!!!!!!!!!!!!!!!!!!!!
    # Perform Threshold
    _, otsu_threshold = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    # Find contours (edges)
    otsu_contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)  # TREE vs EXTERNAL & SIMPLE vs NONE
    img = np.invert(img)  # DELETE (once we figure out if we dup the image or not)
    # Convert image to color so contours can be printed in color
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for i_shape in range(len(otsu_contours)):
        # are the coordinates contained within the shape
        if 1 == cv2.pointPolygonTest(otsu_contours[i_shape], (im_x, im_y), False):
            cv2.drawContours(img, otsu_contours, i_shape, GREEN, 1)
            # enclose box around the
            simp_box = cv2.minAreaRect(otsu_contours[i_shape])
            simp_box = cv2.boxPoints(simp_box)
            simp_box = np.int0(simp_box)
            cv2.drawContours(img, [simp_box], 0, BLUE, 2)
            # need a case if more than one shape detected
    cv2.imshow("Image with detected contours", img)


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
    # !!!!!!!!!!!!!!!!!!Delete once cropping method deteremined!!!!!!!!!!
    sample_start_row = 144  # measurements are based off the 640x480 sample image
    sample_end_row = 408
    sample_start_col = 159
    sample_end_col = 518
    image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # saves the current frame. Not necessary but may be used in final product
    # image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
    cv2.imwrite(temp_image_file_path + "frame%i.jpg" % i_frame, image)

    cv2.imshow("Pre Processing", image)
    # clickable event. if is redundant, but meant to reduce resource usage
    if click_allowed:
        cv2.setMouseCallback("Pre Processing", click_event)
    else:
        Populate(image)

    # wait until a key is pressed, then delete current images and generate next frame
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image %i Complete" % i_frame, "\n")
    i_frame += 1
    success, image = artery_vid.read()