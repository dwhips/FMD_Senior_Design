import FMD
import numpy as np
import math
import cv2

import sys
sys.path.append('../')  # could be hacky, need to figure out how to share between files
import Global.gbl_fmd_class_list as gbl_fmd

# outputs the difference between two coordinates
# c = [x y]
def CoordDist(c0, c1):
    dx2 = (c0[0] - c1[0]) ** 2
    dy2 = (c0[1] - c1[1]) ** 2
    return math.sqrt(dx2 + dy2)


# boxpoints does lowest corner first, then goes clockwise
# This assumes the centerline we want is longer than the vertical centerline. So this could
# cause bugs if the defined box has artifact or problem causing it to be tall/skinny
def BoxCenterLine(rec):
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
    if CoordDist([x1, x2], [y1, y2]) > CoordDist([xa, xa], [yb, yb]):
        return np.array([[x1, y1], [x2, y2]])
    return np.array([[xa, ya], [xb, yb]])


# checks for points that are perpendicular to the center-line
# tang is tangent coord [[xa ya] [xb yb]] so two coord
def TangDiacmean(contour, tang):
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

    # for now icma hardcode 10 points. later should be iterative with left/right buffer width
    # this part finds 10 points on the centerline and uses the tangent to find points on the contour
    n_bins = 10
    length = CoordDist(tang[0], tang[1])
    length_bin = length / (n_bins + 1)
    bin_arr = np.linspace(length_bin, length - length_bin, n_bins)
    # print(bin_arr)
    for x in bin_arr:
        coord = [x, slope * x + y_int]
        # print(coord)
        # dont have this working so return is not important
    return y_int


# this dose the center line area thing brian talked about
def ContourMean(contour, length):
    return cv2.contourArea(contour) / length

# hardcoded stuff
# the scale is 56X767 pixels (4 cm(?) in 767 pixels
# the cropped image is 359*264 pixels
# ^ as acquired from screenshots so both should be relative
def CalcPixel2RealRatio():
    # TODO this one does cm per pixel so icm has 767/4 pixels. maybe its a data type error
    original_pixel_scale = 767  # pixel size of reference cm size
    n_cm_seg = 4  # number of reference segments in original scale (one segment is cm length)
    pixels_per_cm = original_pixel_scale / n_cm_seg
    #n_cm_per_pixel = 1 / pixels_per_cm # maybe keep it as npixel to make more precise?

    # need to have the xy stuff work
    cropped_pixel_x = 552  # found manually, crop size of the .avi file
    cropped_pixel_y = 397  # found manually
    widg_x = gbl_fmd.class_list[0].widget_size[0]
    widg_y = gbl_fmd.class_list[0].widget_size[1]
    # the x and y dimensions between the widget and the original cropped image need to
    # be the same in order for the conversion to not care about x vs y stretching
    x_ratio = widg_x/cropped_pixel_x
    y_ratio = widg_y/cropped_pixel_y

    avg_ratio = (x_ratio + y_ratio) / 2 # change of pixel strech
    print(avg_ratio*pixels_per_cm, " pixels in 1 cm")
    return avg_ratio*pixels_per_cm  # NOW ITS SHIFT OF HOW MANY PIXELS ARE IN A CM

def CalcPixel2RealRatioOG():
    original_pixel_scale = 767  # pixel size of reference cm size
    n_cm_seg = 4  # number of reference segments in original scale (one segment is cm length)
    pixels_per_cm = original_pixel_scale / n_cm_seg
    n_cm_per_pixel = 1 / pixels_per_cm # maybe keep it as npixel to make more precise?
    print("should equal 1: ", n_cm_per_pixel * pixels_per_cm)
    # need to have the xy stuff work
    cropped_pixel_x = 552  # found manually, crop size of the .avi file
    cropped_pixel_y = 397  # found manually
    widg_x = gbl_fmd.class_list[0].widget_size[0]
    widg_y = gbl_fmd.class_list[0].widget_size[1]
    # the x and y dimensions between the widget and the original cropped image need to
    # be the same in order for the conversion to not care about x vs y stretching
    x_ratio = widg_x/cropped_pixel_x
    y_ratio = widg_y/cropped_pixel_y

    avg_ratio = (x_ratio + y_ratio) / 2
    return avg_ratio*n_cm_per_pixel

def CalcPixel2Real(pixel_diam, ratio):
    print(pixel_diam, " pixels  / ", ratio, "pixels/cm")
    return pixel_diam / ratio
