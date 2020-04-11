import FMD.FMDClass as FMDclass
import pathlib

curr_path = pathlib.Path().absolute().parents[1]
image_file_path = str(curr_path / 'Resources\\14.05.25 hrs __[0011697].avi')
class_list = [FMDclass.classFMD("Test FMD", image_file_path, "study_name")]
