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

    print(max([c0[0], c1[0], c2[0], c3[0]]))
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

# turncates a lines coordinates to be at the bounds
def TruncLineWidth(line, x_bounds):
    left_x = x_bounds[0]
    right_x = x_bounds[1]

    x1 = line[0][0]
    x2 = line[1][0]

    if x1 < x2:
        y1 = line[0][1]
        y2 = line[1][1]
    else:
        x1 = line[1][0]
        x2 = line[0][0]
        y1 = line[1][1]
        y2 = line[0][1]

    dxdy = (y2 - y1)/(x1 - x2)
    y_int = y1

    left_y = y_int + left_x*dxdy
    right_y = y_int + right_x*dxdy

    return np.array([[left_x, left_y], [right_x, right_y]])

# checks for points that are perpendicular to the center-line
# tang is tangent coord [[xa ya] [xb yb]] so two coord
def TangDiamMean(contour, tang):
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
    length = CoordDist(tang[0], tang[1])
    length_bin = length / (n_bins + 1)
    bin_arr = np.linspace(length_bin, length - length_bin, n_bins)
    # print(bin_arr)
    for x in bin_arr:
        coord = [x, slope * x + y_int]
        # print(coord)
        # dont have this working so return is not important
    return y_int


# this area divided by center line to find the mean diameter
def ContourMean(contour, length):
    return cv2.contourArea(contour) / length

# this finds out how much the pixel has been stretched by the pixmap as the
# inputted image is fitted to the pixmap size
def CalcPixel2RealConversion():
    return .06  # pixels per mm for ge ultrasound

def CalcPixel2RealConversion3():
    i_class = gbl_fmd.i_class
    pix_per_mm = .06  # pixels per mm for ge ultrasound

    # get the pixel crop width and height
    pix_width = gbl_fmd.class_list[i_class].cropped_bounds[0]
    pix_width = pix_width[1] - pix_width[0]
    pix_height = gbl_fmd.class_list[i_class].cropped_bounds[1]
    pix_height = pix_height[1] - pix_height[0]

    # delete after
    t = pix_height
    pix_height = pix_width
    pix_width = t
    # -----------

    # get the cv width and height
    cv_width = gbl_fmd.class_list[i_class].opencv_widge_size[0]
    cv_height = gbl_fmd.class_list[i_class].opencv_widge_size[1]

    # find ratio between them
    x_rat = pix_width / cv_width   # pix/cv
    y_rat = pix_height / cv_height  # pix/cv

    cv_per_mm_x = pix_per_mm / x_rat  # pix/ mm * cv /pix = cv / mm
    cv_per_mm_y = pix_per_mm / y_rat

    avg = (cv_per_mm_x + cv_per_mm_y) / 2

    return avg


# hardcoded stuff
# the scale is 56X767 pixels (4 cm(?) in 767 pixels
# the cropped image is 359*264 pixels
# ^ as acquired from screenshots so both should be relative
def CalcPixel2RealConversion2():
    i_class = gbl_fmd.i_class

    original_pixel_scale = 767  # pixel size of reference cm size
    n_cm_seg = 4  # number of reference segments in original scale (one segment is cm length)
    pixels_per_cm = original_pixel_scale / n_cm_seg
    n_cm_per_pixel = 1 / pixels_per_cm # maybe keep it as npixel to make more precise?

    # need to have the xy stuff work
    cropped_pixel_x = 359  # found manually (this is the 'frame 0' stuff, so it is scaled to my original gui size)
    cropped_pixel_y = 264  # found manually
    unshrunk_crop_x = 726  # (this is the crop of of the .avi, so its the original image scale)
    scale = unshrunk_crop_x/cropped_pixel_x  # the x crop should be the same, i couldnt tell how large the y crop was
    cropped_pixel_x *= scale
    cropped_pixel_y *= scale

    # USING THE OPENCV VALUES< NOT PYQT
    # the values given by contour and opencv are NOT pixel positions (found this out the hard way)
    widge_x = gbl_fmd.class_list[0].opencv_widge_size[0]
    widge_y = gbl_fmd.class_list[0].opencv_widge_size[1]
    # the x and y dimensions between the widget and the original cropped image need to
    # be the same in order for the conversion to not care about x vs y stretching
    x_ratio = widge_x/cropped_pixel_x
    y_ratio = widge_y/cropped_pixel_y
    print("x ratio: ", x_ratio)
    print("y ratio: ", y_ratio)

    # this ratio is in the cv form, not pixel
    avg_ratio = (x_ratio + y_ratio) / 2
    return avg_ratio*n_cm_per_pixel

def CalcPixel2Real(pixel_diam, pixel2real_conversion):
    return pixel_diam * pixel2real_conversion