# this assumes the files are 640x480 and match the cropped range of the sample image
# import contours as contours
import cv2
import numpy

from FileSupport import *

# Declared Variables ###########################
# file vars
image_file_name = '14.05.25 hrs __[0011697].avi'  # this will be given through some file selection of the user
temp_image_file_path = ReturnTempImagePath()  # gives file path for .avi files to be stored
# image vars
sample_start_row = 144  # measurements are based off the 640x480 sample image
sample_end_row = 408
sample_start_col = 159
sample_end_col = 518

# Pull image ###################################
print("Getting image from ", image_file_name, "\n")

artery_vid = cv2.VideoCapture(ReturnImagePath(image_file_name))
if not artery_vid.isOpened():
    print("Couldn't open file")
    sys.exit()  # some popup for the user that the file couldn't be opened

success, image = artery_vid.read()
i_frame = 0
# success = True
while success:  # this is where big files might mess up if every frame is saved
    # crop the image before saving it (using user generated values?)
    image = image[sample_start_row:sample_end_row, sample_start_col:sample_end_col]
    cv2.imwrite(temp_image_file_path + "frame%i.jpg" % i_frame, image)  # npp from CannyEdgeDetection.py is likely
    # faster, but im not sure how well it will work with GUI?

    # start processing the image
    # -----Just trying to draw around artery-------
    img = cv2.imread(temp_image_file_path + "frame%i.jpg" % i_frame, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 150, 200, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # SIMPLE vs NONE

    for cnt in contours:
        cv2.drawContours(img, [cnt], 0, (168, 50, 50), 5) # (168, 50, 50) is red
        cv2.imshow("image", img)
        cv2.imshow("thresh", threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # ---------------------------------------------

    print("File %i finished" % i_frame)
    i_frame += 1
    success, image = artery_vid.read()
