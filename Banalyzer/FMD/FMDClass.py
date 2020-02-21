# This class will calculate the flow-mediated dilation for a user-input test (test_name) and
# user-input file (file_path).



class classFMD:
    def __init__(self, test_name, file_path):
        self.test_name = test_name
        self.file_path = file_path

        def AddArteryArray(self, artery_array):
            self.artery_array = artery_array

        c = classFMD("baseline", "C:/User/Users")
        print (c.test_name)
        print(c.file_path)

        d = classFMD("One Minute After", "C:/User/Users")
        print (d.test_name)
        print(d.file_path)

        c.AddArteryArray([567, 8910, 2210, 50])
        print(c.artery_array)

class classSTUDENT(classFMD):

    def InputGpa(self, gpa):
        self.gpa = gpa

        def InputStuId(self, student_id):
            self.student_id = student_id

        c = classSTUDENT("GPA", "ID")
        print(c.test_name)
        print(c.file_path)
        c.InputGpa([4, 3.5, 3.8, 3.2, 3.5])
        c.InputStuId([3001, 3002, 3003, 3004, 3005])
        print(c.gpa)
        print(c.student_id)

