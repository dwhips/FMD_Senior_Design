import FMD.FMDClass as FMDclass
import pathlib

# curr_path = pathlib.Path().absolute().parents[1]
# image_file_path = str(curr_path / 'Resources\\14.05.25 hrs __[0011697].avi')

# inits the class list which stores a class for each file
class_list = [] # [FMDclass.classFMD("Test FMD", image_file_path, "study_name", "patient_name")]
# gives index of currently used class
i_class = 0

# for confidence screen. TODO If anyone is working on this code as legacy, definitely tear this out
framefile_list = []
pix_frames_sorted = []
