# this assumes the files are 640x480 and match the cropped range of the sample image

import cv2

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

    print("File %i finished" % i_frame)
    i_frame += 1
    success, image = artery_vid.read()
