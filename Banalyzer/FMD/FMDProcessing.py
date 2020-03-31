import FMD.FMDCalcs as FMDCalcs
import GUI.GUIHelper as GUI
import GUI.brachial_ui as GUIbr
import FMD.FMDClass as FMDclass
import cv2
import numpy as np
import time  # just for delay, ill probably delete this

import sys

sys.path.append('../')  # could be hacky, need to figure out how to share between files
import Global.gbl_fmd_class_list as gbl_fmd
import Excel.excel as excel

############Remove the im_x and such and change colors to resources file##############
RED = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
# UI
im_x, im_y, click_allowed = 150, 150, True


########################

# populates all of the filtered/detected shape images. This function performs all aspects of their generation
def Populate(img, img_obj):
    # Convert image to grayscale
    img = cv2.cvtColor(img,
                       cv2.COLOR_BGR2GRAY)  # imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
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
            center_xy = FMDCalcs.BoxCenterLine(simp_box)
            #          dead = FMDCalcs.TangDiamMean(otsu_contours, center_xy)
            #         cv2.circle(img, tuple([0, dead]), 3, RED, 2)
            cv2.line(img, tuple(center_xy[0]), tuple(center_xy[1]), RED, 2)
            length = FMDCalcs.CoordDist(tuple(center_xy[0]), tuple(center_xy[1]))
            # might need to create namespaces to shorthand these calls
            gbl_fmd.class_list[-1].Add2DiameterArr(FMDCalcs.ContourMean(otsu_contours[i_shape], length))
            print("Diam:\t", gbl_fmd.class_list[-1].GetRecentDiam(), " pixels")
    GUI.OpenCv2QImage(img, img_obj)
    # cv2.imshow("Image with detected contours", img)

# this will run the FMD process once an image has been verified.
def PerformFMD(image_path, image_obj):
    # TODO Deltere following, proves global is saving the class name
    print("showing global class name FMDProcessing  ", gbl_fmd.class_list[-1].name)
    print("print xy in FMDproccessing ", gbl_fmd.class_list[-1].GetXY())
    if gbl_fmd.class_list[-1].CheckXY():
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
            cv2.imwrite(image_path + "frame%i.jpg" % i_frame, image)

            # !!!!!!!! need to implement a clicking opportunity within the GUI
            # !!!!!!!! the coord should already be saved by user, this func shouldnt happen until
            # the user clicks 'accept' or 'run'

            time.sleep(.01)
            Populate(image, image_obj)

            print("Image %i Complete" % i_frame, "\n")
            i_frame += 1
            success, image = artery_avi.read()

        excel.PrintHi()
        excel.ExcelReport()

    else:
         print("user has not defined xy click")
         # have a popup or some error indication that they should click the gui

