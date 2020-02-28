from PyQt5 import QtGui, QtWidgets

# to set up widget class ... https://stackoverflow.com/questions/32226074/display-opencv-window-on-top-of-pyqts-main-window
# should update pyqt5 label
def OpenCv2QImage(opcv_img, image_obj):
    height, width, channel = opcv_img.shape
    bytes_per_line = 3 * width
    pix_img = QtGui.QImage(opcv_img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
    image_obj.setPixmap(QtGui.QPixmap.fromImage(pix_img))
    image_obj.repaint()

def ReturnXYClick(image_obj):
    click= True
    # need to have x and y relative to the widget, not relative to the window.
    # this will get fucked if the user resizes the window so keep in mind