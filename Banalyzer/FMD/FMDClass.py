# This class will calculate the flow-mediated dilation for a user-input test (test_name) and
# user-input file (file_path).

# stores information for each .avi file being processed (ie baseline name, diameter array etc)
# this will only be used to store and retrieve information, it will not directly interact with the GUI
# since the number of classes will be user generated, i think we need to have a list of classes
class classFMD:
    def __init__(self, name, file_path):
        self.name = name  # name of user (baseline, 1mn ....)
        self.file_path = file_path
        self.diameter_arr = []
        self.conf_arr = []

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
class_list = []
class_list.append(classFMD("One Minute After", "C:/User/Users"))

print(class_list[0].name)
print(class_list[0].file_path)

class_list.append(classFMD("baseline", "C:/User/Users"))
print(class_list[1].name)
print(class_list[1].file_path)
class_list[1].AddDiameterArr([567, 8910, 2210, 50])
print(class_list[1].diameter_arr)
class_list[1].Add2DiameterArr(1000)
class_list[1].Add2DiameterArr(2323)
print(class_list[1].diameter_arr)
