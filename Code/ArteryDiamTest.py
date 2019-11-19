import cv2

from FileSupport import *

# Declared Variables ###########################
image_file_name = '14.05.25 hrs __[0011697].avi'  # this will be given through some file selection of the user
temp_image_file_path = ReturnTempImagePath()  # gives file path for .avi files to be stored

# Pull image ###################################
print("Getting image from ", image_file_name, "\n")

artery_vid = cv2.VideoCapture(ReturnImagePath(image_file_name))
if not artery_vid.isOpened():
    print("Couldn't open file")
    sys.exit()  # some popup for the user that the file couldnt be opened

success, image = artery_vid.read()
i_frame = 0
success = True
while success:  # this is where big files might mess up if every frame is saved
    cv2.imwrite(temp_image_file_path + "frame%i.jpg" %i_frame, image)  # npp from CannyEdgeDetection.py is likely faster, but im not sure how well it will work with GUI?
    success, image = artery_vid.read()
    print("Frame %i read" % i_frame)
    i_frame += 1
