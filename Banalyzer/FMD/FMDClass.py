# This class will calculate the flow-mediated dilation for a user-input test (test_name) and
# user-input file (file_path).
import FMD.FMDCalcs as FMDCalcs

# stores information for each .avi file being processed (ie baseline name, diameter array etc)
# this will only be used to store and retrieve information, it will not directly interact with the GUI
# since the number of classes will be user generated, i think we need to have a list of classes
class classFMD:
    def __init__(self, test_name, file_path, study_name, patient_name):
        self.test_name = test_name  # name of user (baseline, 1mn ....)
        self.file_path = file_path
        self.study_name = study_name
        self.patient_name = patient_name
        self.diameter_arr = []
        self.conf_arr = []
        self.percent_dif = []
        self.percent_dif_flag = []
        self.xy_user_click = [None, None]  # if [None, None] then user doesnt have click saved
        self.cropped_bounds = []  # start y end y, start x and x (for cropping the original image)
        # self.max_image_size = []  # [max row, max col]
        self.widget_size = []  # [row, col]    pixel size of widget storing image
        self.opencv_widge_size = [] # [300, 558] # [row, col] for some reason the opencv and pyqt have different dimensions
        self.pixel2real_conversion = None
        self.real_diam_arr = []
        self.threshold = None
        self.frame1pixelvals = None # this stores the pixel list opencv uses for first frame from a file
                                # this is done to reduce lookup speed when using the threshold slider
        self.artery_slider_coord = []  # used to restrict the artery width for measuring [x0, x1]
        self.is_baseline = False

    # Replaces class artery diameter array with input
    def AddDiameterArr(self, diameter_arr):
        self.diameter_arr = diameter_arr

    # adds element to the class diameter array
    def Add2DiameterArr(self, diameter):
        self.diameter_arr.append(diameter)

    def GetRecentDiam(self):
        return self.diameter_arr[-1]

    # Replaces class confidence array with input
    def AddConfidenceArr(self, conf_arr):
        self.conf_arr = conf_arr

    # adds confidence element to class confidence array
    def Add2ConfidenceArr(self, conf):
        self.conf_arr.append(conf)

    def UpdateXY(self, x, y):
        self.xy_user_click = [x, y]

    # if self.xy is [Null,Null] return false
    def CheckXY(self):
        if self.xy_user_click[0] is None and self.xy_user_click[1] is None:
            return False
        else:
            return True

    def GetXY(self):
        return self.xy_user_click

    def SetCropBounds(self, start_y, end_y, start_x, end_x):
        self.cropped_bounds = [[start_y, end_y], [start_x, end_x]]

    def GetCropRow(self):
        return self.cropped_bounds[0]

    def GetCropCol(self):
        return self.cropped_bounds[1]

    def SetMaxImageSize(self, max_row, max_col):
        self.max_image_size = [max_row, max_col]

    def SetWidgetSize(self, width, height):
        self.widget_size = [width, height]

    def SetPixel2Real(self):
        self.pixel2real_conversion = FMDCalcs.CalcPixel2RealConversion()

    def PercentDif(self):
        self.percent_dif.append(0)
        self.percent_dif_flag.append(0)
        for i in range(1, len(self.diameter_arr)):
            self.percent_dif.append(abs(100 * (self.diameter_arr[0] - self.diameter_arr[i]) / self.diameter_arr[0]))

            # %Difference Flags From This:  If the percent difference from the original threshold between any two
            #consecutive threholds is greater than 1 or less than -1, the point will be flagged. Also if greater than
            #5% off of original it will be flagged.

            if ((self.percent_dif[i] - self.percent_dif[i-1]) > 1):
                self.percent_dif_flag.append(1)
            elif ((self.percent_dif[i] - self.percent_dif[i-1]) < -1):
                self.percent_dif_flag.append(1)
            elif (self.percent_dif[i] > 5):
                self.percent_dif_flag.append(1)
            elif (self.percent_dif_flag[i-1] == 1 and self.percent_dif[i] > 2):  #Stricter check if previous frame failed
                self.percent_dif_flag.append(1)
            else:
                self.percent_dif_flag.append(0)

    def PercentDifActual(self):
        for i in range(len(self.diameter_arr)):
            self.percent_dif.append(100 * (self.diameter_arr[0] - self.diameter_arr[i]) / self.diameter_arr[0])

            # %Difference Flags From This:  For now threshold has to be hardcoded?!?
            if ((100 * (self.diameter_arr[0] - self.diameter_arr[i]) / self.diameter_arr[0]) > 40):
                self.percent_dif_flag.append(1)
            elif ((100 * (self.diameter_arr[0] - self.diameter_arr[i]) / self.diameter_arr[0]) < (-40)):
                self.percent_dif_flag.append(1)
            else:
                self.percent_dif_flag.append(0)

    # for some reason the positions given by pyqt (ie user xy click or widget size for crop image in fmd_page)
    # are not the same as stuff drawn in opencv. This converts pyqt pixel position to cv position
    def PyqtPix2CVPix(self, py_coord):
        x = self.widget_size[0]/py_coord[0]
        x = self.opencv_widge_size[0] / x

        y = self.widget_size[1]/py_coord[1]
        y = self.opencv_widge_size[1] / y

        return [x, y]

    def ConvertPix2Real(self, pixel_diam):
        self.real_diam_arr.append(FMDCalcs.CalcPixel2Real(pixel_diam, self.pixel2real_conversion))

# practice class. not used in our final product
class classSTUDENT(classFMD):

    def InputGpa(self, gpa):
        self.gpa = gpa

        def InputStuId(self, student_id):
            self.student_id = student_id

        c = classSTUDENT("GPA", "ID")
        print(c.name)
        print(c.file_path)
        c.InputGpa([4, 3.5, 3.8, 3.2, 3.5])
        c.InputStuId([3001, 3002, 3003, 3004, 3005])
        print(c.gpa)
        print(c.student_id)


# example of dynamically making classes with a list
# ill need to look into this more as best option because its leading to a lot of namespace length
if False:
    class_list = []
    class_list.append(classFMD("One Minute After", "C:/User/Users"))

    print(class_list[0].name)
    print(class_list[0].file_path)
    print("Can the user click the accept button?: ", class_list[0].CheckXY())

    class_list.append(classFMD("baseline", "C:/User/Users"))
    print(class_list[1].name)
    print(class_list[1].file_path)
    class_list[1].AddDiameterArr([567, 8910, 2210, 50])
    print(class_list[1].diameter_arr)
    class_list[1].Add2DiameterArr(1000)
    class_list[1].Add2DiameterArr(2323)
    print(class_list[1].diameter_arr)
