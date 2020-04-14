import FMD.FMDCalcs as FMDCalcs
import GUI.GUIHelper as GUI
#import GUI.brachial_ui as GUIbr
import FMD.FMDClass as FMDclass
import cv2
import numpy as np
import time  # just for delay, ill probably delete this
import Excel.excel as excel

import sys

sys.path.append('../')  # could be hacky, need to figure out how to share between files
import Global.gbl_fmd_class_list as gbl_fmd

############Remove the im_x and such and change colors to resources file##############
RED = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
# UI
im_x, im_y, click_allowed = 150, 150, True


########################

# populates all of the filtered/detected shape images. This function performs all aspects of their generation
def Populate(img, img_obj):
    i_class = gbl_fmd.i_class
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
            gbl_fmd.class_list[i_class].Add2DiameterArr(FMDCalcs.ContourMean(otsu_contours[i_shape], length))
            print("Diam:\t", gbl_fmd.class_list[i_class].GetRecentDiam(), " pixels")
            print(gbl_fmd.class_list[i_class].pixel2real_conversion)
            real_diam = gbl_fmd.class_list[i_class].GetRecentDiam()*gbl_fmd.class_list[i_class].pixel2real_conversion
            print("Diam:\t", real_diam , " cm (avg width height, not accurate)")
            gbl_fmd.class_list[i_class].REALDIAMARR = [gbl_fmd.class_list[i_class].REALDIAMARR, real_diam]
    GUI.OpenCv2QImage(img, img_obj)
    # cv2.imshow("Image with detected contours", img)

# this will run the FMD process once an image has been verified.
def PerformFMD(image_path, image_obj):
    # TODO i think i need to reset the diam measured arrays as i use populate in the verify
    # function which updates them
    i_class = gbl_fmd.i_class
    # cant move on if current index hasnt had an xy set
    if gbl_fmd.class_list[i_class].CheckXY():
        # THIS IS THE ONLY PLACE i_class SHOULD BE CHANGED and in FILE_SCREEN. dont want race conditions
        gbl_fmd.i_class += 1
        i_class = gbl_fmd.i_class

        # all files have been verified, start processing
        print(i_class, ": i class")
        print("list length: ", len(gbl_fmd.class_list))
        if i_class >= len(gbl_fmd.class_list):
            gbl_fmd.i_class = 0
            i_class = gbl_fmd.i_class

            print("All verified")

            artery_avi = cv2.VideoCapture(image_path)
            if not artery_avi.isOpened():
                print("Couldn't open file")
                # change to a button alert
                return
            success, image = artery_avi.read()

            # Process and contour each .avi frame ===============================
            # !!!!!!!!!!!!!!!!!!Delete once cropping method determined!!!!!!!!!!
            # should be saved in the user settings
            sample_start_row = 144  # measurements are based off the 640x480 sample image
            sample_end_row = 408
            sample_start_col = 159
            sample_end_col = 518

            gbl_fmd.class_list[i_class].SetCropBounds(sample_start_row, sample_end_row, sample_start_col,
                                                      sample_end_col)
            gbl_fmd.class_list[i_class].SetMaxImageSize(len(image[0]), len(image[1]))
            row = gbl_fmd.class_list[i_class].GetCropRow()
            col = gbl_fmd.class_list[i_class].GetCropCol()

            # should be removing this as the first frame will update all of these
            gbl_fmd.class_list[i_class].SetPixel2Real()

            i_frame = 0

            # if gbl_fmd.class_list[i_class].accepted_contour:
            while success:
                image = image[row[0]:row[1], col[0]:col[1]]
            # cv2.imwrite(image_path + "frame%i.jpg" % i_frame, image
                time.sleep(.01)  # TODO REMOVE
                Populate(image, image_obj)

                print("Image %i Complete" % i_frame, "\n")
                i_frame += 1
                success, image = artery_avi.read()
            excel.PrintHi()
            excel.ExcelReport()
            # else:
            #    print("contour not accepted. shouldnt be possible")
        # need to verify next file, so set up first frame of next index
        else:
            print("showing global class name FMDProcessing  ", gbl_fmd.class_list[i_class].test_name)
            print("print xy in FMDproccessing ", gbl_fmd.class_list[i_class].GetXY())

            image_path = gbl_fmd.class_list[i_class].file_path
            SetFirstFrame(image_path, image_obj)
    else: # user hasnt selected an xy
        print("User hasnt selected xy")
        # Need user indication to select xy


# populates the first frame when pixmap artery image is clicked
def VerifyFrame1(image_path, image_obj):
    g = gbl_fmd.class_list
    i_class = gbl_fmd.i_class
    print("showing global class name FMDProcessing  ", gbl_fmd.class_list[i_class].test_name)
    print("print xy in FMDproccessing ", gbl_fmd.class_list[i_class].GetXY())
    if gbl_fmd.class_list[i_class].CheckXY():
        image = GetFirstFrame(image_path)
        gbl_fmd.class_list[i_class].SetPixel2Real()

        time.sleep(.01)  # TODO REMOVE
        Populate(image, image_obj)
        print("Verifed frame 1", "\n")
    else:
        # this edge case should never happen. this funciton should only trigger if user clicks
        print("user has not defined xy click")
        # TODO have a popup or some error indication that they should click the gui

# gets and returns first frame image
def GetFirstFrame(image_path):
    i_class = gbl_fmd.i_class

    artery_avi = cv2.VideoCapture(image_path)
    if not artery_avi.isOpened():
        print("Couldn't open file")
        # change to a button alert
        return
    success, image = artery_avi.read()
    # Process and contour each .avi frame ===============================
    # !!!!!!!!!!!!!!!!!!Delete once cropping method determined!!!!!!!!!!
    # should be saved in the user settings
    sample_start_row = 144  # measurements are based off the 640x480 sample image
    sample_end_row = 408
    sample_start_col = 159
    sample_end_col = 518

    gbl_fmd.class_list[i_class].SetCropBounds(sample_start_row, sample_end_row, sample_start_col, sample_end_col)
    # gbl_fmd.class_list[i_class].SetMaxImageSize(len(image[0]), len(image[1]))
    row = gbl_fmd.class_list[i_class].GetCropRow()
    col = gbl_fmd.class_list[i_class].GetCropCol()

    # gbl_fmd.class_list[i_class].SetPixel2Real()

    image = image[row[0]:row[1], col[0]:col[1]]
    return image

# updates pixmap cropimage to the first frame image
def SetFirstFrame(image_path, image_obj):
    print("set first frame image path : ", image_path)
    image = GetFirstFrame(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(image_path + "init_frame.jpg", image)
    GUI.OpenCv2QImage(image, image_obj)