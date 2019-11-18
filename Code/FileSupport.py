import os

# takes in file name and finds file path based on the current source code file path and the expected 'Sample_Images'
# file path. image_name should include the file name and file extension
def ReturnImageFilePath(image_name):
    path = os.getcwd()
    path = path.split("Code")[0]
    return path + 'Sample_Images\\2017Dec08 Study__[0001464]\\'+ image_name
