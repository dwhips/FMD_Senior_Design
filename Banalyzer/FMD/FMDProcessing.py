import FMD.FMDCalcs as FMDCalcs
import GUI.GUIHelper as GUI
# import GUI.brachial_ui as GUIbr
import FMD.FMDClass as FMDclass
import cv2
import numpy as np
import time  # just for delay, ill probably delete this
import Excel.excel as excel
import pydicom
from skimage import exposure
import PIL

import sys

sys.path.append('../')  # could be hacky, need to figure out how to share between files
import Global.gbl_fmd_class_list as gbl_fmd

############Remove the im_x and such and change colors to resources file##############
BLUE = (0, 0, 255)  # opencv uses BGR not RGB
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
########################

# populates all of the filtered/detected shape images. This function performs all aspects of their generation
def Populate(img, img_obj, SaveDiamData):
    i_class = gbl_fmd.i_class

    # TODO the opencv vs pyqt pixel dimensions dont line up
    widge_height = gbl_fmd.class_list[i_class].opencv_widge_size[1]
    left_bound = gbl_fmd.class_list[i_class].artery_slider_coord[0]
    right_bound = gbl_fmd.class_list[i_class].artery_slider_coord[1]

    s = gbl_fmd.class_list[i_class].widget_size

    # Convert image to grayscale
    img = cv2.cvtColor(img,
                       cv2.COLOR_BGR2GRAY)  # imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)

    # Gaussian smooth (need to investigate if we need)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    # Invert Image
    copy = np.invert(img)  # need copy as processing on image will destroy quality
    # Perform Threshold
    if gbl_fmd.class_list[i_class].threshold == None:
        _, otsu_threshold = cv2.threshold(copy, 0, 255, cv2.THRESH_OTSU)
        print(cv2.THRESH_OTSU)
        gbl_fmd.class_list[i_class].threshold = ['otsu', cv2.THRESH_OTSU]
    elif gbl_fmd.class_list[i_class].threshold[0] == 'binary':
        thresh = gbl_fmd.class_list[i_class].threshold[1]
        _, otsu_threshold = cv2.threshold(copy, thresh, 255, cv2.THRESH_BINARY)
    elif gbl_fmd.class_list[i_class].threshold[0] == 'otsu':
        _, otsu_threshold = cv2.threshold(copy, 0, 255, cv2.THRESH_OTSU)

    # now draws user bounds (to restrict artery width measurement)
    cv2.line(otsu_threshold, (left_bound, 0), (left_bound, widge_height), BLACK, 1)
    cv2.line(otsu_threshold, (right_bound, 0), (right_bound, widge_height), BLACK, 1)

    # Find contours (edges)
    otsu_contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)  # TREE vs EXTERNAL & SIMPLE vs NONE
    # Convert image to color so contours can be printed in color
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # draw user click
    #im_x = gbl_fmd.class_list[i_class].widget_size[0]/gbl_fmd.class_list[i_class].xy_user_click[0]
    #im_x = gbl_fmd.class_list[i_class].opencv_widge_size[0] / im_x

    #im_y = gbl_fmd.class_list[i_class].widget_size[1]/gbl_fmd.class_list[i_class].xy_user_click[1]
    #im_y = gbl_fmd.class_list[i_class].opencv_widge_size[1] / im_y

    pyqt_coord = gbl_fmd.class_list[i_class].xy_user_click
    click_coord = gbl_fmd.class_list[i_class].PyqtPix2CVPix(pyqt_coord)
    cv2.circle(img, (int(click_coord[0]), int(click_coord[1])), 1, RED, 2)

    # If multiple shapes contain coordinate this will break. Need case
    for i_shape in range(len(otsu_contours)):
        # are the coordinates contained within the shape
        # need to convert the pyat xy position to opencv to check inside the contour
        pix_width = gbl_fmd.class_list[i_class].cropped_bounds[1]
        pix_width = pix_width[1] - pix_width[0]
        pix_height = gbl_fmd.class_list[i_class].cropped_bounds[0]
        pix_height = pix_height[1] - pix_height[0]
        # pyqt and cv have flipped rows and colomns. Everything about them is different sadly
        cv_width = pix_width / 1.5# gbl_fmd.class_list[i_class].opencv_widge_size[0]
        cv_height = pix_height / 1.06# gbl_fmd.class_list[i_class].opencv_widge_size[1]

        #im_x = gbl_fmd.class_list[i_class].xy_user_click[0]*(cv_width/pix_width) # hardcoded opencv width/pyat width
        #im_y = gbl_fmd.class_list[i_class].xy_user_click[1]*(cv_height/pix_height) # same for height

        if 1 == cv2.pointPolygonTest(otsu_contours[i_shape], (click_coord[0], click_coord[1]), False):
            # otu = otsu_contours[i_shape]
            cv2.drawContours(img, otsu_contours, i_shape, GREEN, 1)
            # enclose box around the contour. This could also be used to re crop image and perform thresholding again
            simp_box = cv2.minAreaRect(otsu_contours[i_shape])
            simp_box = cv2.boxPoints(simp_box)
            # cv2.drawContours(img, [np.int0(simp_box)], 0, BLUE, 2)
            center_xy = FMDCalcs.BoxCenterLine(simp_box)
            # cv2.line(img, tuple(center_xy[0]), tuple(center_xy[1]), RED, 2)


            # now draws user bounds (to restrict artery width measurement)
            cv2.line(img, (left_bound, 0), (left_bound, widge_height), WHITE, 1)
            cv2.line(img, (right_bound, 0), (right_bound, widge_height), WHITE, 1)

            # calculates and saves the array measurements
            if SaveDiamData:
                otu = otsu_contours[i_shape]
                deleteme = gbl_fmd.class_list[i_class].widget_size
                length = FMDCalcs.CoordDist(tuple(center_xy[0]), tuple(center_xy[1]))
                # might need to create namespaces to shorthand these calls
                gbl_fmd.class_list[i_class].Add2DiameterArr(FMDCalcs.ContourMean(otsu_contours[i_shape], length))
                pixel_diam = gbl_fmd.class_list[i_class].GetRecentDiam()
                print("Diam:\t", pixel_diam, " pixels")

                print(gbl_fmd.class_list[i_class].pixel2real_conversion)
                gbl_fmd.class_list[i_class].ConvertPix2Real(pixel_diam)
                real_diam = gbl_fmd.class_list[i_class].real_diam_arr[-1]
                print("Diam:\t", real_diam, " cm (avg width height, not accurate)")
    GUI.OpenCv2QImage(img, img_obj)

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
            print("All verified")
            gbl_fmd.i_class = 0
            for i in range(0, len(gbl_fmd.class_list)):
                image_path = gbl_fmd.class_list[i].file_path
                PerformFMDHelper(image_path, image_obj)
                gbl_fmd.i_class += 1
                gbl_fmd.class_list[i].PercentDif()
                print("printed %dif")

        # need to verify next file, so set up first frame of next index
        else:
            print("showing global class name FMDProcessing  ", gbl_fmd.class_list[i_class].test_name)
            print("print xy in FMDproccessing ", gbl_fmd.class_list[i_class].GetXY())

            image_path = gbl_fmd.class_list[i_class].file_path
            SetFirstFrame(image_path, image_obj)
    else:  # user hasnt selected an xy
        print("User hasnt selected xy")
        # Need user indication to select xy


# for perfroming the fmd after all the files have been verified
def PerformFMDHelper(image_path, image_obj):
    i_class = gbl_fmd.i_class

    artery_numpy = GetFileImage(image_path)

    # gbl_fmd.class_list[i_class].SetMaxImageSize(len(image[0]), len(image[1]))
    row = gbl_fmd.class_list[i_class].GetCropRow()
    col = gbl_fmd.class_list[i_class].GetCropCol()

    # should be removing this as the first frame will update all of these
    gbl_fmd.class_list[i_class].SetPixel2Real()

    for image in artery_numpy:
        # image = artery_numpy[i_frame]
        image = image[row[0]:row[1], col[0]:col[1]]
        Populate(image, image_obj, True)


# populates the first frame when pixmap artery image is clicked
def VerifyFrame1(image_path, image_obj):
    i_class = gbl_fmd.i_class
    print("showing global class name FMDProcessing  ", gbl_fmd.class_list[i_class].test_name)
    print("print xy in FMDproccessing ", gbl_fmd.class_list[i_class].GetXY())
    if gbl_fmd.class_list[i_class].CheckXY():
        image = GetFirstFrame(image_path)
        gbl_fmd.class_list[i_class].SetPixel2Real()

        Populate(image, image_obj, False)
        print("Verifed frame 1", "\n")
    else:
        # this edge case should never happen. this funciton should only trigger if user clicks
        print("user has not defined xy click")
        # TODO have a popup or some error indication that they should click the gui


def GetFirstFrame(image_path):
    i_class = gbl_fmd.i_class

    if gbl_fmd.class_list[i_class].frame1pixelvals is None:
        artery_numpy = GetFileImageFrame1(image_path)
        SetCropBounds(image_path)
        # gbl_fmd.class_list[i_class].SetPixel2Real()

        row = gbl_fmd.class_list[i_class].GetCropRow()
        col = gbl_fmd.class_list[i_class].GetCropCol()

        # gbl_fmd.class_list[i_class].SetPixel2Real()
        # artery_numpy = artery_numpy[0]
        artery_numpy = artery_numpy[row[0]:row[1], col[0]:col[1]]

        # set first frame pixel vals
        gbl_fmd.class_list[i_class].frame1pixelvals = artery_numpy
    else:
        artery_numpy = gbl_fmd.class_list[i_class].frame1pixelvals
    return artery_numpy


# updates pixmap cropimage to the first frame image
def SetFirstFrame(image_path, image_obj):
    print("set first frame image path : ", image_path)
    image = GetFirstFrame(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(image_path + "init_frame.jpg", image)  # TOO do we need this? why are we making jpegs
    GUI.OpenCv2QImage(image, image_obj)

# for the conf page. This returns all the pixels that failed
def GetiFrameiFilePixels(fileframe_list):
    # TODO for now i just have this loading in data. maybe we can store all
    #  the data but 7* files with a numpy arr seems a little too demanding. We will test it out
    pixel_sorted = []
    print(len(gbl_fmd.class_list))
    deleteme = gbl_fmd.class_list
    for i in range(len(gbl_fmd.class_list)):
        pixel_nump = GetFileImage(gbl_fmd.class_list[i].file_path)
        for i_gui_list in range(len(fileframe_list[0])):
            if fileframe_list[0][i_gui_list] == i:
                i_frame = fileframe_list[1][i_gui_list]
                pixel_sorted.append(pixel_nump[i_frame])
        # TODO im scrambling to get this done. Will break if different files have different crops bt
        # that shouldnt happen as the machine type should stay same with each run
    # assumes same crop for each
    row = gbl_fmd.class_list[0].GetCropRow()
    col = gbl_fmd.class_list[0].GetCropCol()

    for i in range(len(pixel_sorted)):
        # image = artery_numpy[i_frame]
        frame = pixel_sorted[i]
        pixel_sorted[i] = frame[row[0]:row[1], col[0]:col[1]]
    return pixel_sorted


# verifies the diacom is a .file extension
def CheckAviFile(image_path):
    if image_path.endswith('.avi'):
        return True
    return False


# converts a .file extension to png
# dicom file is ygb_FULL_422, neeed > rbg (for cv2 imreader)
def ConvertFromDicom(image_path):
    # TODO try dcmread() if not working
    dicom = pydicom.read_file(image_path)

    pix_dicom = dicom.pixel_array
    # new_dicom = pydicom.dcmread(image_path, force=True)
    # new_dicom.pixel_array
    # dicom = pydicom.dcmread(image_path)
    # frames = pydicom.encaps.generate_pixel_data_frame(dicom.pixel_array)
    # print(dicom.file_meta)

    # for i in range(1000):
    #    merge_dicom = []
    #    for j in range(100):
    #        merge_dicom.append(pix_dicom[j])
    #    i+=100
    #    cv2.imshow('dicom frame?', merge_dicom)
    #    print(i)
    #    cv2.waitKey(0)
    # frame_1 = pix_dicom[0]
    cv2.imwrite(image_path + ".png", pix_dicom)
    # cv2.imshow('dicom frame?', frame_1)
    # cv2.waitKey(0)
    # slice = dicom._dataset_slice(dicom)
    # img_shape = list(dicom.pixel_array.shape)
    # img2d = dicom.pixel_array
    # img2d = cv2.cvtColor(img2d, cv2.COLOR_)
    # cv2.imshow('dicom bgr', img2d)
    # cv2.waitKey(0)

    dicom = dicom.pixel_array
    dicom = exposure.equalize_adapthist(dicom)
    # max_dicom = max(dicom)
    # ratio = 255 / max_dicom
    # dicom = [x * ratio for x in dicom]

    cv2.imshow('dicom', dicom)
    cv2.waitKey(0)

    new_dicom = pydicom.dcmread(image_path, force=True)
    cv2.imshow('dicom', new_dicom.pixel_array)
    cv2.waitKey(0)
    return dicom


# gets file of .avi or dicom type and returns usable image type as numpy of pixel values
def GetFileImage(image_path):
    if CheckAviFile(image_path):
        artery_avi = cv2.VideoCapture(image_path)
        if not artery_avi.isOpened():
            print("Couldn't open file")
            # change to a button alert
            return None
        success, image = artery_avi.read()
        i_frame = 0
        image_numpy = []
        while success:
            image_numpy.append(image)
            print("Image %i Complete" % i_frame, "\n")
            i_frame += 1
            success, image = artery_avi.read()
        return image_numpy
    else:
        return ConvertFromDicom(image_path)


# gets file of .avi or dicom type and returns usable image type as numpy of pixel values
def GetFileImageFrame1(image_path):
    if CheckAviFile(image_path):
        artery_avi = cv2.VideoCapture(image_path)
        if not artery_avi.isOpened():
            print("Couldn't open file")
            # change to a button alert
            return None
        success, image = artery_avi.read()
        i_frame = 0
        print("Image %i Complete" % i_frame, "\n")
        success, image = artery_avi.read()
        return image
    else:
        return ConvertFromDicom(image_path)


# sets crop bounds based on the file type (.avi vs dicom)
def SetCropBounds(file_path):
    if CheckAviFile(file_path):
        # change to flip x and y # TODO
        sample_start_y = 80  # crop for the new avi (dicom to avi)
        sample_end_y = 650
        sample_start_x = 350
        sample_end_x = 650
        # sample_start_row = 100 # crop for the new avi (dicom to avi)
        # sample_end_row = 600
        # sample_start_col = 360
        # sample_end_col = 600

        #sample_start_y = 144  # measurements are based off the 640x480 sample image
        #sample_end_y = 408
        #sample_start_x = 159
        #sample_end_x = 518
    else:
        sample_start_row = 0
        sample_end_row = 600
        sample_start_col = 0
        sample_end_col = 600
    i_class = gbl_fmd.i_class
    gbl_fmd.class_list[i_class].SetCropBounds(sample_start_y, sample_end_y, sample_start_x, sample_end_x)
    gbl_fmd.class_list[i_class].opencv_widge_size = [sample_end_x - sample_start_x, sample_end_y - sample_start_y ]