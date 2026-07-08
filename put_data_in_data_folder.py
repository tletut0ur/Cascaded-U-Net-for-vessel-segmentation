import shutil
import os
import pathlib
from glob import glob

def input_folder_image_to_id(folder):
    return int(pathlib.PurePath(folder).stem.split("_")[0])

input_image_folder = r"D:\datasets\brain\IXI_MRA\guest-20260707_145532"
input_gt_folder = r"D:\datasets\brain\IXI_MRA\vessel_dataset"
output_image_folder = r".\data\Images"
output_gt_folder = r".\data\GT"
all_input_folders = glob(os.path.join(input_image_folder, "*\\"))
all_input_ids = list(map(input_folder_image_to_id, all_input_folders))
print(all_input_ids)
shutil.rmtree(output_image_folder, ignore_errors=True)
shutil.rmtree(output_gt_folder, ignore_errors=True)

os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_gt_folder, exist_ok=True)
for gt_image in glob(os.path.join(input_gt_folder, "*.nii.gz")):
    patient_id_gt_str = pathlib.PurePath(gt_image).stem[3:6]
    patient_id_gt = int(pathlib.PurePath(gt_image).stem[3:6])
    print(patient_id_gt)
    if patient_id_gt in all_input_ids:
        shutil.copyfile(gt_image, os.path.join(output_gt_folder, pathlib.PurePath(gt_image).stem.replace(".nii", "") + "_GT.nii.gz"))
        folder_index = all_input_ids.index(patient_id_gt)
        patient_folder = all_input_folders[folder_index]
        glob_file = glob(os.path.join(patient_folder, r"MRA\NIfTI\*.nii.gz"))[0]
        # os.makedirs(os.path.join(output_image_folder, r"{}-IXI".format(patient_id_gt_str)))
        shutil.copyfile(
            glob_file, 
            os.path.join(output_image_folder, r"IXI{}.nii.gz".format(patient_id_gt_str))
        )